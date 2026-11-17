import os, html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT, 'figures')
os.makedirs(OUT, exist_ok=True)
INK='#123A5C'; GOLD='#C9A227'; TEAL='#1F5A7A'; CREAM='#F7F4EC'; LIGHT='#DCE6F1'; PALE='#FBF7E9'
GRAY='#555555'; MID='#8A9AA8'; WHITE='#FFFFFF'; GREEN='#2E7D5B'; RED='#A23B3B'; SAND='#E2D3A8'

def esc(s): return html.escape(str(s), quote=False)

def svg(w,h,body,bg=CREAM):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3.5" orient="auto"><path d="M0,0 L10,3.5 L0,7 z" fill="{INK}"/></marker>
<marker id="arrowg" markerWidth="10" markerHeight="10" refX="9" refY="3.5" orient="auto"><path d="M0,0 L10,3.5 L0,7 z" fill="{GOLD}"/></marker>
</defs>
<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>
{body}
</svg>'''

def rect(x,y,w,h,fill,stroke=None,rx=12,sw=2,dash=None,opacity=None):
    o=f' opacity="{opacity}"' if opacity else ''
    s=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    d=f' stroke-dasharray="{dash}"' if dash else ''
    f='none' if fill is None else fill
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"{s}{d}{o}/>'

def txt(x,y,s,size=20,color=INK,bold=False,anchor='start',italic=False,family='Lato',opacity=None):
    w=' font-weight="700"' if bold else ''
    i=' font-style="italic"' if italic else ''
    o=f' opacity="{opacity}"' if opacity else ''
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}"{w}{i} text-anchor="{anchor}"{o}>{esc(s)}</text>'

def lines(x,y,arr,size=16,color=GRAY,leading=None,bold=False,italic=False,anchor='start',family='Lato'):
    if leading is None: leading=size*1.25
    out=[]
    for i,s in enumerate(arr):
        out.append(txt(x,y+i*leading,s,size,color,bold,anchor,italic,family))
    return ''.join(out)

def line(x1,y1,x2,y2,color=INK,w=2,dash=None,arrow=False,marker='arrow'):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    m=f' marker-end="url(#{marker})"' if arrow else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}{m}/>'

def circle(cx,cy,r,fill,stroke=None,sw=2):
    s=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    f='none' if fill is None else fill
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}"{s}/>'

def header(title,sub=None,w=1200):
    out=txt(60,62,title,34,INK,True)
    if sub: out+=txt(60,96,sub,17,GRAY)
    out+=line(60,118,w-60,118,GOLD,3)
    return out

# 1. ladder
b=header('Four chapters, one ladder','The same concepts, met at increasing resolution.')
steps=[
 (60,400,250,230,'1','Foundations','4–8',['Is that the thing,','or a name for it?'],'a wall of five fact cards',LIGHT),
 (335,340,250,290,'2','Rules & search','8–11',['Does it follow?','Have we tried everything?'],'a class rule base and a debug log',PALE),
 (610,270,250,360,'3','Critique','11–15',['What did they not say?'],'a bad-argument rule base',LIGHT),
 (885,190,260,440,'4','Judgement','15–adult',['Where does the model end?'],'a program with a boundary note',PALE),
]
for i,(x,y,w,h,n,name,age,q,build,fill) in enumerate(steps):
    b+=rect(x,y,w,h,fill,SAND,16)
    b+=rect(x,y,w,10,GOLD if i%2==0 else TEAL,None,0)
    b+=txt(x+22,y+47,n,32,GOLD,True)
    b+=txt(x+22,y+82,name,22,INK,True)
    b+=txt(x+22,y+108,age,17,GRAY)
    b+=lines(x+22,y+135,q,18,TEAL,leading=22,italic=True)
    b+=txt(x+22,y+h-55,'THEY BUILD',10.5,GRAY,True)
    b+=txt(x+22,y+h-31,build,14.5,GRAY)
b+=txt(60,675,'Chapters are conceptual; tracks are delivery. They overlap by design.',15,GRAY)
open(f'{OUT}/fig_ladder.svg','w').write(svg(1200,700,b))

# 2. gates
b=header('Nine gates','Each gate is a discrimination, not a vocabulary word.')
gates=[
 (1,'thing vs. name for the thing','5–7',LIGHT),
 (2,'thing vs. slot for a thing','6–8',LIGHT),
 (3,'describing vs. claiming','6–9',LIGHT),
 (4,'adding vs. conditioning','8–10',LIGHT),
 (5,'finding vs. proving','9–12',LIGHT),
 (6,'following vs. feeling','10–14',PALE),
 (7,'saying vs. knowing','13–18',PALE),
 (8,'model vs. world','16–22',LIGHT),
 (9,'derivation vs. output','15–adult',LIGHT),
]
for i,(n,d,age,fill) in enumerate(gates):
    col=i%3; row=i//3
    x=70+col*375; y=160+row*150
    accent=GOLD if n in (6,7) else (TEAL if n in (8,9) else INK)
    b+=rect(x,y,340,125,fill,SAND,14)
    b+=rect(x,y,8,125,accent,None,0)
    b+=txt(x+24,y+42,str(n),28,accent,True)
    # wrap discrimination to two lines
    words=d.split(' ')
    l1=' '.join(words[:3]); l2=' '.join(words[3:])
    b+=txt(x+24,y+76,l1,19,INK,True)
    b+=txt(x+24,y+100,l2,19,INK,True)
    b+=txt(x+300,y+42,age,14,GRAY,False,'end')
b+=txt(70,650,'Gates 1–5: logic.   Gates 6–7: critical thinking.   Gates 8–9: professional and civic.',14,GRAY)
open(f'{OUT}/fig_gates.svg','w').write(svg(1200,680,b))

# 3. tracks
b=header('Five tracks, one backbone','Delivery overlaps by design; the gates, not the birthdays, decide readiness.')
# axis
b+=line(110,520,1130,520,MID,2)
for x,l in [(110,'4'),(340,'8'),(570,'12'),(800,'16'),(1030,'20'),(1110,'adult')]:
    b+=line(x,514,x,526,MID,2)
    b+=txt(x,548,l,14,GRAY,False,'middle')
tracks=[
 (140,430,150,'T1 Elementary','5–11  ·  Stages 0–5  ·  L0–L2',LIGHT),
 (320,590,220,'T2 Middle','10–13  ·  Stages 4–11  ·  L2–L4',PALE),
 (620,870,290,'T3 High School','14–18  ·  Stages 8–12  ·  L4–L5',LIGHT),
 (860,1000,360,'T4 University','18–22  ·  Stages 13–14  ·  L5–L6',PALE),
 (990,1120,430,'T5 Life','adult  ·  Stage 16  ·  LX',LIGHT),
]
for x1,x2,y,label,sub,fill in tracks:
    b+=rect(x1,y,x2-x1,42,fill,SAND,21)
    b+=txt(x1+14,y+27,label,18,INK,True)
    b+=txt(x1,y-10,sub,15,GRAY)
b+=txt(110,585,'A 13-year-old may be in T2 on one concept and T3 on another. That is a feature.',15,GRAY,False,italic=True)
open(f'{OUT}/fig_tracks.svg','w').write(svg(1200,620,b))

# 4. glassbox
b=header('The four parts of every artefact','The first three are the program. The fourth is the lesson.')
b+=rect(220,150,760,400,None,TEAL,24,3,dash='10 7')
b+=txt(600,135,'THE EDGE — what is not on the wall',16,TEAL,True,'middle')
b+=rect(270,200,660,300,LIGHT,TEAL,20,2,opacity='0.55')
b+=txt(600,230,'THE GLASS BOX',13,TEAL,True,'middle')
b+=rect(300,260,260,80,PALE,SAND,12)
b+=txt(430,292,'FACTS',19,INK,True,'middle')
b+=txt(430,316,'what is on the wall',16,GRAY,False,'middle')
b+=rect(640,260,260,80,PALE,SAND,12)
b+=txt(770,292,'RULES',19,INK,True,'middle')
b+=txt(770,316,'what follows',16,GRAY,False,'middle')
b+=rect(470,400,260,70,PALE,SAND,12)
b+=txt(600,428,'QUERY',19,INK,True,'middle')
b+=txt(600,450,'what we ask',16,GRAY,False,'middle')
b+=line(560,320,535,395,INK,2,arrow=True)
b+=line(640,320,665,395,INK,2,arrow=True)
b+=txt(600,590,'A program shown without its edge teaches the closed-world error as a feature.',17,GRAY,False,'middle')
open(f'{OUT}/fig_glassbox.svg','w').write(svg(1200,650,b))

# 5. rungs
b=header('Seven rungs, one ladder','The surface changes; the three parts do not.')
rungs=[
 ('L0','4–7','cards','teacher'),
 ('L1','6–9','paper','pair'),
 ('L2','8–11','LE2','teacher'),
 ('L3','10–13','syntax','student'),
 ('L4','12–15','Prolog','student'),
 ('L5','14–18','limits','student'),
 ('L6','18–22','semantics','student'),
 ('LX','adult','paper','facilitator'),
]
for i,(r,age,surface,agency) in enumerate(rungs):
    x=45+i*145; h=110+i*58; y=640-h
    fill=LIGHT if i%2==0 else PALE
    b+=rect(x,y,132,h,fill,SAND,10)
    b+=txt(x+12,y+32,r,22,GOLD,True)
    b+=txt(x+12,y+54,age,16,GRAY)
    b+=txt(x+12,y+82,surface,18,INK,True)
    b+=txt(x+12,y+104,agency,15,GRAY)
b+=line(45,650,1155,650,MID,2)
b+=txt(45,680,'No Prolog syntax before 10. No cut, NAF-as-logic or material implication before 14.',15,GRAY)
open(f'{OUT}/fig_rungs.svg','w').write(svg(1200,710,b))

# 6. same program
b=header('The same three lines, three resolutions','If it rains, the ground is wet. It rained. Is the ground wet?')
# panel 6
b+=rect(50,150,340,400,PALE,SAND,18)
b+=txt(80,195,'6',34,GOLD,True)
b+=txt(80,225,'Three cards',18,GRAY)
for j,(s) in enumerate(['rain','if rain → wet','wet?']):
    y=255+j*70
    b+=rect(80,y,230,48,LIGHT,TEAL,8)
    b+=txt(195,y+30,s,18,INK,False,'middle')
b+=txt(80,500,'"Which card can you put down? Why?"',15,TEAL,italic=True)
# panel 12
b+=rect(430,150,340,400,PALE,SAND,18)
b+=txt(460,195,'12',34,GOLD,True)
b+=txt(460,225,'Prolog',18,GRAY)
b+=rect(460,255,280,170,'#1B2B3A',None,10)
b+=lines(478,288,['wet :- rain.','rain.','?- wet.'],18,'#E8EEF2',leading=34,family='DejaVu Sans Mono')
b+=txt(460,500,'"Trace it. What if we add a sprinkler?"',15,TEAL,italic=True)
# panel 20
b+=rect(810,150,340,400,PALE,SAND,18)
b+=txt(840,195,'20',34,GOLD,True)
b+=txt(840,225,'A model',18,GRAY)
b+=circle(980,350,72,None,TEAL,3)
b+=txt(980,345,'valid in',17,INK,False,'middle')
b+=txt(980,365,'all models',17,INK,False,'middle')
b+=txt(840,500,'"Is the premise true? How would you know?"',15,TEAL,italic=True)
b+=txt(600,600,'Same program. Three resolutions. This is the whole tuning argument.',16,GRAY,False,'middle')
open(f'{OUT}/fig_sameprogram.svg','w').write(svg(1200,630,b))

# 7. growing
b=header('The Growing Rule Base','One artefact, revisited from age 5 to 18.')
layers=[
 ('5–7','five fact cards'),('7–9','questions'),('9–11','if–then rules'),
 ('11–13','search, negation, counterexamples'),('13–15','Prolog and ghost rules'),
 ('15–16','defaults and limits'),('16–18','audit and public defence')]
for i,(age,label) in enumerate(layers):
    w=380+i*60; x=600-w//2; y=545-i*58
    fill=LIGHT if i%2==0 else PALE
    b+=rect(x,y,w,48,fill,SAND,8)
    b+=txt(x+14,y+30,age,17,GOLD,True)
    b+=txt(x+100,y+30,label,20,INK)
b+=txt(600,625,'It is never thrown away; it is re-represented.',15,GRAY,False,'middle')
open(f'{OUT}/fig_growing.svg','w').write(svg(1200,650,b))

# 8. lesson cycle
b=header('The five-move lesson cycle','Every module uses it; every teacher is trained on it.')
cx,cy,r=600,290,130
pts=[(cx,cy-r),(cx+r*0.95,cy-r*0.31),(cx+r*0.59,cy+r*0.81),(cx-r*0.59,cy+r*0.81),(cx-r*0.95,cy-r*0.31)]
labels=['See it','Say it','Play it','Prove it','Break it']
for i,((x,y),lab) in enumerate(zip(pts,labels)):
    b+=circle(x,y,54,LIGHT,TEAL,3)
    b+=txt(x,y+6,lab,19,INK,True,'middle')
import math
for i in range(5):
    x1,y1=pts[i]; x2,y2=pts[(i+1)%5]
    dx=x2-x1; dy=y2-y1; L=math.hypot(dx,dy)
    b+=line(x1+dx/L*58,y1+dy/L*58,x2-dx/L*58,y2-dy/L*58,GOLD,3,arrow=True,marker='arrowg')
legend=[('See it','a case in the body'),('Say it','the learner’s words'),('Play it','used in a game'),('Prove it','show the chain'),('Break it','find the failure')]
for i,(h,d) in enumerate(legend):
    x=55+i*230
    b+=txt(x,540,h,17,INK,True)
    b+=txt(x,560,d,14,GRAY)
b+=txt(600,610,'A curriculum that stops at “Prove it” produces confident reasoners; only “Break it” produces critical ones.',14.5,GRAY,False,'middle')
open(f'{OUT}/fig_lessoncycle.svg','w').write(svg(1200,640,b))


# 9. T4 CS map
def week7(b,x0,y0,w):
    cw=w/7
    for i in range(8):
        b+=line(x0+i*cw,y0,x0+i*cw,y0+340,'#D8DEE4',1)
    labels=['1–2','3–4','5–6','7–8','9–10','11–12','13–14']
    for i,l in enumerate(labels):
        b+=txt(x0+i*cw+cw/2,y0-14,l,16,GRAY,False,'middle')
    return b

def block7(b,x0,y0,cw,col,label,fill):
    x=x0+(col-1)*cw+3; w=cw-6
    b+=rect(x,y0,w,78,fill,SAND,7)
    words=label.split(' ')
    if len(label)>18 and len(words)>1:
        mid=len(words)//2
        b+=txt(x+7,y0+31,' '.join(words[:mid]),18,INK,True)
        b+=txt(x+7,y0+49,' '.join(words[mid:]),18,INK,True)
    else:
        b+=txt(x+7,y0+40,label,18,INK,True)
    return b

b=header('T4 Computer Science — course map','Two strands, one proof obligation. Seven two-week blocks.')
x0=210; y0=180; cw=(1140-x0)/7
b=week7(b,x0,y0,1140-x0)
b+=txt(60,y0+20,'Logic & argument',15,TEAL,True)
b+=txt(60,y0+165,'Logic programming',15,TEAL,True)
b+=txt(60,y0+310,'Labs',15,TEAL,True)
logic=['Epistemics','Models','Abduction','Uncertainty','Fallacies','AI audit','Project']
lp=['Facts','SLD','Lists','Cut/NAF','findall','Tabling','Debugging']
labs=['Lab 1–2','Lab 3','Lab 4','Lab 5','—','—','Portfolio']
for i,l in enumerate(logic): b=block7(b,x0,y0,cw,i+1,l,LIGHT)
for i,l in enumerate(lp): b=block7(b,x0,y0+145,cw,i+1,l,PALE)
for i,l in enumerate(labs): b=block7(b,x0,y0+290,cw,i+1,l,'#F3E6B8')
b+=txt(60,610,'Assessments: portfolio 40% · lab practical 20% · argument audit 20% · project defence 20%.',14,GRAY)
open(f'{OUT}/fig_t4cs.svg','w').write(svg(1200,650,b))

# 10. T4 General map
b=header('T4 General — course map','Evidence, argument, machines. Seven two-week blocks.')
x0=210; y0=180; cw=(1140-x0)/7
b=week7(b,x0,y0,1140-x0)
b+=txt(60,y0+20,'Evidence',15,TEAL,True)
b+=txt(60,y0+165,'Argument',15,TEAL,True)
b+=txt(60,y0+310,'Machines',15,TEAL,True)
ev=['Sources','Models','Cause','Uncertainty','Evidence audit','Capstone','Presentations']
ar=['Standard form','Validity','Explanation','Fallacies','Manipulation','Capstone','Presentations']
ma=['What AI is','Confidence','Proof','Bias','AI audit','Capstone','Presentations']
for i,l in enumerate(ev): b=block7(b,x0,y0,cw,i+1,l,LIGHT)
for i,l in enumerate(ar): b=block7(b,x0,y0+145,cw,i+1,l,PALE)
for i,l in enumerate(ma): b=block7(b,x0,y0+290,cw,i+1,l,'#F3E6B8')
b+=txt(60,610,'Assessments: portfolio 40% · argument audit 25% · AI audit 15% · capstone 20%.',14,GRAY)
open(f'{OUT}/fig_t4gen.svg','w').write(svg(1200,650,b))

# 11. Argument anatomy
b=header('The anatomy of an argument','The warrant is the ghost rule: the premise you were not given.')
b+=rect(80,220,270,100,PALE,SAND,10)
b+=txt(215,255,'GROUNDS',15,INK,True,'middle'); b+=txt(215,280,'what we have',11,GRAY,False,'middle')
b+=rect(465,220,270,100,PALE,SAND,10)
b+=txt(600,255,'WARRANT',15,INK,True,'middle'); b+=txt(600,280,'why the grounds support it',11,GRAY,False,'middle')
b+=rect(850,220,270,100,PALE,SAND,10)
b+=txt(985,255,'CLAIM',15,INK,True,'middle'); b+=txt(985,280,'what we want to establish',11,GRAY,False,'middle')
b+=line(350,270,465,270,INK,2,arrow=True)
b+=line(735,270,850,270,INK,2,arrow=True)
b+=rect(465,380,270,70,'#F3E6B8',SAND,10)
b+=txt(600,410,'REBUTTAL',13,INK,True,'middle'); b+=txt(600,432,'unless something blocks the warrant',10,GRAY,False,'middle')
b+=line(600,320,600,380,TEAL,2,dash='6 4',arrow=True)
b+=txt(985,190,'QUALIFIER: probably · on the whole',11,GOLD,True,'middle')
b+=txt(600,500,'Write down the warrant. Then ask whether it is true, or merely familiar.',12,GRAY,False,'middle')
open(f'{OUT}/fig_argument.svg','w').write(svg(1200,530,b))

# 12. SLD trace
b=header('A search tree you can see','Depth-first search, a choice point, and a backtrack.')
b+=rect(430,150,340,60,LIGHT,TEAL,10)
b+=txt(600,185,'?- ancestor(ana, X).',14,INK,False,'middle',family='DejaVu Sans Mono')
b+=line(600,210,480,270,INK,2,arrow=True)
b+=line(600,210,720,270,INK,2,arrow=True)
b+=rect(340,270,280,60,PALE,SAND,10)
b+=txt(480,305,'parent(ana, X)',13,INK,False,'middle',family='DejaVu Sans Mono')
b+=rect(620,270,300,60,PALE,SAND,10)
b+=txt(770,305,'parent(ana, Z), ancestor(Z, X)',12,INK,False,'middle',family='DejaVu Sans Mono')
b+=line(480,330,480,390,INK,2,arrow=True)
b+=txt(480,420,'X = bob  ✓',13,GREEN,True,'middle')
b+=line(770,330,770,390,INK,2,arrow=True)
b+=rect(640,390,260,55,'#F6DADA',RED,8)
b+=txt(770,422,'fail: no clause',12,RED,True,'middle')
b+=line(770,445,600,445,RED,2,dash='6 4')
b+=line(600,445,600,340,RED,2,dash='6 4',arrow=True)
b+=txt(590,470,'backtrack to the choice point',11,RED,False,'end')
open(f'{OUT}/fig_trace.svg','w').write(svg(1200,520,b))


print('figures written')
