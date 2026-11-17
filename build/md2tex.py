import re, sys, os, html

SPECIAL = {
 '&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}',
 '~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}',
}
SYM = {
 '→':r'$\rightarrow$','←':r'$\leftarrow$','×':r'$\times$','·':r'$\cdot$',
 '≤':r'$\le$','≥':r'$\ge$','≠':r'$\ne$','⊢':r'$\vdash$','¬':r'$\neg$',
 '∧':r'$\wedge$','∨':r'$\vee$','∀':r'$\forall$','∃':r'$\exists$',
 '↔':r'$\leftrightarrow$','✓':r'$\checkmark$','∞':r'$\infty$','±':r'$\pm$',
}

def esc(s):
    s=''.join(SPECIAL.get(c,c) for c in s)
    for k,v in SYM.items(): s=s.replace(k,v)
    return s

def inline(s):
    # protect inline code
    codes=[]
    def stash(m):
        codes.append(m.group(1)); return f'@@CODE{len(codes)-1}@@'
    s=re.sub(r'`([^`]+)`', stash, s)
    # straight double quotes become typographic pairs, in order of appearance
    out=[]; opened=False
    for ch in s:
        if ch=='"':
            out.append('@@RQ@@' if opened else '@@LQ@@')
            opened=not opened
        else:
            out.append(ch)
    s=''.join(out)
    s=esc(s)
    # links
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: r'\href{'+m.group(2)+'}{'+m.group(1)+'}', s)
    # bold then italic
    s=re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\\textit{\1}', s)
    s=s.replace('@@LQ@@', r'\textquotedblleft{}').replace('@@RQ@@', r'\textquotedblright{}')
    def restore(m):
        i=int(m.group(1)); return r'\texttt{\detokenize{'+codes[i]+'}}'
    s=re.sub(r'@@CODE(\d+)@@', restore, s)
    return s

def parse_meta(lines):
    meta={}
    if lines and lines[0].strip()=='---':
        i=1
        while i<len(lines) and lines[i].strip()!='---':
            if ':' in lines[i]:
                k,v=lines[i].split(':',1); meta[k.strip()]=v.strip()
            i+=1
        return meta, lines[i+1:]
    return meta, lines

def table_tex(rows, caption=None):
    n=len(rows[0])
    # skip separator row if present
    body=[r for r in rows if not all(re.fullmatch(r':?-{2,}:?', c.strip() or '---') for c in r)]
    if not body: return ''
    header=body[0]; data=body[1:]
    size=r'\scriptsize' if n>=6 else (r'\footnotesize' if n>=4 else r'\small')
    spec='@{}'+''.join('>{\\raggedright\\arraybackslash}X' for _ in range(n))+'@{}'
    out=[r'\begin{center}',r'\vspace{2pt}',r'\rowcolors{2}{white}{pale}',size,r'\begin{tabularx}{\textwidth}{'+spec+'}',r'\toprule',r'\rowcolor{ink}']
    out.append(' & '.join(r'\textcolor{white}{\textbf{'+inline(c.strip())+'}}' for c in header)+r' \\')
    out.append(r'\midrule')
    for r in data:
        r=(r+['']*n)[:n]
        out.append(' & '.join(inline(c.strip()) for c in r)+r' \\')
    out+= [r'\bottomrule',r'\end{tabularx}',r'\end{center}',r'\vspace{4pt}']
    return '\n'.join(out)

def render(lines):
    out=[]; i=0
    while i<len(lines):
        ln=lines[i]
        s=ln.strip()
        if not s:
            i+=1; continue
        if s.startswith('<!-- part:'):
            t=s[len('<!-- part:'):].rstrip('->').strip()
            t=re.sub(r'^Part\s+[IVXLC]+\s*[—–-]\s*', '', t)
            out.append(r'\part{'+inline(t)+'}'); i+=1; continue
        if s=='<!-- pagebreak -->':
            out.append(r'\newpage'); i+=1; continue
        if s.startswith('```'):
            lang=s[3:].strip()
            i+=1; code=[]
            while i<len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i+=1
            i+=1
            out.append(r'\begin{lstlisting}[style=codebox]')
            out.append('\n'.join(code))
            out.append(r'\end{lstlisting}')
            continue
        m=re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            level=len(m.group(1)); title=m.group(2).strip()
            if level==1:
                if title.startswith('^ '):
                    t=title[2:].strip()
                    out.append(r'\chapter*{'+inline(t)+'}')
                    out.append(r'\addcontentsline{toc}{chapter}{'+inline(t)+'}')
                    out.append(r'\markboth{'+inline(t)+'}{}')
                else:
                    t=re.sub(r'^\d+\.\s+','',title)
                    out.append(r'\chapter{'+inline(t)+'}')
            elif level==2:
                if title.startswith('^ '):
                    t=title[2:].strip()
                    out.append(r'\section*{'+inline(t)+'}')
                    out.append(r'\addcontentsline{toc}{section}{'+inline(t)+'}')
                else:
                    out.append(r'\section{'+inline(title)+'}')
            elif level==3:
                out.append(r'\subsection{'+inline(title)+'}')
            else:
                out.append(r'\subsubsection{'+inline(title)+'}')
            i+=1; continue
        if s.startswith('!['):
            m=re.match(r'!\[([^\]]*)\]\(([^)]+)\)(?:\{width=([0-9.]+)\})?', s)
            if m:
                cap,path,w=m.group(1),m.group(2),m.group(3) or '0.92'
                out.append(r'\begin{figure}[htbp]')
                out.append(r'\centering')
                out.append(r'\includegraphics[width='+w+r'\linewidth]{'+path+'}')
                if cap: out.append(r'\caption{'+inline(cap)+'}')
                out.append(r'\end{figure}')
                i+=1; continue
        if s.startswith('|') and i+1<len(lines) and lines[i+1].strip().startswith('|'):
            rows=[]; j=i
            while j<len(lines) and lines[j].strip().startswith('|'):
                raw=lines[j].strip().strip('|')
                cells=[c.strip() for c in raw.split('|')]
                rows.append(cells); j+=1
            # separator may be row index 1
            out.append(table_tex(rows))
            i=j; continue
        if s.startswith('::: '):
            kind, title = (s[4:].split(' ',1)+[''])[:2]
            kind=kind.strip(); title=title.strip()
            i+=1; buf=[]
            while i<len(lines) and lines[i].strip()!=':::':
                buf.append(lines[i]); i+=1
            i+=1
            box={'box':'curriculumbox','warning':'warningbox','lesson':'lessonbox'}.get(kind,'curriculumbox')
            out.append(r'\begin{'+box+'}{'+inline(title)+'}')
            out.append(render(buf))
            out.append(r'\end{'+box+'}')
            continue
        if s.startswith('- '):
            items=[]; j=i
            while j<len(lines) and lines[j].strip().startswith('- '):
                items.append(lines[j].strip()[2:].strip()); j+=1
            out.append(r'\begin{itemize}[leftmargin=1.2em,itemsep=2pt,topsep=2pt]')
            for it in items: out.append(r'\item '+inline(it))
            out.append(r'\end{itemize}')
            i=j; continue
        if re.match(r'^\d+\.\s+', s):
            items=[]; j=i
            while j<len(lines) and re.match(r'^\d+\.\s+', lines[j].strip()):
                items.append(re.sub(r'^\d+\.\s+','',lines[j].strip())); j+=1
            out.append(r'\begin{enumerate}[leftmargin=1.4em,itemsep=2pt,topsep=2pt]')
            for it in items: out.append(r'\item '+inline(it))
            out.append(r'\end{enumerate}')
            i=j; continue
        if s.startswith('> '):
            out.append(r'\begin{quote}\itshape '+inline(s[2:].strip())+r'\end{quote}')
            i+=1; continue
        if s=='---':
            out.append(r'\vspace{4pt}\noindent\textcolor{gold}{\rule{\linewidth}{0.8pt}}\vspace{4pt}')
            i+=1; continue
        # paragraph: collect until blank/block
        buf=[s]; j=i+1
        while j<len(lines) and lines[j].strip() and not re.match(r'^(#{1,4}\s|```|\||- |\d+\.\s|> |::: |!\[|<!--)', lines[j].strip()):
            buf.append(lines[j].strip()); j+=1
        out.append(inline(' '.join(buf))+'\n')
        i=j
    return '\n'.join(out)

PREAMBLE=r'''
\documentclass[11pt,a4paper,oneside]{book}
\usepackage{fontspec}
\setmainfont{Lato}
\setsansfont{Lato}
\setmonofont{DejaVu Sans Mono}[Scale=0.82]
\usepackage[a4paper,top=2.2cm,bottom=2.2cm,left=2.2cm,right=2.2cm,headheight=14pt]{geometry}
\usepackage[table]{xcolor}
\definecolor{ink}{HTML}{123A5C}
\definecolor{gold}{HTML}{C9A227}
\definecolor{teal}{HTML}{1F5A7A}
\definecolor{cream}{HTML}{F7F4EC}
\definecolor{lightblue}{HTML}{DCE6F1}
\definecolor{pale}{HTML}{FBF7E9}
\definecolor{grayx}{HTML}{555555}
\definecolor{sand}{HTML}{E2D3A8}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\newtcolorbox{curriculumbox}[1]{enhanced,breakable,colback=cream,colframe=gold,title={#1},fonttitle=\sffamily\bfseries\small,boxrule=0.6pt,arc=2mm,left=3mm,right=3mm,top=2mm,bottom=2mm}
\newtcolorbox{warningbox}[1]{enhanced,breakable,colback=red!4,colframe=red!55!black,title={#1},fonttitle=\sffamily\bfseries\small,boxrule=0.6pt,arc=2mm,left=3mm,right=3mm,top=2mm,bottom=2mm}
\newtcolorbox{lessonbox}[1]{enhanced,breakable,colback=lightblue!45,colframe=teal,title={#1},fonttitle=\sffamily\bfseries\small,boxrule=0.6pt,arc=2mm,left=3mm,right=3mm,top=2mm,bottom=2mm}
\usepackage{booktabs,tabularx,array,longtable}
\arrayrulecolor{sand}
\renewcommand{\arraystretch}{1.3}
\usepackage{tocloft}
\setcounter{tocdepth}{0}
\setlength{\cftchapnumwidth}{2.6em}
\setlength{\cftsecnumwidth}{2.9em}
\setlength{\cftsubsecnumwidth}{3.3em}
\usepackage{titlesec}
\titleformat{\chapter}[block]{\normalfont\sffamily\bfseries\Huge\color{ink}}{\color{gold}\thechapter}{0.45em}{}[\vspace{4pt}{\color{gold}\titlerule[2pt]}]
\titlespacing*{\chapter}{0pt}{0pt}{16pt}
\titleformat{\section}{\normalfont\sffamily\Large\bfseries\color{ink}}{\thesection}{0.6em}{}
\titleformat{\subsection}{\normalfont\sffamily\large\bfseries\color{teal}}{\thesubsection}{0.6em}{}
\titleformat{\part}[display]{\centering\normalfont\sffamily\bfseries\color{ink}}{\Huge Part \thepart}{1cm}{\Huge}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\fancyhead[L]{\footnotesize\sffamily\color{grayx}\RUNNING}
\fancyhead[R]{\footnotesize\sffamily\color{grayx}\leftmark}
\fancyfoot[C]{\footnotesize\sffamily\color{grayx}\thepage}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\usepackage{graphicx}
\graphicspath{{/home/jacinto/Desktop/Curricula/}}
\usepackage{listings}
\lstdefinestyle{codebox}{basicstyle=\ttfamily\footnotesize,backgroundcolor=\color{pale},frame=single,rulecolor=\color{sand},breaklines=true,columns=fullflexible,keepspaces=true,aboveskip=6pt,belowskip=6pt}
\usepackage{enumitem}
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage[hidelinks]{hyperref}
\usepackage{tikz}
\usepackage{pagecolor}
\usepackage{eso-pic}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\begin{document}
'''

def titlepage(meta):
    title=meta.get('title','Curriculum')
    subtitle=meta.get('subtitle','')
    version=meta.get('version','Version 1.0')
    date=meta.get('date','November 2026')
    code=meta.get('doccode','')
    audience=meta.get('audience','')
    n=len(title)
    tsize=40 if n<=24 else (36 if n<=30 else (32 if n<=40 else (28 if n<=52 else 26)))
    tlead=tsize+4
    return rf'''
\thispagestyle{{empty}}
\pagecolor{{cream}}
\AddToShipoutPictureBG*{{\AtPageLowerLeft{{\color{{gold}}\rule{{0.55cm}}{{\paperheight}}}}}}
\vspace*{{2.2cm}}
{{\sffamily\small\color{{grayx}} CURRICULUM DOCUMENT \hfill {inline(code)}}}\par
\vspace{{2.2cm}}
{{\sffamily\bfseries\fontsize{{TITLESIZE}}{{TITLELEAD}}\selectfont\color{{ink}} {inline(title)}}}\par
\vspace{{0.8cm}}
{{\sffamily\Large\color{{teal}} {inline(subtitle)}}}\par
\vspace{{1.2cm}}
{{\color{{gold}}\rule{{0.65\linewidth}}{{2pt}}}}\par
\vspace{{1.2cm}}
{{\sffamily\large\color{{grayx}} {inline(version)} \quad · \quad {inline(date)}}}\par
\vspace{{0.4cm}}
{{\sffamily\large\color{{grayx}} {inline(audience)}}}\par
\vfill
{{\sffamily\small\color{{grayx}} {inline(meta.get('prepared','Prepared by the PEG cross-group drafting group.'))}\\
This document is self-contained. References are listed at the end.}}\par
\vspace{{1cm}}
\newpage
\pagecolor{{white}}
'''.replace('TITLESIZE',str(tsize)).replace('TITLELEAD',str(tlead))

def main(src,dst):
    lines=open(src,encoding='utf8').read().split('\n')
    meta,body=parse_meta(lines)
    content=render(body)
    has_fig=any(l.strip().startswith('![') for l in body)
    figlist=r'\clearpage\listoffigures\clearpage' if has_fig else ''
    running=meta.get('running', meta.get('title','Curriculum')).upper()
    pre=PREAMBLE.replace('\\RUNNING', running.replace('&',r'\&').replace('_',r'\_').replace('%',r'\%').replace('#',r'\#'))
    tex=pre+titlepage(meta)+r'''
\frontmatter
\tableofcontents
\clearpage
'''+figlist+r'''
\mainmatter
'''+content+r'''
\end{document}
'''
    open(dst,'w',encoding='utf8').write(tex)
    print('wrote',dst)

if __name__=='__main__':
    main(sys.argv[1],sys.argv[2])
