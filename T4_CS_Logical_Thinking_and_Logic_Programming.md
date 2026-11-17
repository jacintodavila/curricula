---
title: Logical Thinking and Logic Programming for Computer Science
subtitle: A fourteen-week university curriculum, with lesson notes and labs
version: Version 1.0
date: November 2026
doccode: CURR-T4-CS-001
audience: T4-CS · computer-science students · 18–22
running: T4-CS · Logic and logic programming
prepared: Prepared by the curriculum drafting group. Companion volume to The Glass Box.
---

# ^ Preface

This volume is the computer-science curriculum at T4. It assumes the reader has met the argument of the central document, *The Glass Box*, and turns one track of it into fourteen weeks of teachable material.

The course has two strands that run in parallel for the whole semester.

**Strand A — logic and argument.** What follows from what, why it follows, and what a derivation does not establish. The strand begins with the epistemics of premises and ends with the audit of a machine answer. It is a course in reasoning, not in notation.

**Strand B — logic programming.** Facts, rules and queries as a formal object: unification, resolution, recursion, terms, lists, grammars, control, constraints, tabling and answer-set programming. Each feature is taught twice — once as a convenience, once as a distortion — because the distortion is where the examinable understanding lives.

The two strands share one obligation, stated in week 1 and demanded in every week after it:

> **Every claim that a program is correct must come with the chain that supports it, and with a statement of what the program does not know.**

A student who can write a program and cannot say where it is wrong about the world has learned a tool, not a discipline. This course is designed so that such a student cannot pass.

## ^ What is in this volume

The volume is self-contained for teaching. It contains:

- the course design: aims, outcomes, prerequisites, weekly rhythm, assessment and reading;
- fourteen week chapters, each with learning outcomes, a three-hour plan, lecture notes for both strands, a lab, homework and the errors to expect;
- three fully scripted sessions, for the first week, a lab, and the final defence;
- the project brief, the audit template and the marking rubrics;
- a diagnostic quiz, an examination paper with model answers, and a table of common errors;
- an explicit list of references and sources at the end.

## ^ How to read a week chapter

Every week chapter has the same shape.

**At a glance** is a four-row table: what strand A does, what strand B does, what the lab does, and what is assessed.

**Outcomes** are written as observable actions. They are the contract between the teacher and the student.

**The three hours** is a timing table. It is a default, not a straitjacket; the timings assume a 180-minute session with one break.

**Strand A notes** are the lecture content, written to be read aloud and interrupted.

**Strand B notes** are the lecture content with runnable code. Code is set as it would be typed, and is meant to be typed live.

**Lab** is the exercise that makes the week's concept operational.

**Homework** is short on purpose. The course is assessed by production, not by problem sets.

**Common errors** is the most useful page for a new teacher. It names what students actually do.

## ^ The one rule for teachers

Do not demonstrate a feature before the students have met the problem it solves. A cut demonstrated before a search that needs pruning is a syntax lesson. A cut demonstrated after a search that returns the wrong answer twice is a lesson in commitment.

## ^ Where this volume sits

This is the university volume for computer-science students. It is one of eight documents in the set.

- `00_Overview_and_Map.pdf` — the entry point.
- `G1-3_Foundations.pdf` — grades 1–3.
- `G4-6_Rules_and_Search.pdf` — grades 4–6.
- `G7-9_Critique.pdf` — grades 7–9.
- `G10-12_Judgement.pdf` — grades 10–12.
- `T4_GEN_Logic_Evidence_and_Machines.pdf` — the companion university volume.
- `Adult_PostCollege.pdf` — the post-college sessions.

The course assumes the band 10–12 resolution but does not assume that every student had it. Week 1 includes a repair diagnostic, and the first two weeks re-teach standard form, validity and the hidden premise at university speed. A student who can write a program and cannot state its boundary has not met the course's obligation, whatever her school record says.

The Gricean standard is used in two ways. It is the editorial standard for this volume: one idea per paragraph, every section answering a stated question, terms defined at first use. It is also course content: week 2 introduces implicature as the theory of the unstated warrant, and week 10 uses it to test a public argument. The references list the source.

<!-- part: Part I — The course -->

# 1. Course design

## Aims

By the end of the course, a student should be able to do four things that they could not do at the start.

1. **Reconstruct.** Take a real argument — from a paper, a policy, a bug report, a chatbot — and put it in a form where its premises, its warrant and its conclusion are separate objects.
2. **Test.** Say what would make it fail. Produce a countermodel, a counterexample, a base rate or a missing premise, as the case requires.
3. **Formalise.** Write the argument, or the domain, as a logic program, and explain both what the program means and how it runs.
4. **Bound.** State what the formalisation does not capture, and defend the boundary in public.

The fourth is the one that distinguishes this course from a programming course with a logic unit attached. It is also the one that is hardest to assess, which is why the defence is 20 per cent of the mark and cannot be waived.

## Outcomes

On completion, the student can:

- distinguish validity from soundness, and both from strength of evidence;
- produce a proof of validity and a countermodel for the same sentence;
- explain the declarative and procedural readings of a program and identify where they diverge;
- write, trace and debug programs using facts, rules, recursion, terms, lists, grammars and constraints;
- explain the closed-world assumption, negation as failure, the cut and tabling as semantic choices rather than syntax;
- audit a machine-generated answer and state who is responsible for acting on it;
- document the boundary of a program in writing and defend it orally.

## Prerequisites

Discrete mathematics or its equivalent, including propositional logic and elementary set notation. One semester of programming in any language. No prior Prolog. Students without discrete mathematics may take the course with a two-hour bridge workshop in week 0, covering truth tables, sets, relations and the idea of a model.

The bridge workshop is not remedial in tone and is not optional for those who need it. It exists because the course uses the word *model* in week 3 and cannot afford to define it twice.

## The weekly rhythm

| Segment | Minutes | What happens |
|---|---|---|
| Recall | 10 | Three questions from last week, answered cold |
| Strand A | 55 | Lecture with two built-in interruptions |
| Strand B | 55 | Live coding, typed from scratch, errors included |
| Break | 10 | — |
| Lab | 40 | Paired, assessed formatively |
| Close | 10 | One sentence from each pair: what broke? |

The recall segment is not a quiz. It is three questions asked of named students, with no notes. The purpose is to make retrieval normal, not to rank.

The live-coding segment must include an error. A teacher who types perfect code teaches that the tool is magical; a teacher who types a wrong clause, reads the error, and fixes it teaches the actual skill.

## Assessment

| Component | Weight | What it is | When |
|---|---|---|---|
| Portfolio | 40% | Seven production tasks, one per fortnight | Weeks 2, 4, 6, 8, 10, 12, 14 |
| Lab practical | 20% | A two-hour unseen task: write, trace and debug a small program | Week 11 |
| Argument audit | 20% | A 1,500-word reconstruction and test of a real argument | Week 9 |
| Project defence | 20% | A working program, a boundary note, a fifteen-minute defence | Weeks 13–14 |

The portfolio is not a folder of exercises. Each entry is a production task: something made, with a short note saying what it establishes and what it does not. The seven tasks are listed in Chapter 16.

The pass condition includes the boundary note. A student may submit a perfect program with no boundary note and receive no marks for the project, because the boundary note is the outcome, not the decoration.

## Reading

The course uses one main text for strand B and a set of primary sources for strand A. The full list is in the References. The essential items are:

- Arias, *Logic Programming*, for the formal spine of strand B;
- the Open Logic Project, for models, soundness and completeness;
- Toulmin, *The Uses of Argument*, for the anatomy used in weeks 2 and 9;
- Kahneman, *Thinking, Fast and Slow*, chapters on base rates, for weeks 8–9;
- the SWI-Prolog manual, which is the reference for every predicate used.

Students are not required to buy anything. All items are available online or through the library.

## Software

SWI-Prolog, with the `clpfd`, `tables` and `sgml` libraries, is the reference implementation. s(CASP) is used in week 12 and installed from source or run in the provided container. No student account is required; everything runs locally.

A note on tooling: the course deliberately uses one plain implementation rather than an IDE. The trace facility is the teaching instrument, and an IDE that hides the trace hides the lesson.

# 2. The shape of the semester

## Two strands, one obligation

Strand A moves from premises to machines. Strand B moves from queries to semantics. They meet at four points, marked in the table.

| Weeks | Strand A | Strand B | Meeting point |
|---|---|---|---|
| 1–2 | Epistemics, argument form | Facts, rules, queries | The query as a question |
| 3–5 | Models, validity, countermodels | Unification, SLD | The derivation as a chain |
| 6–7 | Abduction and explanation | Recursion and terms | Explanation as a proof |
| 8–9 | Uncertainty, base rates | Lists, grammars, cut, negation | The missing premise |
| 10–11 | Fallacies and manipulation | findall, CLP(FD) | All the answers |
| 12 | AI audit | Tabling, ASP | Non-monotonicity |
| 13–14 | Project | Debugging, defence | The boundary |

## The four questions

Every week ends with the same four questions, at the resolution the week has earned.

| Weeks | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| 1–2 | What is claimed? | What supports it? | What is assumed? | What would change it? |
| 3–5 | What is the model? | What is a countermodel? | Why does it follow? | What does validity not give? |
| 6–9 | What is the explanation? | What else explains it? | How strong is the evidence? | What is missing? |
| 10–12 | What is the search space? | Was it exhausted? | What does silence mean? | Where is the boundary? |
| 13–14 | What does it know? | What does it not know? | Why this answer? | What would change it? |

The questions are printed on the lab sheet every week. By week 12 students should be asking them without the sheet.

## What the course refuses to do

- It does not teach Prolog syntax before the student has needed it.
- It does not teach a fallacy name without the question that dissolves it.
- It does not treat a passing test suite as evidence of correctness.
- It does not let a program be submitted without its boundary.
- It does not assess recall of definitions.

<!-- part: Part II — The fourteen weeks -->

# 3. Week 1 — Epistemics and the proof obligation; facts, rules, queries

## At a glance

| Strand | Content |
|---|---|
| Strand A | Where premises come from; the proof obligation |
| Strand B | Facts, rules, queries; the shape of a program |
| Lab | Read a program, predict its answers, then run it |
| Assessed | Nothing formally; diagnostic quiz at the end |

## Outcomes

By the end of the session, the student can:

- distinguish a premise that is observed, measured, stipulated or testified;
- state the proof obligation in their own words;
- read a small program and say what it knows and what it does not;
- explain why a query is a question with a hole in it.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | None; this is week 1. Instead: two questions on the board |
| 10–60 | Strand A | The regress of premises; the four sources; the proof obligation |
| 60–75 | Break | — |
| 75–130 | Strand B | Facts, rules, queries; first program; the edge |
| 130–165 | Lab | Predict-then-run |
| 165–180 | Close | One sentence per pair |

## Strand A notes

### The regress

Put this argument on the board.

> All the files in this directory are encrypted. `notes.txt` is in this directory. Therefore `notes.txt` is encrypted.

Ask the class whether the conclusion follows. It does. Ask whether it is true. They will say they cannot tell, and that is the right answer. The form is valid; the first premise is unverified.

Now ask where the first premise came from. Someone will say "we checked the files". Ask how many. Ask what would happen if a new file were added between the check and the conclusion. The point arrives quickly: **the validity of the argument is independent of the truth of its premises, and the premises are always obtained by something other than deduction.**

This is the regress. To establish a premise deductively you need further premises; the chain ends in observation, measurement, testimony, stipulation or axiom. The last step of every establishment is non-deductive. That is not a defect of logic. It is the division of labour between logic and evidence.

Write the two slogans on the board and leave them there for the semester.

> **Deduction preserves truth. It does not acquire it.**
>
> **Validity is about the form. Truth is about the world.**

### Four sources of premises

Give the class a claim and ask where it came from.

| Source | Example | What it is good for | How it fails |
|---|---|---|---|
| Observation | I saw the error message | Direct, checkable | Attention, instrument, expectation |
| Measurement | The latency is 240 ms | Precision, comparison | Instrument error, sampling, definition |
| Testimony | The maintainer says it is fixed | Coverage beyond one observer | Interest, memory, competence |
| Stipulation | Let "user" mean a registered account | Precision in a specification | Drift between stipulation and world |

The fourth is the one computer scientists use most and examine least. A definition in a specification is a stipulation. It is not true or false; it is more or less useful, and it can diverge from the world. When the code says "user" and the policy says "user", the argument that connects them may be valid and the two words may not mean the same thing.

### The proof obligation

Introduce the obligation as a rule of the course, not as a topic.

> Anyone who asserts that a system is correct owes two things: the chain that supports the claim, and a statement of the conditions under which the chain would fail.

Ask for a show of hands: who has been told "it works on my machine"? Who has said it? The obligation is not an accusation. It is a specification of what "works" has to mean before it can be believed.

Then give the professional version. A test suite is evidence, not proof. A proof is evidence about a model, not about the world. A benchmark is evidence about a distribution, not about this input. Each of these is legitimate; none of them discharges the obligation alone.

**Exercise (five minutes, pairs).** Find one claim in the room — a poster, a slide, the course description — and write down what would have to be true for it to be true, and how anyone would know.

## Strand B notes

### Three parts and an edge

Write this on the board.

```prolog
rain.
wet :- rain.
```

Ask what the program knows. It knows `rain`. It can derive `wet`. Now ask: what does it not know? Someone will say "whether it is actually raining". That is the edge. The program's `rain` is a stipulation, not an observation.

Add the fourth part explicitly.

| Part | In the program | The question it answers |
|---|---|---|
| Facts | `rain.` | What is on the wall? |
| Rules | `wet :- rain.` | What follows? |
| Query | `?- wet.` | What do we ask? |
| Edge | nothing | What is not on the wall? |

The edge is not written in the program. That is exactly why it must be written next to it. A program without a boundary note teaches the closed-world error as a feature.

### The first program

Type this live. Do not paste it.

```prolog
parent(alice, bob).
parent(bob, carol).
parent(carol, dave).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).
```

Ask for the answers to four queries before running them.

```prolog
?- parent(alice, bob).
?- parent(bob, alice).
?- grandparent(alice, carol).
?- grandparent(carol, X).
```

The second is the important one. Prolog answers `false`. Ask the class what `false` means here. It does not mean "Bob is not Alice's parent" in the sense of a fact about the world; it means "this atom is not in the program". That is the closed-world assumption, met in the first hour, before it has a name.

Do not name it yet. Let them feel the gap. Name it in week 4.

### Reading a program

Give them this and ask what it knows and what it does not.

```prolog
eligible(X) :- registered(X), passed(X, logic).
registered(ana).
registered(bo).
passed(ana, logic).
```

Questions:

- Who is eligible? (Ana.)
- Is Bo eligible? (Prolog says false. Is Bo ineligible, or merely not known to have passed?)
- What would you add to make the program answer the second question honestly?

The third question is the whole course in miniature. There are three options: add a fact, add a rule for unknown, or change the representation so that unknown is representable. Each is a design decision with consequences.

### The query as a hole

Write `?- parent(alice, X).` and ask what `X` is. It is not a name. It is a place where a name can go. The query is a statement with a hole in it, and the engine's job is to find fillings.

This is the same object as the variable in the rule. A rule is a statement with holes; a query is a statement with holes; running the program is matching holes to fillings. Say this once, plainly, and it will save a term of confusion.

## Lab: predict, then run

Students work in pairs. Each pair receives a printed program and a sheet of six queries. They must write the predicted answer and the reason before touching the machine. Then they run it and mark the prediction right or wrong.

The programs are deliberately small and include:

- a query that succeeds;
- a query that fails;
- a query with a variable that has two answers;
- a query with a variable that has no answers;
- a query whose answer depends on clause order;
- a query where the "obvious" answer is wrong because a fact is missing.

The last one is the point. Pairs that predicted `false` and wrote "because it is not in the program" get full marks even though the world answer is unknown.

**Debrief question.** Which was harder, predicting or explaining? Almost everyone says explaining. That is the skill the course teaches.

## Homework

Read the first two chapters of the main text. Write, in fewer than 200 words, one claim you believe and the chain that supports it. Bring it to week 2; it will be used.

## Common errors

- Treating `false` as a fact about the world rather than a report about the program.
- Reading `:-` as "if and only if". It is one direction.
- Expecting `grandparent(carol, X)` to fail "because Carol is at the bottom". The direction is in the arguments, not in the tree.
- Assuming the order of clauses is decoration. It is not; it determines the search.

# 4. Week 2 — Argument form; facts, rules and queries in anger

## At a glance

| Strand | Content |
|---|---|
| Strand A | Standard form; grounds, warrant, claim, rebuttal, qualifier |
| Strand B | Arity, argument order, the shape of a rule base |
| Lab | Reconstruct an argument as a rule base |
| Assessed | Portfolio 1: argument in standard form, with a rule base |

## Outcomes

By the end of the session, the student can:

- put a paragraph into standard form with an explicit warrant;
- identify the qualifier and the rebuttal in a real text;
- explain why argument order in a predicate is a design decision;
- encode a small argument as facts and rules, and say what the encoding loses.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions on week 1 |
| 10–65 | Strand A | Toulmin anatomy; standard form; warrant hunting |
| 65–75 | Break | — |
| 75–130 | Strand B | Arity, order, a rule base that mirrors the argument |
| 130–165 | Lab | Argument to rule base |
| 165–180 | Close | Two pairs read their warrant aloud |

## Strand A notes

### The anatomy

Draw the six parts. They are not a diagram to memorise; they are a checklist for reading.

| Part | Question it answers | Example |
|---|---|---|
| Claim | What are we asked to accept? | The build is not reproducible. |
| Grounds | What do we have? | Two machines produced different hashes. |
| Warrant | Why do the grounds support the claim? | Different hashes mean different inputs or different toolchains. |
| Backing | Why should we believe the warrant? | The hash is a function of the input and the toolchain. |
| Qualifier | How strong is the claim? | Probably, on this platform. |
| Rebuttal | When would it fail? | Unless the build embeds a timestamp. |

The warrant is the part that is almost never stated. It is the ghost rule. In a well-made argument it is shared and obvious; in a bad one it is the whole trick.

### Standard form

Give the class a paragraph and reconstruct it together. Use something from the room: a course evaluation, a bug report, a vendor's claim.

> "We should move to the new database. Three teams have migrated and report no incidents, and the vendor's benchmark shows a 40 per cent improvement."

Standard form:

1. Three teams migrated without incidents.
2. The vendor's benchmark shows a 40 per cent improvement.
3. Therefore we should move to the new database.

Then the warrant, which is not stated:

4. What happened to three teams predicts what will happen to us, and the vendor's benchmark measures the workload we care about.

Now the argument is testable. The grounds may be true. The warrant is where the argument lives, and the warrant is false if our workload differs, our team differs, or the benchmark measures throughput on a workload we do not run.

**The move to teach.** Do not attack the grounds. Ask for the warrant. Most arguments are not defeated by denying the evidence; they are defeated by making the implicit premise explicit and showing that it is false.

### Qualifier and rebuttal

Most real claims are qualified and most arguments omit the qualifier. "The build is not reproducible" is a different claim from "the build is not reproducible on Linux with timestamps embedded". Ask students to restore the qualifier and the rebuttal to the vendor argument. The exercise feels pedantic and is not: a claim without a qualifier cannot be tested, because there is no condition under which it would be false.

### Grice and the implicit warrant

The warrant is often not stated. Grice's theory of implicature explains how an unstated warrant can still be communicated, and why the speaker can later deny it.

The Cooperative Principle: make your contribution such as is required, at the stage at which it occurs, by the accepted purpose of the exchange. Four maxims follow: Quality (be true), Quantity (be as informative as required), Relation (be relevant), Manner (be perspicuous).

An **implicature** is what a speaker means without saying. Grice's example: a referee writes only that a candidate's handwriting is excellent. The reader infers that the candidate is poor at philosophy. Nothing was said; everything was meant. The inference is calculable from the words, the situation and the assumption that the referee is cooperating.

Three consequences for this course.

**The warrant is often an implicature.** Reconstruct it by asking what the speaker must have assumed for the grounds to support the claim. In the vendor argument, the unstated warrant is that three teams' experience predicts ours and the benchmark measures our workload. The speaker did not say it because it is obvious to her, or because stating it would invite the test.

**Implicature is cancellable.** A speaker can add a sentence that removes the inference: *Some teams reported no incidents — in fact, all did.* A writer can omit the cancellation and later say she never claimed the stronger thing. The audit must reconstruct the inference and ask whether it was cancelled.

**Flouting is a signal.** A speaker flouts a maxim when she deliberately and openly breaks it. In a specification, an obviously irrelevant detail may be carrying the message: a vendor's case study about a client nothing like you is not evidence, and its presence is the claim. In a code review, "the tests pass on my machine" is under-informative; the implicature is that the environment is the problem.

The audit question is the one the course uses for machine answers: **what would the speaker have to know, and how would she know it?** For a human, the answer is access and interest. For a model, it is a training distribution. Neither is a chain.

Do not let the vocabulary replace the reconstruction. Students should be able to say *what was left out and why it matters* without using the word *implicature*. The word is a handle, not the skill.

## Strand B notes

### Arity is meaning

```prolog
parent(alice, bob).      % alice is a parent of bob
parent(bob, alice).      % the other direction
```

Two arguments, two positions, two meanings. Ask what `parent(alice)` would mean. It would be a different predicate: a one-place property, "is a parent". The arity is not a formatting choice; it is part of the predicate's identity. `parent/1` and `parent/2` are different predicates that happen to share a name.

The same point in a rule base:

```prolog
can_open(Door) :- has_key, unbolted(Door).
```

Here `can_open/1` says which door; `unbolted/1` says which door; `has_key/0` says the key is in hand, for any door. That last decision is a modelling choice, and it is wrong as soon as there are two keys. Ask the class to fix it. They will propose `has_key(Door)`; then ask whether a key is per door or per person, and the model grows a second argument.

### The rule base as an argument

Take the vendor argument and encode the warrant explicitly.

```prolog
migrated(team_a).
migrated(team_b).
migrated(team_c).
no_incident(team_a).
no_incident(team_b).
no_incident(team_c).

safe_to_migrate(Team) :-
    migrated(Team),
    no_incident(Team).

comparable(our_workload, Team) :-
    workload(Team, W),
    workload(ours, W).
```

Now ask: what does `safe_to_migrate(team_a)` establish? It establishes that team A is in the program and had no recorded incident. It does not establish that our migration is safe. The gap between them is the warrant, and the warrant is now a predicate that has to be supplied — `comparable/2` — and there happens to be no fact for it.

This is the most important lab of the first half of the course: making the warrant a predicate that fails for lack of evidence. The program's failure is not a verdict on the world; it is a report that the argument was never completed.

### Order and duplication

Add a second clause and ask what changes.

```prolog
safe_to_migrate(Team) :- benchmark(Team, _).
```

Now team A can be safe for two reasons. Ask whether that is a disjunction or a duplication. It is a disjunction: two routes to the same conclusion. Ask what happens to the trace. The first route is tried; if it succeeds, the second is never seen unless the query asks for more.

This is where the procedural reading starts to matter, and it is worth thirty seconds of confusion now.

## Lab: argument to rule base

Each pair takes one argument from a supplied set of five (a policy, an advertisement, a code review, a news claim, a student's own claim from the homework). They must:

1. put it in standard form with an explicit warrant;
2. encode the grounds as facts;
3. encode the warrant as a rule;
4. run two queries: one that succeeds and one that fails for lack of a premise;
5. write three sentences on what the encoding loses.

The last step is marked as heavily as the encoding. A pair that encodes a complex argument perfectly and claims nothing is lost has not understood the exercise.

## Homework

Finish the portfolio entry. Then find one argument in your own reading for another course and write its warrant in one sentence. Bring it; we will collect three and test them.

## Common errors

- Putting the conclusion first and calling it standard form. Standard form separates the parts; it does not reorder them arbitrarily.
- Writing a warrant that restates the grounds. "Because three teams migrated" is not a warrant.
- Encoding the warrant as a fact. If it is a fact, it is not a warrant; it is an assumption, and assumptions can be wrong.
- Using `;` to mean "and". This is a syntax error that reveals a conceptual one.

# 5. Week 3 — Models and countermodels; unification

## At a glance

| Strand | Content |
|---|---|
| Strand A | Interpretations, models, countermodels; validity as truth in all models |
| Strand B | Terms, substitution, unification; the declarative reading |
| Lab | Find the countermodel, then unify the terms |
| Assessed | Portfolio 2: a sentence, a model and a countermodel |

## Outcomes

By the end of the session, the student can:

- give an interpretation for a sentence and say whether it is a model;
- construct a countermodel for an invalid sentence;
- perform unification by hand and check it with the machine;
- explain why unification is not symmetric in time or cost.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–65 | Strand A | Interpretations; models; validity; countermodels |
| 65–75 | Break | — |
| 75–130 | Strand B | Terms, substitutions, unification, occurs check |
| 130–165 | Lab | Countermodel and unifier |
| 165–180 | Close | One countermodel on the board |

## Strand A notes

### Interpretation

An interpretation is an assignment of truth values to the atomic sentences, plus a domain for the quantifiers. For propositional logic, it is a row of a truth table. Say this plainly; the truth table is not a different topic, it is a bookkeeping device for interpretations.

Take `p → q`. It is false in exactly one interpretation: `p` true, `q` false. That row is the countermodel. Everything else about implication follows from this one fact, including the two "paradoxes" that upset students: a false antecedent makes the conditional true, and a true consequent makes it true.

Ask why. Not because the logician is perverse, but because a conditional is a promise about what happens when the antecedent holds. If the antecedent does not hold, the promise is not broken.

### Validity and countermodels

A sentence is valid when it is true in every interpretation. To show validity you need an argument that covers all rows; to show invalidity you need one row. This asymmetry is the practical centre of the week: **countermodels are cheap, proofs are expensive, and most claims that look valid are not.**

Work three examples.

| Sentence | Status | Witness |
|---|---|---|
| `p → (q → p)` | valid | no countermodel |
| `(p → q) → (q → p)` | invalid | `p` false, `q` true |
| `(p ∧ q) → p` | valid | no countermodel |

For the invalid one, make the class read the countermodel aloud as a situation: "p is false and q is true." Then translate: "The build failed and the tests passed" makes `(p → q)` true and `(q → p)` false. The formula is not a law about causes; it is a truth function.

### The quantifier warning

One sentence, two readings: `∀x ∃y loves(x, y)`. Everyone has someone they love, possibly different people. `∃y ∀x loves(x, y)`. There is one person whom everyone loves. The second entails the first; the first does not entail the second.

Draw both. Students who have not drawn them will conflate them in the exam, and the conflation is not a small error; it is the difference between a theorem and a falsehood.

## Strand B notes

### Terms

A term is a variable, an atom, a number, or a compound of a functor and arguments. Write a few and label the parts.

```prolog
X
alice
42
pair(alice, bob)
tree(leaf, tree(leaf, leaf))
[1,2,3]
[a|[b,c]]
```

The last two are the same term. Ask the class to prove it by unification in their heads, then on the machine.

```prolog
?- [1,2,3] = [X|Y].
X = 1,
Y = [2, 3].
```

### Substitution and unification

A substitution is a mapping from variables to terms. Unification is the process of finding the substitution that makes two terms identical. It is not assignment; it is solving an equation.

Do these by hand, on the board, in this order.

```prolog
?- f(X, b) = f(a, Y).
?- f(X, X) = f(a, b).
?- f(X, g(X)) = f(a, g(a)).
?- X = f(X).
```

The first gives `X = a, Y = b`. The second fails, because one substitution must serve both occurrences. The third succeeds. The fourth is the interesting one; without an occurs check it succeeds and creates a circular term. SWI-Prolog, by default, does not perform the occurs check for performance, and `?- X = f(X).` yields a cyclic term. This is a design decision with consequences; show it, then show `unify_with_occurs_check/2`.

> **The rule to state.** A variable is a hole, and one substitution must fill every occurrence of the same hole consistently. That single sentence is unification.

### The declarative reading

```prolog
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
```

Declaratively: for all X and Z, X is a grandparent of Z if there exists a Y such that X is a parent of Y and Y is a parent of Z. The comma is conjunction; the variables are universally quantified at the clause level, with the body's existential handled by the search.

Procedurally: to solve `grandparent(X, Z)`, solve `parent(X, Y)`, then solve `parent(Y, Z)`, undoing bindings on failure.

Both readings are correct. They are not the same. The declarative reading does not mention order; the procedural one is entirely about order. Week 4 makes the difference bite.

## Lab: countermodel and unifier

Part 1, on paper: each pair receives four sentences. For each, either draw a countermodel or write a short argument that none exists. Two of the four are invalid and two are valid; the pairs do not know which.

Part 2, on the machine: eight unification problems, predicted on paper first. Include `?- f(X, X) = f(a, b).` and `?- X = f(X).` The second will produce a cyclic term; the class should see it and be told what it is.

Part 3: write one clause whose declarative and procedural readings differ in cost, and explain the difference in two sentences.

## Homework

Take a sentence from the lab that you thought was valid and find its countermodel. Write one paragraph on why you thought it was valid.

## Common errors

- Reading `→` as "causes". It is a truth function.
- Treating a countermodel as a counterexample to the premises. It is a counterexample to the form.
- Thinking unification assigns left to right. It solves simultaneously.
- Expecting `f(X, X) = f(a, b)` to succeed "because X can be a and then b". One hole, one filler.
- Confusing a cyclic term with an infinite one. They are different, and both are avoidable.

# 6. Week 4 — Validity, soundness and proof; SLD resolution

## At a glance

| Strand | Content |
|---|---|
| Strand A | Proof by natural deduction; soundness; what a proof does not give |
| Strand B | SLD resolution; the search tree; clause order and fairness |
| Lab | Trace a derivation and draw its tree |
| Assessed | Portfolio 3: a proof and a countermodel for the same sentence |

## Outcomes

By the end of the session, the student can:

- give a natural-deduction proof of a small valid sentence;
- explain why soundness is a property of a proof system and completeness a property of a logic;
- draw the SLD tree for a query;
- explain how clause order changes the tree without changing the declarative meaning.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Countermodels from week 3 |
| 10–60 | Strand A | Proof rules; soundness; the limits of proof |
| 60–75 | Break | — |
| 75–135 | Strand B | SLD by hand; the tree; infinite branches |
| 135–170 | Lab | Trace and tree |
| 170–180 | Close | One tree on the board |

## Strand A notes

### Proof

Introduce four rules only: assumption, conjunction introduction and elimination, conditional introduction and elimination, and modus tollens as derived. Do not build a full natural-deduction system; build enough to prove two things and to see the shape.

Prove `p → (q → p)`.

```
1. p            assumption
2.   q          assumption
3.   p          reiteration of 1
4. q → p        → introduction, 2–3
5. p → (q → p)  → introduction, 1–4
```

Then prove `(p ∧ q) → p`. Then fail, deliberately, to prove `(p → q) → (q → p)`, and produce the countermodel from week 3. The pair — failed proof and successful countermodel — is the lesson. A proof is a finite object that certifies validity; a countermodel is a finite object that certifies invalidity. Between them they decide every propositional sentence, and neither tells you whether the premises are true.

### Soundness and completeness

Define both, and keep them apart.

- **Soundness:** if the proof system derives `φ`, then `φ` is valid. Nothing false is provable.
- **Completeness:** if `φ` is valid, the proof system derives it. Nothing true is unprovable.

Ask which one a bug in the proof checker would violate. (Soundness.) Ask which one a missing rule would violate. (Completeness.) This is the cleanest way to make the distinction stick.

Then say the sentence that matters for the rest of the course:

> Soundness and completeness are properties of the relation between a proof system and a semantics. They say nothing about whether the axioms describe the world.

### What a proof does not give

A proof gives conditional truth: if the premises hold, the conclusion holds. It does not give the premises. In software, the premises are specifications, assumptions about the environment, and invariants. Each is a stipulation, and each can be wrong.

Give the professional example. A proof of a sorting routine establishes that the output is ordered and a permutation of the input, *given* that the comparison function is a total order. If the comparison is inconsistent, the proof is valid and the program is wrong. The proof discharged its obligation; the specification did not.

## Strand B notes

### SLD by hand

Use the family program. Ask for `?- grandparent(alice, Z).` and resolve it step by step on the board.

```
?- grandparent(alice, Z).
   grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
   X = alice
?- parent(alice, Y), parent(Y, Z).
   parent(alice, bob).
   Y = bob
?- parent(bob, Z).
   parent(bob, carol).
   Z = carol
```

Write the substitution at each step. This is the whole of SLD resolution: select a literal, unify with a clause head, replace the literal by the body, repeat. Depth-first, left-to-right.

### The tree

Draw the tree for `?- grandparent(alice, Z).` with both clauses of `parent/2` under each node. Then add a second `grandparent` clause and watch the tree widen.

```prolog
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandparent(X, Z) :- parent(X, Z), parent(Z, _).
```

Ask which clause gives an answer first. Ask whether the second clause changes the set of answers. It does not, in this program, but the order changes the cost. Then give an example where order changes whether an answer is found at all: an infinite branch tried before a finite one.

```prolog
path(X, Y) :- edge(X, Y).
path(X, Y) :- path(X, Z), edge(Z, Y).
```

With a cycle in `edge/2`, the second clause can recurse forever before the first is tried. The declarative reading is fine. The procedural reading diverges. This is the first appearance of the central theme of week 12.

### Fairness

Define it simply: a search is fair if no branch is starved forever. Depth-first search is not fair. That is not a bug in Prolog; it is a consequence of the strategy. The fix is either to reorder the program, to use tabling, or to use a breadth-first or iterative-deepening interpreter.

Do not fix it yet. Show the divergence and leave it. Week 12 fixes it.

## Lab: trace and tree

Students run `?- trace.` on three queries and draw the tree for each, marking:

- every choice point;
- every failure and the backtrack that follows;
- the bindings undone on backtracking.

Then they reorder the clauses of `path/2` and observe the difference. The lab sheet asks for one sentence: "The declarative meaning is unchanged because ______; the procedural behaviour changed because ______."

## Homework

Complete the portfolio entry. Then write a paragraph explaining why a passing test suite does not discharge the proof obligation, using the words *premise*, *model* and *boundary*.

## Common errors

- Calling an invalid argument "unsound". Invalidity is about form; unsoundness is about a true premise set with an invalid form, or about a proof system.
- Drawing the tree without substitutions. The substitutions are the derivation.
- Reordering clauses and expecting the answer set to change. It usually does not; it changes whether you get there.
- Thinking trace output is for debugging only. It is the declarative reading made visible.

# 7. Week 5 — Proof, decision and the limits of checking; resolution in practice

## At a glance

| Strand | Content |
|---|---|
| Strand A | Decision procedures; why validity is expensive; specifications and their models |
| Strand B | Resolution with variables; equality; arithmetic; term inspection |
| Lab | Break a specification, then break an equality |
| Assessed | Nothing new; portfolio 3 is returned with comments |

## Outcomes

By the end of the session, the student can:

- explain why propositional validity is decidable and first-order validity is not;
- distinguish `=/2`, `==/2` and `is/2` and say what each one means;
- explain why arithmetic in Prolog is not relational by default;
- find the case where a specification is satisfied by a program that does the wrong thing.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions on weeks 3–4 |
| 10–60 | Strand A | Decidability, cost, specification models |
| 60–75 | Break | — |
| 75–135 | Strand B | Equality, arithmetic, term inspection |
| 135–170 | Lab | The specification that admits the wrong program |
| 170–180 | Close | One broken specification on the board |

## Strand A notes

### Two decision problems

Propositional validity is decidable: truth tables decide it, and the cost is exponential in the number of atoms. First-order validity is semi-decidable: if a sentence is valid, a proof will eventually be found; if it is not, the search may run forever. This is not a gap in our cleverness; it is a theorem.

The practical consequence is worth stating in the first five minutes: **there is no general procedure that will tell you whether your specification is consistent.** You can find a proof of inconsistency, or you can fail to find one. Failure is not a certificate.

### Why truth tables do not scale

Twenty atoms give a million rows. Fifty give a quadrillion. Real systems have thousands of boolean variables. This is why the world moved to satisfiability solving, and why the satisfiability problem is both theoretically hard and practically tractable on structured instances.

The teaching point is not the complexity theory. It is that the method of week 3 — enumerate the interpretations — is a definition, not an algorithm. Definitions tell you what validity is; algorithms tell you what you can check before lunch.

### Specifications and their models

A specification is a set of sentences. A program is a model of the specification if the sentences are true of it. The danger is familiar and worth an entire hour: **a weak specification has many models, including wrong ones.**

Give this specification for a function that returns the maximum of a list.

```
For every list L and value m:
  max(L, m) is true only if m is a member of L.
```

Ask whether this specification is satisfied by the function that returns the first element of the list. It is. The specification does not say that `m` is greater than or equal to every member. It is satisfied by a wrong program.

Then add the missing conjunct and watch the space of models shrink. This is the same lesson as the ghost rule, in a formal setting: the specification's silence is not permission. Every omitted constraint is a licence for a wrong implementation.

**Exercise.** In pairs, write a specification for `sort/2` with exactly one omitted constraint, and swap with another pair. They must find the wrong program it admits.

## Strand B notes

### Three kinds of equality

| Goal | Meaning | Example |
|---|---|---|
| `X = Y` | unify | `?- X = 1.` succeeds, binds |
| `X == Y` | identical now, no binding | `?- X == 1.` fails if X is unbound |
| `X is Y` | evaluate arithmetic and unify the result | `?- X is 2 + 3.` binds 5 |

Show all three with the same pair of terms.

```prolog
?- X = 1 + 2.
X = 1+2.
?- X is 1 + 2.
X = 3.
?- 1 + 2 == 3.
false.
```

The first is the one that surprises. `1 + 2` is a term, not a number. Prolog does not evaluate unless asked. Ask why this is a good design: because terms are data, and a program that evaluates everything cannot represent an expression as an object.

### Arithmetic is not relational

```prolog
?- 3 is 1 + X.
ERROR: Arguments are not sufficiently instantiated
```

The evaluator needs ground arithmetic. Ask what a relational version would look like, and why implementing it is harder than it looks. CLP(FD) in week 10 is the answer; do not give it yet.

### Term inspection

```prolog
?- functor(foo(a, b), F, N).
F = foo, N = 2.
?- arg(2, foo(a, b), X).
X = b.
?- foo(a, b) =.. L.
L = [foo, a, b].
```

These are the tools for writing interpreters. Mention that week 7 uses them; do not demonstrate.

### Resolution with variables, carefully

Two clauses can share a variable name and mean different things. Rename apart before resolving.

```prolog
p(X) :- q(X).
q(Y) :- r(Y).
```

Resolving `p(a)` gives `q(a)`, then `r(a)`. If you do not rename, you may accidentally constrain the two clauses to the same variable. The machine renames automatically; the student must too, on paper.

Add the occurs-check demonstration from week 3 if it was not seen, and show the standard occurs-check predicate in the manual.

## Lab: the specification that admits the wrong program

Part 1. Each pair receives three specifications and three implementations. Two implementations satisfy the specification and are wrong; one is right. Find the omissions and repair the specification.

Part 2. Each pair writes one specification with a deliberate omission and passes it to another pair, who must produce a wrong program that satisfies it. This is the most reliable way to teach the difference between "passes the tests" and "meets the specification".

Part 3. One query per student: predict the output of `X = 1+2`, `X is 1+2`, `X = 1+2, X == 3`, `X is 1+2, X == 3`. The third fails; the fourth succeeds. Explain in one sentence.

## Homework

Read the section on resolution in the main text. Then find one specification in your own project — a type, an interface comment, a test name — and write the constraint it omits.

## Common errors

- Believing that a failed proof search proves invalidity.
- Treating a specification as complete because it is written down.
- Using `is/2` to test equality of terms. It evaluates.
- Writing `X = Y + 1` and expecting arithmetic.
- Forgetting to rename variables apart when resolving on paper.

# 8. Week 6 — Abduction and explanation; recursion

## At a glance

| Strand | Content |
|---|---|
| Strand A | Deduction, induction, abduction; explanation versus argument |
| Strand B | Recursion: base case, step, termination, modes |
| Lab | Diagnose a failure by abduction; write and break a recursive rule |
| Assessed | Portfolio 4: a diagnosis and a recursive program with a marked floor |

## Outcomes

By the end of the session, the student can:

- distinguish an explanation from an argument for the same conclusion;
- generate competing explanations and rank them by explicit criteria;
- write a recursive predicate with a base case and a step;
- explain why a recursive rule without a reachable base case diverges.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–60 | Strand A | The three inferences; explanation; criteria |
| 60–75 | Break | — |
| 75–130 | Strand B | Recursion; the ancestor shape; termination |
| 130–170 | Lab | Diagnosis and recursion |
| 170–180 | Close | One diagnosis, one divergence |

## Strand A notes

### Three inferences

| Form | From | To | Risk |
|---|---|---|---|
| Deduction | rule + case | result | premises may be false |
| Induction | many cases | rule | the next case may differ |
| Abduction | result + rule | case | the best explanation may be wrong |

Write the schema and one example each.

```
Deduction:  All tests pass. This is a test. Therefore this passes.
Induction:  Tests 1..999 pass. Therefore test 1000 will pass.
Abduction:  The build failed. A missing dependency would make it fail.
            Therefore a dependency is probably missing.
```

Abduction is the inference to the best explanation. It is not valid, and it is indispensable. Every diagnosis, every debugging session, every scientific hypothesis is abductive. The discipline is not to avoid it but to make the candidate set explicit and to say what would discriminate between the candidates.

### Explanation versus argument

An argument aims to establish that a claim is true. An explanation aims to show why it is true, given that it is. The same sentences can serve both purposes, which is why they are confused.

> The service went down because the database ran out of connections.

As an argument: the claim that it went down is supported by the connection exhaustion. As an explanation: the fact that it went down is accounted for by the exhaustion. If you already accept that it went down, the sentence explains; if you do not, it argues. Ask which one the sentence is doing in a post-mortem, and whether the difference matters. It does: an explanation presupposes the fact, and a post-mortem that only explains can leave the fact unestablished.

### Criteria for the best explanation

Do not teach "inference to the best explanation" as a slogan. Give four criteria and make students use them.

| Criterion | Question | Failure mode |
|---|---|---|
| Explanatory scope | How much of the evidence does it account for? | Ad hoc patches |
| Simplicity | How many independent assumptions does it need? | Conspiracy |
| Testability | What observation would discriminate? | Unfalsifiable |
| Fit with background | Does it conflict with what else we know? | Novelty worship |

Then apply them. A production incident: the service is slow, the database is slow, and the network is lossy. Three explanations. Which one accounts for the latency spike at 14:02, the absence of errors, and the recovery at 14:20? The one that does is not thereby true; it is the one to test first.

**The sentence to leave on the board.** The best explanation is the best of the candidates you thought of. Abduction is bounded by imagination, and that is why the candidate set must be written down.

## Strand B notes

### The shape

Every recursive predicate has two parts.

```prolog
ancestor(X, Y) :- parent(X, Y).                 % floor
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y). % step
```

The floor does not call itself. The step calls the predicate on a strictly smaller problem. The order matters procedurally: put the floor first or the recursion may run away before the answer is found.

Ask what happens if the clauses are swapped. With acyclic data, the answer is still found, eventually, after deeper search. With cyclic data, it is not found at all. This is the first time the class sees that clause order is a semantic choice in practice, not a stylistic one.

### Termination

Termination is not guaranteed by the syntax. It is guaranteed by a measure that decreases. On lists, the measure is the tail; on trees, the subterm; on numbers, the predecessor.

```prolog
count([], 0).
count([_|T], N) :- count(T, N0), N is N0 + 1.
```

Ask what decreases. The list. Ask what happens with `count(L, N).` with both arguments unbound. It generates lists forever. The predicate is a relation, not a function, and the modes matter.

### Modes

A mode is a statement of which arguments are inputs and which are outputs. `count(+List, -N)` is the intended mode. The same clause can be run backwards, and then it enumerates. That is a feature and a hazard.

Introduce the mode declaration as documentation, not syntax.

```prolog
% count(+List, -N)
```

Then show `?- count(L, 2).` and let the class watch it produce `[_, _]`. Ask whether that is correct. It is: the relation holds for every two-element list. Ask whether it is useful. Sometimes. Ask whether the program terminates for `?- count(L, N).` It does not.

### Accumulators

Show the accumulator version and explain the trade.

```prolog
count(L, N) :- count_acc(L, 0, N).
count_acc([], A, A).
count_acc([_|T], A0, N) :- A1 is A0 + 1, count_acc(T, A1, N).
```

The accumulator makes the recursion tail-recursive and the cost linear in stack. It also makes the declarative reading less obvious. Present it as an engineering choice with a semantic cost, not as the "right" version.

## Lab: diagnose and recurse

Part 1. A failing system is described in six observations. Each pair writes at least three candidate explanations, ranks them by the four criteria, and names one observation that would discriminate the top two. No pair may write only one explanation; the lab is marked on the candidate set.

Part 2. Write `ancestor/2`, run four queries, then delete the floor and run one. Draw what happens as a chain of calls. Then restore the floor and add a cycle to `parent/2`; observe the divergence and explain it in one sentence.

Part 3. Write `sum_list/2` twice: once with the direct recursion and once with an accumulator. State one advantage and one disadvantage of each, in terms of the declarative reading.

## Homework

Take a bug you have actually fixed. Write the three explanations you considered, the observation that discriminated, and the one you did not consider until later.

## Common errors

- Calling abduction "guessing" and stopping there. The discipline is in the candidate set and the discriminator.
- Writing the recursive clause before the base case and then blaming Prolog.
- Believing that a predicate that works in one mode works in all modes.
- Adding an accumulator and claiming the program is now "more correct". It is faster; it is not more true.

# 9. Week 7 — Explanation under test; terms and recursive data

## At a glance

| Strand | Content |
|---|---|
| Strand A | Diagnosis as abduction; discriminating tests; the cost of a wrong explanation |
| Strand B | Compound terms; recursive data structures; term inspection; building terms |
| Lab | Build a term representation and a traversal |
| Assessed | Nothing new; the argument audit brief is issued |

## Outcomes

By the end of the session, the student can:

- design a test that discriminates between two explanations;
- represent a small language or structure as compound terms;
- write a traversal over a recursive term;
- explain why terms are the right representation for syntax.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–55 | Strand A | Discriminating tests; the cost of a wrong diagnosis |
| 55–70 | Break | — |
| 70–135 | Strand B | Terms, functors, traversal, term inspection |
| 135–170 | Lab | A tiny expression language |
| 170–180 | Close | Argument audit brief |

## Strand A notes

### From explanation to test

An explanation is a hypothesis. A hypothesis earns its keep by predicting something that would not otherwise be the case. The test is not "does the explanation sound right" but "what would we see if it were false".

Work the incident from week 6. The top two explanations are connection exhaustion and a slow query. Both account for the latency. The discriminator is the connection pool metric: exhaustion predicts a saturated pool with waiters; a slow query predicts low utilisation and long query times. One metric separates them. That is a good test.

Ask what makes a test good. It must be:

- **discriminating** — the two explanations predict different observations;
- **feasible** — you can actually observe it;
- **cheap relative to the decision** — the cost of finding out is less than the cost of being wrong;
- **independent** — it does not rely on the same instrument that produced the original observation.

The fourth is the one that is skipped. If the latency measurement is wrong, a second measurement from the same instrument will confirm the same wrong number.

### The cost of a wrong explanation

A wrong diagnosis is not a neutral error. It consumes the fix budget and it teaches the system's operators the wrong lesson. Give a short case: a team spends three days optimising a query that was never slow, because the dashboard's latency metric included a queue that was waiting on a lock. The explanation fit the graph. The graph was the wrong instrument.

The professional version of the proof obligation applies to explanations too: **say what would change your mind, before you act.**

## Strand B notes

### Terms as data

```prolog
expr(num(3)).
expr(add(num(3), num(4))).
expr(mul(add(num(3), num(4)), num(2))).
```

Ask what the last term represents. Draw it as a tree. The term is the tree; the syntax is the drawing. That is the reason to use terms for syntax: the structure of the data is the structure of the language, and recursion over the data is recursion over the language.

### Traversal

```prolog
eval(num(N), N).
eval(add(A, B), V) :- eval(A, VA), eval(B, VB), V is VA + VB.
eval(mul(A, B), V) :- eval(A, VA), eval(B, VB), V is VA * VB.
```

Three clauses, one per constructor. This is the shape of every interpreter the students will write. Point it out; name it; they will meet it again in compilers.

Then add a constructor and watch the program fail with "no clause". That failure is the type error made visible.

```prolog
?- eval(neg(num(3)), V).
false.
```

The program does not say "unknown constructor"; it says false. That is the closed-world assumption again, now in a place where it matters for correctness. The fix is to add a clause, and the discipline is to know that a missing clause is silent.

### Inspection and construction

```prolog
?- expr(E), functor(E, F, N).
?- expr(E), E =.. [F|Args].
```

`=../2` converts between a term and a list. It is the tool for generic traversals, and it is slow. Show it, warn about it, move on.

`copy_term/2` makes a fresh copy. `term_variables/2` lists the variables. These are the tools for meta-programming, which the course does not teach but does use.

### Recursive data beyond arithmetic

Give the class a family tree as terms and ask for a traversal that collects all descendants.

```prolog
descendants(X, Ds) :-
    findall(D, ancestor(X, D), Ds).
```

Do not explain `findall/3` yet; it appears in week 10. Use it as a black box and say so. The point of the week is the recursion, not the collector.

## Lab: a tiny expression language

Each pair implements:

1. a term representation of boolean expressions: `tt`, `ff`, `and/2`, `or/2`, `not/1`;
2. an evaluator;
3. a simplifier that removes `and(tt, X)` and `or(ff, X)`;
4. a pretty-printer;
5. one query that exposes a missing clause.

Then they add a constructor and observe the failure. The lab sheet asks: which of the five parts broke, and why did the breakage not produce an error message?

## Homework

Read the project brief at the end of this volume. Bring three candidate domains for your project, each with one rule that would be interesting to get wrong.

## Common errors

- Representing syntax as strings and then writing a parser by hand for a five-line language.
- Forgetting that a missing clause fails silently.
- Using `=../2` for everything because it is general.
- Writing `eval` with an `is` on the left of a comparison.
- Thinking a pretty-printer is trivial. It is where the ambiguity lives.

# 10. Week 8 — Uncertainty and base rates; lists

## At a glance

| Strand | Content |
|---|---|
| Strand A | Base rates, natural frequencies, Bayes in odds form, calibration |
| Strand B | Lists: construction, `append/3`, `member/2`, accumulators |
| Lab | The test that is 99 per cent accurate and mostly wrong |
| Assessed | Portfolio 5: a base-rate analysis of a real claim |

## Outcomes

By the end of the session, the student can:

- convert a base-rate problem into natural frequencies and compute the answer;
- explain why a highly accurate test can have a low positive predictive value;
- write list predicates in both directions;
- explain the difference between a list and a term.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–60 | Strand A | Base rates; natural frequencies; Bayes in odds |
| 60–75 | Break | — |
| 75–130 | Strand B | Lists; append; member; accumulator patterns |
| 130–170 | Lab | The screening test and the list library |
| 170–180 | Close | One number on the board |

## Strand A notes

### The screening problem

Give the numbers in this form and ask for the answer before showing any formula.

> A condition affects 1 in 1,000 people. A test detects it in 99 per cent of cases and produces a false positive in 5 per cent of people without it. A person tests positive. What is the probability that they have the condition?

Most of the class will say 99 per cent, or 95, or "high". Then do the frequencies.

Out of 1,000 people:

- 1 has the condition; the test detects it: 1 true positive.
- 999 do not; 5 per cent test positive: about 50 false positives.
- Total positives: 51.
- Of those, 1 has the condition: about 2 per cent.

The answer is roughly 2 per cent, and it is not a trick. It is what the numbers say. The prior is doing almost all the work.

### Why frequencies work

Natural frequencies are easier than probabilities because they keep the denominator visible. A probability is a ratio with the denominator hidden; a frequency is a count out of a population. The same information, presented as counts, is understood by far more people, including clinicians.

Teach the frequency method first and the formula second. The formula is a compression of the count, and compressing it before the count exists is how the base rate disappears.

### Bayes in odds form

For those who want the formula, give the odds form, which is easier to use and harder to misremember.

```
posterior odds = prior odds × likelihood ratio
```

With a prior of 1:999 and a likelihood ratio of 0.99/0.05 ≈ 20, the posterior odds are about 20:999, or 1:50, which is 2 per cent. The arithmetic is done in one line, and the prior is visibly a term, not a decoration.

### Calibration

Distinguish confidence from accuracy. A forecaster is calibrated if, among the events they assign 70 per cent, about 70 per cent occur. Most people are overconfident on hard questions and underconfident on easy ones.

Give the class five trivia questions with confidence ratings, then reveal the answers. Most will be right on the ones they were sure about and wrong on a few they were confident about. The lesson is not "you are bad at trivia"; it is that confidence is a feeling, and calibration is a measurement.

**The professional point.** The same distinction applies to a model's confidence score. A score of 0.9 is a claim about frequency, not a feeling of certainty, and it is only meaningful if it has been calibrated on data like yours.

## Strand B notes

### Lists are terms

```prolog
[a, b, c] = [a | [b, c]] = '.'(a, '.'(b, '.'(c, [])))
```

Three notations, one term. Ask the class to write the last one. The list is a recursive compound term with two constructors: the cons cell and the empty list.

### append

```prolog
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).
```

Run it in four modes.

```prolog
?- append([1,2], [3], X).
?- append(X, [3], [1,2,3]).
?- append(X, Y, [1,2]).
?- append(X, X, [1,2,3]).
```

The third enumerates splits. The fourth fails, and the failure is informative: no list is its own concatenation with a non-empty other part, for a finite list. Ask why the program can tell.

### member and the cost of ambiguity

```prolog
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).
```

`?- member(a, [a,b,a]).` succeeds twice if you ask for more. That is correct: there are two positions. Ask whether the predicate means "is a member" or "where is a member". It means both, depending on the mode, and that is the relational reading.

### Accumulators and difference lists

Show the accumulator sum, then mention difference lists as the technique that makes appending constant-time.

```prolog
sum(L, S) :- sum(L, 0, S).
sum([], A, A).
sum([H|T], A0, S) :- A1 is A0 + H, sum(T, A1, S).
```

Do not teach difference lists fully; they appear in the DCG week. One sentence of foreshadowing is enough.

### The list library

Show `length/2`, `nth0/3`, `nth1/3`, `last/2`, `reverse/2`, `msort/2`, `sort/4`. Warn that the library is not a substitute for knowing the recursion; the exam asks for definitions.

## Lab: the screening test and the list library

Part 1. Three screening problems with different base rates. Compute with frequencies, then with odds, and check that the two agree. One problem has a base rate of 1 in 2; another 1 in 100,000. The contrast is the lesson.

Part 2. Implement `append/3`, `member/2`, `length/2` and `reverse/2` without using the library. Then test each in at least two modes. For each, write one sentence on which mode is the intended one and what happens in the others.

Part 3. Write `delete_all/3` and test it with a variable in the element position. Explain the non-termination in one sentence.

## Homework

Find one claim in the news that reports a relative risk without a base rate. Write the base rate that would be needed to interpret it, and say where you would find it.

## Common errors

- Reporting a positive predictive value without the prevalence.
- Confusing `p(positive | condition)` with `p(condition | positive)`.
- Believing a calibrated model is accurate. Calibration is about the scores, not the decisions.
- Writing `append([H|T], L, [H|R])` without the recursive call.
- Testing a list predicate in one mode only.

# 11. Week 9 — Risk, uncertainty and the argument audit; grammars, cut and negation

## At a glance

| Strand | Content |
|---|---|
| Strand A | Expected value, risk, regression to the mean, the conjunction fallacy |
| Strand B | DCGs; cut; negation as failure |
| Lab | Parse a sentence; then break the parser with left recursion |
| Assessed | Argument audit due (20%) |

## Outcomes

By the end of the session, the student can:

- compute an expected value and explain what it hides;
- recognise regression to the mean and the conjunction fallacy in a report;
- write a DCG for a small fragment of English;
- explain what the cut commits you to and what negation as failure actually computes.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–55 | Strand A | Expected value; risk; regression; conjunction |
| 55–70 | Break | — |
| 70–135 | Strand B | DCGs; cut; negation as failure |
| 135–170 | Lab | Parser and commitment |
| 170–180 | Close | Audit submission and one warning |

## Strand A notes

### Expected value and what it hides

Expected value is the probability-weighted sum of outcomes. It is a useful summary and a dangerous one. A lottery with a positive expected value can still be a bad decision if the variance ruins you; a bridge with a negative expected value can still be worth building if it prevents a catastrophe.

Give the St Petersburg-style example in a modern form: a project with a 90 per cent chance of losing 1 and a 10 per cent chance of gaining 20 has an expected value of +1.1. Ask whether to fund it. The answer depends on the size of the budget relative to the loss and on how many such projects you can run. Expected value assumes you can average over repetitions; most decisions cannot be repeated.

### Risk

Risk is not probability. It is probability times consequence, considered against what you can bear. Two events with the same probability are different risks if one is recoverable and the other is not.

Introduce the distinction between risk and uncertainty: risk is quantifiable, uncertainty is not. Most software decisions are made under uncertainty and discussed as if they were risk. The vocabulary matters because it changes what evidence would help.

### Regression to the mean

Extreme measurements tend to be followed by less extreme ones, without any causal mechanism. A team that has its worst quarter is likely to improve; a team that has its best is likely to decline. Both are partly regression, and both are routinely attributed to the intervention that followed.

Ask the class: a company introduces a new process after its worst quarter and improves. What can we conclude? Almost nothing, unless we compare with what would have happened. This is the base-rate lesson in time.

### The conjunction fallacy

> Linda is 31, outspoken and very bright. She majored in philosophy. As a student she was deeply concerned with discrimination and social justice. Which is more probable: that Linda is a bank teller, or that Linda is a bank teller and active in the feminist movement?

Most people choose the second. It cannot be more probable: a conjunction cannot exceed its conjuncts. The story makes the conjunction more *representative*, and representativeness is not probability.

The professional version: a detailed failure narrative with many specific causes feels more likely than the simple one. It is not. Detail is a cost, not a bonus.

## Strand B notes

### DCGs

A definite clause grammar is a notation for difference lists. Write the fragment.

```prolog
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb, noun_phrase.
determiner --> [the].
determiner --> [a].
noun --> [cat].
noun --> [mat].
verb --> [sat_on].
```

Query `?- sentence([the, cat, sat_on, the, mat], []).` and it succeeds. Ask what the two arguments are. They are the input list and what remains; the grammar is a relation between a list and its remainder.

Then show the expansion, so the notation is not magic.

```prolog
sentence(S0, S) :- noun_phrase(S0, S1), verb_phrase(S1, S).
```

### The famous failure

Add a rule with left recursion.

```prolog
np --> np, pp.
```

Ask what happens. It loops, because the first thing it does is call itself on the same input. The declarative reading is fine; the operational one diverges. This is the same lesson as week 4, now in a notation where it is easy to write by accident.

Then show the fix: left-corner transformation, or tabling, or a different grammar formalism. One sentence each; the point is that the failure is structural, not a bug in Prolog.

### The cut

Give a program that produces a wrong second answer.

```prolog
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.
```

Run `?- max(3, 3, M).` It gives `M = 3` twice if you ask for more. Ask whether that is wrong. It is not wrong, but it is redundant, and in a larger program the redundancy becomes a bug.

Now add the cut.

```prolog
max(X, Y, X) :- X >= Y, !.
max(X, Y, Y).
```

Explain exactly what it does: it commits to the choices made since entering the predicate. It does not mean "if"; it does not mean "stop"; it prunes the choice points. Then show the cost: the declarative reading is lost, and the predicate now depends on clause order for correctness.

**The rule to state.** A cut is a promise that no other clause could have applied. If you cannot justify that promise, you have written a program whose meaning depends on the order of the text.

### Negation as failure

```prolog
not_raining :- \+ rain.
```

Ask what `\+` does. It attempts the goal; if the goal fails, it succeeds. It does not establish the negation; it establishes that the goal could not be proved.

Demonstrate the difference.

```prolog
?- \+ rain.
true.
?- \+ \+ rain.
false.
```

And the classic unsoundness:

```prolog
?- \+ (X = 1, X = 2).
true.
?- X = 1, X = 2.
false.
```

The first succeeds because the conjunction fails; but it is not the case that there is no X satisfying both — it is that no X does. The scope matters.

The professional point: `\+` implements "not provable", which is not "false". In a closed world they coincide; in an open one they do not. This is the single most consequential semantic decision in Prolog, and it is the one students most often mistake for negation.

## Lab: parser and commitment

Part 1. Extend the grammar to handle a small vocabulary with two sentence types and one prepositional phrase. Test it in both directions: parse a list, and generate a sentence from an unbound list. The second will surprise them.

Part 2. Add left recursion and observe the loop. Then apply one fix and verify it terminates.

Part 3. Write `max/3` with and without cut, and a client predicate that exposes the difference. Then write `\+` into a rule and find the case where it gives the wrong answer about the world.

## Homework

Finish the argument audit. In it, state explicitly which of your premises are stipulated and which are evidenced, and what would change your verdict.

## Common errors

- Writing a DCG and forgetting the two arguments when calling it directly.
- Believing the cut makes a predicate more efficient in a way that is free.
- Reading `\+` as classical negation.
- Using `\+` on an unbound variable and expecting an answer about the world.
- Confusing regression to the mean with a causal effect.

# 12. Week 10 — Fallacies as questions; collecting answers with findall and constraints

## At a glance

| Strand | Content |
|---|---|
| Strand A | The fallacy taxonomy as a question hierarchy; transposition |
| Strand B | `findall/3`, `bagof/3`, `setof/3`; CLP(FD) introduced |
| Lab | Transpose an argument; solve a puzzle by constraints |
| Assessed | Portfolio 6: a transposition and a constraint model |

## Outcomes

By the end of the session, the student can:

- use the generic detector before naming any fallacy;
- transpose an argument and say what survives;
- explain the difference between `findall`, `bagof` and `setof`;
- model a small combinatorial problem in CLP(FD) and explain propagation versus search.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions on weeks 8–9 |
| 10–55 | Strand A | The question hierarchy; transposition |
| 55–70 | Break | — |
| 70–135 | Strand B | findall family; CLP(FD) first model |
| 135–170 | Lab | Transposition and SEND+MORE |
| 170–180 | Close | One transposition read aloud |

## Strand A notes

### Questions before names

The taxonomy is useful only after the questions. Teach the questions in tiers, and let the names attach to them.

| Tier | Question | Names that attach |
|---|---|---|
| 0 | Does that actually get you there? | non sequitur |
| 1 | Is that about the claim, or about the person or the feeling? | ad hominem, appeal to authority, appeal to emotion, bandwagon, tu quoque |
| 2 | Are there other options? How many cases? Is the premise the conclusion again? | false dilemma, hasty generalisation, circularity, straw man |
| 3 | What is the quantifier, the comparison, the base rate? | composition, division, equivocation, loaded question, post hoc, cum hoc, base rate, conjunction, survivorship |
| 4 | Who benefits if I believe this? | manipulation, framing, scapegoating |

Tier 0 is the whole method. The rest are search hints: when the generic detector fires, the tiers tell you where to look.

### Implicature as a question

Tier 3 includes the quantifier, the comparison and the base rate. Grice's implicature belongs there too, because it is a question about what the words leave open.

A speaker says *some* and implicates *not all*. A headline says *crime doubles* and implicates a comparison it does not state. A vendor says *probably the best* and implicates *the best* while keeping the legal shield. In each case the surface is true and the inference is doing the work.

The classroom move is a three-column table: **said**, **meant**, **cancelled**. The third column is the discipline. If the speaker can cancel the inference without contradiction, it was an implicature, not an entailment. If she cannot, it was part of the claim.

This is also the audit for a machine answer. A language model produces cooperative-sounding text: relevant, informative, clear, confident. It has no access and no interest. The question is not whether the answer sounds helpful. It is what the speaker would have to know, and how she would know it.

### Transposition

Transposition is the test of form. Replace the content-carrying terms with placeholders, preserve the structure, and see whether the argument still persuades. If it does, the persuasion was never about the content.

Work one example in full.

> We should not listen to her argument about the budget; she has never run a department.

Transposed:

> We should not accept X's claim about Y; X has not done Z.

Ask whether the transposed version persuades. It does not. The original's force came from the person, not the claim. Name it: ad hominem. The name arrives last, as a label for something already diagnosed.

Then the reverse exercise, which is harder and more valuable. Take a *good* argument and transpose it. It should still persuade, because its force is in the form and the evidence. If it does not, something was doing the work that should not have been.

### The failure mode of this week

The failure mode is the fallacy-of-the-week syllabus: students learn twenty names and use them as conversation-enders. Guard against it with the marking. An answer that names a fallacy without asking the question scores zero on that item; an answer that asks the question and never names anything scores full marks.

## Strand B notes

### The findall family

```prolog
?- findall(X, parent(X, _), L).
L = [alice, bob, carol].

?- findall(X-Y, parent(X, Y), L).
L = [alice-bob, bob-carol, carol-dave].
```

`findall/3` collects every solution, in order, with no duplicates, and fails only if the goal is malformed. `bagof/3` groups by free variables and fails if there are no solutions. `setof/3` sorts and removes duplicates.

```prolog
?- bagof(C, parent(P, C), L).
P = alice, L = [bob] ;
P = bob, L = [carol] ;
...
?- setof(C, parent(P, C), L).
```

Ask why `bagof` backtracks over `P` while `findall` does not. The free variable is existentially quantified in `findall` and grouped in `bagof`. This is the quantifier lesson from week 3, now with a concrete difference in behaviour.

### The warning

Collecting all solutions presupposes that the search terminates and that all solutions are found. With an infinite branch, `findall` loops. With a cut, it may miss solutions. The collector does not make the search complete; it reports what the search produced.

> `findall` is a claim that the search space is finite and fully explored. Make that claim deliberately.

### CLP(FD): the first model

```prolog
:- use_module(library(clpfd)).

puzzle([A, B, C]) :-
    Vars = [A, B, C],
    Vars ins 0..9,
    A #> 0,
    A + B #= C,
    label(Vars).
```

Run it and ask what `label/1` did. Without it, the constraints are posted and the answer is a set of domains, not a solution. With it, the search enumerates.

Then show propagation. Add `A #= 3` and query without `label`; the domains shrink. This is the distinction the week is built on: **propagation reasons, labelling enumerates.** A constraint solver is a reasoning engine with a search engine attached, and confusing the two is the most common modelling error.

### SEND + MORE = MONEY

Give the classic. Build it together, with these decisions made explicit:

- the domain is 0..9 for each letter;
- the leading letters are non-zero;
- all letters are distinct (`all_different/1`);
- the column arithmetic is a single equation;
- labelling is separate from modelling.

```prolog
send_more_money([S,E,N,D,M,O,R,Y]) :-
    Vars = [S,E,N,D,M,O,R,Y],
    Vars ins 0..9,
    S #> 0, M #> 0,
    all_different(Vars),
    1000*S + 100*E + 10*N + D
  + 1000*M + 100*O + 10*R + E
  #= 10000*M + 1000*O + 100*N + 10*E + Y,
    label(Vars).
```

Ask how many solutions. One. Ask how long it takes with and without `all_different`. The difference is propagation, and it is visible in the time.

## Lab: transposition and constraints

Part 1. Each pair receives four arguments: two bad, two good. Transpose each, and report whether the transposed version persuades. For the good ones, explain why the form survives. For the bad ones, name the question that kills them, then the fallacy.

Part 2. Model a small scheduling problem: five tasks, three machines, two precedence constraints, one task that cannot start before another. Post the constraints, solve, and then explain in writing which part of the program was reasoning and which was enumeration.

Part 3. Run SEND+MORE with and without `all_different`, timing both. Write one sentence on what the constraint bought.

## Homework

Take a claim from a field you know and write its best version, then attack it. The attack must use a question, not a name. Bring both.

## Common errors

- Naming a fallacy before asking the question.
- Transposing by replacing words rather than structure.
- Believing `findall` sorts or removes duplicates. It does neither.
- Using `bagof` and being surprised by the backtracking over free variables.
- Calling `label` before posting all constraints.
- Believing propagation alone has solved the problem.

# 13. Week 11 — Manipulation and its refusal; constraints at work

## At a glance

| Strand | Content |
|---|---|
| Strand A | The four-way distinction; manipulation techniques; prebunking; lateral reading |
| Strand B | Labelling strategies; optimisation; scheduling model |
| Lab | Build a manipulation; optimise a timetable |
| Assessed | Lab practical (20%) in the second half |

## Outcomes

By the end of the session, the student can:

- classify a piece of speech as mistake, disagreement, bullshit, trolling or manipulation;
- build a manipulation and explain which one they would fall for;
- choose a labelling strategy and justify it;
- use `min/2` or `max/2` inside a constraint model and explain what is optimised.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–55 | Strand A | Four-way distinction; techniques; refusal |
| 55–70 | Break | — |
| 70–110 | Strand B | Labelling; optimisation; a scheduling model |
| 110–170 | Lab practical | Two-hour unseen task, starts here and continues |
| 170–180 | Close | Practical instructions |

The lab practical replaces the lab and runs into the following week's first hour if the timetable allows. The version printed here assumes a single 60-minute block; adjust to your calendar.

## Strand A notes

### The four-way distinction

Not every bad utterance is a lie. Distinguish:

| Kind | The speaker's relation to the claim | The right response |
|---|---|---|
| Mistake | Believes it, has it wrong | Correct the belief |
| Disagreement | Believes it, values differ | Argue the values |
| Bullshit | Does not care whether it is true | Ask for the chain; refuse the frame |
| Trolling | Wants a reaction, not belief | Do not feed it |
| Manipulation | Wants a behaviour, uses the claim as a means | Name the technique; refuse the frame |

The distinctions matter because the responses differ. Correcting a troll is a gift. Arguing values with a mistake is a category error. Asking a manipulator for evidence is often exactly what they want, because it keeps you in their frame.

### The toolbox

Give the techniques as verbs, not as Latin names.

- **Decontextualise** — a real photo, a false caption.
- **Fabricate** — a quote in a real person's voice.
- **Impersonate** — an account that looks like an institution.
- **Polarise** — two posts designed to make each side furious.
- **Scapegoat** — one group as the explanation for a complex failure.
- **Flood** — bury one true claim under twenty trivial ones.
- **Emotion first** — make them feel before they think.

The order is roughly the order of cost to the manipulator. Decontextualising is cheap and effective; building a fake institution is expensive and rare. Teach the cheap ones hardest.

### Build one

The exercise that works is construction, not detection.

In groups, students take a real photograph and write a false caption; write a fake quote in a real person's style; design two posts to enrage opposite sides; bury a true claim. Then each group reports: which was easiest, which was most convincing, and which one would you fall for?

The confession is the learning. A student who says "I would fall for the flood, because I skim" has learned more than one who can recite seven techniques.

### Refusal

Give four portable counter-moves and rehearse them aloud.

1. **Stop.** Do not share on first contact.
2. **Source.** Who made this, and what are they selling?
3. **Corroborate.** Does an independent source have it?
4. **Trace.** Follow the claim to its original, not to its loudest repetition.

Then the two that are harder: **name the technique** (only with someone who will hear it), and **refuse the frame** (answer a different question than the one asked).

## Strand B notes

### Labelling

`label/1` enumerates. `labeling/2` takes options.

```prolog
labeling([ff], Vars).          % first fail: smallest domain first
labeling([min(Goal)], Vars).   % minimise
labeling([max(Goal)], Vars).   % maximise
labeling([leftmost], Vars).    % default order
```

Ask which is fastest and why. First-fail is usually fastest because it fails early and prunes. But "usually" is doing work: on some models, leftmost is better. The honest answer is to measure.

### Optimisation

```prolog
schedule(Tasks, Makespan) :-
    ...
    Makespan #>= End1,
    Makespan #>= End2,
    labeling([min(Makespan)], Vars).
```

Explain the branch-and-bound: the solver finds a solution, then adds a constraint that the objective must be strictly better, and repeats. The trace is not a single search but a sequence of searches with a tightening bound.

Ask what happens if the objective is not bounded below. The solver will keep improving until it can prove optimality or run out of time. There is no "good enough" unless you encode one.

### Propagation versus search, again

Add a redundant constraint and time the model. A redundant constraint does not change the solution set; it changes the propagation. This is one of the few places in the course where a change that is logically inert is computationally important, and it is worth ten minutes.

Give the example: in SEND+MORE, adding `S + M #= O + 10` (the carry into the thousands column) is redundant with the full equation and prunes much earlier.

## Lab practical

Two hours, unseen, individual. The task has four parts:

1. Read a small program and state what it does and what it does not know (10 marks).
2. Write a recursive predicate over a list or a term (10).
3. Trace a query and draw the tree, marking choice points (10).
4. Write a constraint model for a small puzzle and explain propagation versus search (10).

The rubric rewards the boundary statement in part 1 and the explanation in part 4 as heavily as the code. A student who writes perfect code and no explanation gets half marks.

## Homework

None. The practical is the week's work.

## Common errors

- Treating every bad argument as a lie.
- Building a manipulation and enjoying it without the debrief.
- Calling `labeling` before posting constraints.
- Optimising with an unbounded objective.
- Adding a redundant constraint and assuming it is harmless because it is logically inert. It is harmless logically and not computationally.

# 14. Week 12 — The AI audit; tabling and answer-set programming

## At a glance

| Strand | Content |
|---|---|
| Strand A | Derivation versus output; confidence versus calibration; responsibility |
| Strand B | Tabling; termination; ASP and s(CASP); stable models |
| Lab | Audit a machine answer; write a default rule |
| Assessed | Nothing new; project brief confirmed |

## Outcomes

By the end of the session, the student can:

- distinguish a derivation from an output and say why the distinction matters;
- test a system out of its scope and document the failure;
- use tabling to terminate a program that should not terminate;
- write a default rule in ASP and explain what a stable model is.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–50 | Strand A | The audit; calibration; responsibility |
| 50–65 | Break | — |
| 65–130 | Strand B | Tabling; ASP; s(CASP) |
| 130–170 | Lab | Audit and defaults |
| 170–180 | Close | Project brief |

## Strand A notes

### Derivation versus output

A derivation is a chain from premises to conclusion. An output is a string. The two are independent: a system can produce a correct output with no derivation, and a derivation can be valid with a false premise.

For a generative system, the output is usually a sample from a distribution conditioned on the prompt. There is no derivation in the logical sense, even when the output looks like one. The chain a system shows you, if it shows one, is generated text about a chain, not the chain.

Ask the class what would have to be true for an output to count as evidence. Answers will converge on: it must be checkable independently, and the check must be cheaper than the decision. That is the right criterion.

### The audit

Give a fixed procedure. An audit is not a vibe.

1. **Scope.** What was the system trained on, and what is out of scope? Write the boundary.
2. **Probe.** Ask something just outside the boundary and record the answer verbatim.
3. **Chain.** Ask for the derivation. Reconstruct it or refuse the claim.
4. **Calibration.** Ask the same question with two framings. Note whether the answer moves.
5. **Responsibility.** Who acts on the answer, and who bears the consequence?
6. **Verdict.** Use, use with check, or refuse. With a reason.

The audit is marked on the boundary statement and the verdict, not on the prose.

### The uncomfortable finding

Out-of-scope probes usually produce fluent confabulation, and the fluency is the problem. Students expect errors to look like errors. They do not. Show three examples where the wrong answer is better written than the right one.

Then the professional point: because errors are fluent, the only reliable defence is a check that does not depend on fluency. That check is the derivation, or an independent source, or a test. There is no fourth option.

## Strand B notes

### Tabling

Take the `path/2` program with a cycle.

```prolog
edge(a, b). edge(b, c). edge(c, a).
path(X, Y) :- edge(X, Y).
path(X, Y) :- path(X, Z), edge(Z, Y).
```

`?- path(a, c).` finds an answer, but `?- path(a, X), fail.` loops, and some queries never terminate. Add one line.

```prolog
:- table path/2.
```

Now the same queries terminate, because answers are memoised and repeated subgoals are resolved from the table rather than re-explored.

Ask what changed. Not the declarative reading; the same relation. The operational strategy changed from depth-first without memory to a form of memoised search. This is the fix promised in week 4.

The cost: tabling changes termination and complexity, and in some systems it changes the answer set for programs with negation. Say so, and say that "it just makes it faster" is false.

### ASP and stable models

Give a default.

```prolog
bird(tweety).
bird(penguin_pete).
penguin(penguin_pete).

flies(X) :- bird(X), not penguin(X).
```

Ask what `not` means here. It is default negation: `flies(X)` holds if X is a bird and there is no evidence that X is a penguin. The answer set contains the two bird facts, the penguin fact, and one flight: `flies(tweety)` holds; `flies(penguin_pete)` does not.

Now add `penguin(tweety).` and recompute. The answer set changes; `flies(tweety)` disappears. This is non-monotonicity: adding a fact removes a conclusion. Nothing in classical logic does that.

In s(CASP):

```prolog
flies(X) :- bird(X), not penguin(X).
```

The system produces a model and, crucially, a justification for each atom. Show the justification. It is the derivation made visible, which is why the tool belongs in this course.

### The warning

A stable model is one consistent reading, not the truth. If two stable models exist, the program does not tell you which is right; it tells you that the rules admit two readings. That is a modelling fact, not a defect, and it is the same lesson as the countermodel in week 3.

## Lab: audit and defaults

Part 1. Each student audits one machine answer using the six-step procedure. The answer must be one they actually received during the week. The deliverable is one page: scope, probe, chain, calibration, responsibility, verdict.

Part 2. Write a default theory in ASP with one exception and one conflicting default. Compute the stable models by hand, then with s(CASP). Explain the difference in one paragraph.

Part 3. Take the tabled `path/2` and remove the tabling. Find a query that terminates with tabling and does not without it. Write the query and the reason.

## Homework

Complete the audit page. Bring it to the project workshop; it is the model for the boundary note.

## Common errors

- Treating a fluent answer as evidence.
- Auditing the system's tone rather than its scope.
- Believing tabling changes only the speed.
- Reading `not` in ASP as classical negation.
- Assuming a unique stable model when there are two.
- Writing a boundary note that says "the model may be wrong" with no specifics.

# 15. Week 13 — Project workshop; declarative debugging

## At a glance

| Strand | Content |
|---|---|
| Strand A | Judgement under uncertainty; the four questions applied |
| Strand B | Declarative debugging; tracing strategy; minimising a failing case |
| Lab | Debug a deliberately broken program |
| Assessed | Project draft reviewed in studio |

## Outcomes

By the end of the session, the student can:

- apply the four questions to their own project;
- locate a bug by asking which belief is wrong, not which line to change;
- minimise a failing query;
- write a boundary note that names specific failures.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–40 | Strand A | Judgement; the four questions; the boundary note |
| 40–55 | Break | — |
| 55–115 | Strand B | Declarative debugging; trace; minimisation |
| 115–170 | Studio | Project draft review in pairs |
| 170–180 | Close | Defence schedule |

## Strand A notes

### Judgement, not verdict

The project asks for a judgement: this program is adequate for this purpose, with these limits. A judgement is not a verdict. It is a claim with a scope, a standard and a boundary.

Give the template.

> This program is adequate for [purpose] because [evidence]. It is not adequate for [other purpose] because [specific failure]. The boundary is [where], and it would be crossed if [condition].

Every clause is checkable. "It works" is not a judgement; it is an advertisement.

### The four questions

Apply them to a project the class has seen: the family program.

| Question | Answer |
|---|---|
| What does it know? | The parent facts supplied |
| What does it not know? | Anyone not in the facts; adoption; step-relations |
| Why this answer? | The derivation, clause by clause |
| What would change it? | A new fact, or a rule for a relation it does not model |

Then ask them to answer the same four for their own project, in writing, in ten minutes. Most will find question 2 hard. That is the point of the week.

### The boundary note

The boundary note is one page, with four headings: scope, known failures, assumptions, and what would change the verdict. It is not a disclaimer. A disclaimer protects the author; a boundary note informs the reader.

Give a bad example and a good one.

> Bad: "This program may not be correct in all cases."

> Good: "This program assumes a static family: no births, deaths or adoptions after the facts are loaded. If a birth is added, `ancestor/2` remains correct but `sibling/2` can become wrong, because it is defined by shared parent and does not check for half-siblings. Adding a half-sibling fact makes `sibling(a, b)` true when it should be false."

The second is specific, testable and useful. It is also the kind of thing that gets a student hired.

## Strand B notes

### Declarative debugging

The question is not "which line is wrong" but "which belief is wrong". A program is a set of beliefs; an unexpected answer is evidence that at least one is false.

Procedure:

1. Write the query that gives the wrong answer.
2. Ask whether the answer is wrong, or the expectation is wrong. (Half the time it is the expectation.)
3. Find the smallest subgoal whose answer is wrong.
4. Ask which clause produced it.
5. Ask whether the clause is wrong in itself or wrong in context.

Show it on a broken program.

```prolog
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- ancestor(X, Z), parent(Z, Y).
```

Ask for `?- ancestor(a, d).` with a cycle. It loops. Is the belief wrong, or the search? The belief is right; the search strategy is wrong. The fix is tabling or reordering. That distinction — wrong belief versus wrong search — is the core of declarative debugging.

### Minimising

Give a failing query with twelve facts. Remove facts one at a time until the failure disappears, then restore the last one. The result is a minimal failing case, and it is usually three lines.

Teach the discipline: never debug a large case. Shrink first. The shrink is the explanation.

### Trace and spy

```prolog
?- trace.
?- spy(parent/2).
```

Show `trace` once, slowly, and then say the truth: trace output is useful for small programs and unusable for large ones. The skill is to shrink until trace is readable.

## Studio

Pairs exchange projects. Each pair must answer the four questions for the other's program, in writing, without looking at the author's answers. Then they compare. The gaps are the boundary note.

The reviewer's job is to find one thing the program does not know. If they cannot, the program is either trivial or the author has hidden the boundary.

## Homework

Revise the boundary note using the reviewer's findings. Prepare a ten-minute defence: three minutes of demonstration, four minutes of boundary, three minutes of questions.

## Common errors

- Debugging by staring.
- Changing a line before identifying the wrong belief.
- Writing a boundary note that names no specific failure.
- Defending the program instead of describing it.
- Confusing "I could not find a bug" with "there is no bug".

# 16. Week 14 — Defence; the course in one page

## At a glance

| Strand | Content |
|---|---|
| Strand A | The obligation, restated; what the course established |
| Strand B | Semantics summary; soundness and completeness of SLD |
| Lab | Defences, in parallel rooms |
| Assessed | Project defence (20%); portfolio closes |

## Outcomes

By the end of the session, the student can:

- defend a program's boundary under questioning;
- state the soundness and completeness results for SLD resolution and their limits;
- explain the difference between a program that is correct and a program that is adequate;
- name the one question they will carry out of the course.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–20 | Strand A | The obligation, restated |
| 20–40 | Strand B | SLD soundness and completeness; what they exclude |
| 40–50 | Break | — |
| 50–170 | Defences | Three rooms, four students each, fifteen minutes each |
| 170–180 | Close | One question each |

## Strand A notes

### The obligation, restated

Return to week 1.

> Anyone who asserts that a system is correct owes two things: the chain that supports the claim, and a statement of the conditions under which the chain would fail.

Ask the class what has changed in fourteen weeks. The obligation has not. What has changed is that they can now discharge it: they can build the chain, draw it, test it, and name its edge.

The professional point: this is the obligation that separates an engineer from a tool operator, and it is the one that is most often waived under deadline. The course cannot make anyone keep it. It can make the waiver visible.

### Correct and adequate

A program is correct relative to a specification. A program is adequate relative to a purpose. The two are different, and the second is what practice needs.

A correct program can be inadequate because the specification was wrong. An adequate program can be incorrect because the purpose tolerates the error. Say both, and give an example of each. Then ask which one they would rather ship. The answer is "it depends on the purpose", and the ability to say why is the outcome of the course.

## Strand B notes

### SLD soundness and completeness

State the results plainly.

- **Soundness:** every answer computed by SLD resolution is a logical consequence of the program. If the program is a set of definite clauses, an answer is correct.
- **Completeness:** for definite clauses, if a goal is a logical consequence, SLD resolution can find it — given a fair search rule. Prolog's depth-first search is not fair, so Prolog is sound but not complete.

This is the cleanest statement in the course, and it is worth writing on the board and leaving there.

The caveats:

- the results are for definite clauses; add negation and they need qualification;
- soundness is relative to the program, not to the world;
- completeness assumes fairness, which Prolog does not provide;
- the occurs check affects the result.

Each caveat is a week of the course. The exam asks for the statement and one caveat.

### The one-page summary

Give them this table on the last slide.

| Feature | What it buys | What it costs |
|---|---|---|
| Unification | pattern matching as solving | bidirectional cost, occurs check |
| Backtracking | completeness over choices | non-termination, order dependence |
| Cut | pruning, commitment | declarative reading lost |
| Negation as failure | defaults | not classical negation |
| findall | collection | assumes termination and exhaustiveness |
| CLP(FD) | propagation | not search; a fixpoint is not an answer |
| Tabling | termination | semantics change, not just speed |
| ASP | defaults, stable models | multiple models are not the truth |

If they remember one table from the course, this is the one.

## Defences

Fifteen minutes per student: five minutes of demonstration, five of boundary, five of questions. Three questions are mandatory:

1. What does your program know that you did not tell it?
2. Where is it wrong about the world?
3. What would you have to add to make it right, and why have you not?

The third is the one that separates the students who understand from the students who have a working program.

## Close

Each student writes one question on a card and leaves it at the door. The questions are typed up and sent to the class the following week. The best one is read at the start of the next cohort's first session.

<!-- part: Part III — Assessment and projects -->

# 17. The portfolio

Seven production tasks, one per fortnight. Each is marked out of 100 and converted to the 40 per cent component. Each entry has the same cover sheet: what I made, what it establishes, what it does not establish, what I would do next.

| # | Week | Task | Length | What it must contain |
|---|---|---|---|---|
| 1 | 2 | Argument in standard form, with a rule base | 600 words + code | Claim, grounds, warrant, qualifier, rebuttal; the warrant as a predicate that fails |
| 2 | 4 | A proof and a countermodel for the same sentence | 400 words | The proof, the countermodel, and a sentence on what the pair establishes |
| 3 | 5 | A specification with an omission | 500 words | The specification, the wrong program it admits, the repaired version |
| 4 | 6 | A diagnosis and a recursive program | 500 words + code | Three candidate explanations, the discriminator, a recursive predicate with a marked floor |
| 5 | 8 | A base-rate analysis of a real claim | 600 words | The claim, the base rate, the frequencies, the corrected reading |
| 6 | 10 | A transposition and a constraint model | 500 words + code | The transposition, the verdict, a constraint model, propagation versus search |
| 7 | 12 | A machine-answer audit | 700 words | Scope, probe, chain, calibration, responsibility, verdict |

## Marking the portfolio

| Criterion | Weight | What earns full marks |
|---|---|---|
| Correctness of the artefact | 30 | The proof is valid, the program runs, the arithmetic is right |
| The boundary statement | 30 | A specific, testable statement of what the artefact does not establish |
| The reasoning | 25 | The steps are shown, not asserted; the warrant is explicit |
| The writing | 15 | Plain, specific, no filler |

An entry that is technically perfect and has no boundary statement cannot exceed 70. This is deliberate and is stated in the first week.

# 18. The project

## Brief

Build a working logic program in a domain you know, with a written boundary note and a public defence.

The domain must be small enough to finish in four weeks and rich enough to have a boundary. Good domains from previous cohorts:

- a course-prerequisite adviser with rules for waivers;
- a family-relations program with step- and half-relations;
- a small grammar for a controlled language, with a parser and a generator;
- a scheduling model for a lab's equipment;
- a policy checker for a scholarship scheme;
- a diagnosis assistant for a printer's error codes;
- a game-playing program with an explicit search bound.

Bad domains: anything that needs a database, anything that needs a GUI, anything whose rules you would have to invent on the last night.

## Deliverables

| Item | Length | Weight within the project |
|---|---|---|
| The program | 150–400 lines, commented | 40 |
| The boundary note | one page, four headings | 30 |
| The defence | 15 minutes, three mandatory questions | 30 |

## The boundary note

Four headings, in this order.

**Scope.** What the program models, and for what purpose. One paragraph.

**Known failures.** Specific inputs or situations where it gives a wrong or misleading answer. At least three, each with the input and the wrong output.

**Assumptions.** What must be true of the world for the program to be usable. Distinguish facts you supplied from facts you assumed.

**What would change the verdict.** The observation or requirement that would make the program inadequate even within its scope.

A boundary note with no specific failures is returned unmarked. This is not a formality; the specific failures are the assessment.

## Rubric

| Criterion | Weight | 0–40 | 40–70 | 70–100 |
|---|---|---|---|---|
| Program | 40 | Runs on the examples only | Runs generally; some clauses redundant | Clear, recursive where needed, well-factored, documented |
| Boundary note | 30 | Generic disclaimer | Names failures but not mechanisms | Specific failures, mechanisms, and conditions |
| Defence | 30 | Reads the note | Answers the three questions | Answers questions not anticipated, and concedes limits |

## Defence questions

The three mandatory questions are given in week 14. The examiner may add two from this list.

- Which clause would you delete first if you had to simplify, and what would you lose?
- Where does your program rely on the closed world?
- Which of your predicates is not in its intended mode, and what happens when it is run backwards?
- What is the smallest input that makes your program wrong?
- If the domain changed in one way, which rule would break first?
- Why did you not use a constraint solver here?
- What would a reviewer who disagrees with your scope say, and what is your answer?

# 19. The examination

## Format

Three hours, closed book, four questions from six. Calculators permitted. No machine.

| Question | Topic | Marks |
|---|---|---|
| 1 | Validity, countermodels, and what a proof does not give | 25 |
| 2 | Unification and SLD, by hand | 25 |
| 3 | Recursion and termination | 25 |
| 4 | Lists, grammars or constraints (one of three) | 25 |
| 5 | Cut, negation as failure, tabling: semantic consequences | 25 |
| 6 | Audit an argument or a machine answer | 25 |

Questions 1 and 6 are compulsory in spirit: the paper is designed so that a student who avoids both cannot reach a pass.

## Sample question and model answer

**Question.** Consider the program:

```prolog
p(a).
p(b).
q(X) :- p(X), \+ r(X).
r(b).
```

(a) What are the answers to `?- q(X).`? (5)
(b) Explain why `q(a)` is derivable and `q(b)` is not. (5)
(c) Add a fact `r(c).` and say what changes. (5)
(d) Is `\+` here classical negation? Justify your answer with reference to this program. (10)

**Model answer.**

(a) `X = a`. The query has one answer.

(b) `q(a)` succeeds because `p(a)` succeeds and `\+ r(a)` succeeds: `r(a)` is not in the program. `q(b)` fails because `r(b)` is in the program, so `\+ r(b)` fails. The derivability of `q(a)` depends on the absence of a fact, not on a negative fact.

(c) Nothing changes for `q/1`, because no clause has head `r(c)` and `q/1` only tests `r/1` on values that are `p/1`. The added fact is inert here. If the program had a rule with a variable ranging over a larger domain, it could matter.

(d) No. `\+ r(a)` succeeds because `r(a)` cannot be proved, not because `r(a)` is false. If a fact `r(a)` were added, `q(a)` would stop being derivable; classical negation would not change its truth value on the addition of an unrelated fact in this way. `\+` implements negation as failure: it is a statement about the program, not about the world. The program is sound with respect to its own completion, and that completion is an assumption.

The mark scheme gives 4 for (d) for identifying negation as failure, 3 for the distinction between "not provable" and "false", and 3 for connecting it to the closed-world assumption with an example.

# 20. Lab sheets

Each lab sheet has four parts: predict, run, explain, break. The sheet is collected, marked formatively, and returned at the start of the next session.

## Template

```
Lab N — [title]
Names: ______________________  Date: __________

1. PREDICT
   For each query, write the answer and the reason before running it.
   Query: ______________________
   Predicted: __________________  Reason: ____________________

2. RUN
   Actual: _____________________  Right/Wrong: _______________

3. EXPLAIN
   Why did the prediction differ (or not)?
   _________________________________________________________

4. BREAK
   Change one fact or clause. What breaks, and why?
   _________________________________________________________
```

The "break" section is worth half the marks. A pair that runs everything correctly and breaks nothing has done the easy half.

## Lab 1, worked example

| Field | Content |
|---|---|
| Program | The family program from week 1, plus `sibling/2` defined as shared parent |
| Query 1 | `?- sibling(bob, carol).` |
| Prediction | true, because they share a parent |
| Run | true |
| Explain | `sibling/2` is defined by shared parent; no other condition |
| Break | Add `parent(alice, dave).` and `parent(zed, dave).` Then `sibling(bob, dave)` is true, although they are half-siblings. The definition is too weak. |
| Mark | 8/10: the break was found, the explanation of *why* the definition is too weak was thin |

# 21. Three scripted sessions

These are transcripts of the moves, not of the words. They exist so that a new teacher can see the shape of a session before adapting it.

## Script 1: Week 1, first 60 minutes

| Time | Move | What the teacher does | What the students do |
|---|---|---|---|
| 0–3 | Silence | Writes two questions on the board: "What do you know?" "How do you know it?" Says nothing else | Read, sit, wonder |
| 3–8 | Elicit | Asks three students for something they know and how they know it | Answer; discover that "I read it" is a source, not a proof |
| 8–15 | The regress | Writes the encrypted-files argument; asks whether the conclusion follows and whether it is true | Separate form from truth; the room divides |
| 15–22 | Name it | Writes the two slogans; defines validity and truth as different standards | Copy the slogans |
| 22–32 | Four sources | Gives the table; asks for an example of each from their own week | Supply examples; argue about testimony |
| 32–40 | The obligation | States the obligation; asks who has said "it works on my machine" | Most hands go up; laughter |
| 40–50 | Pairs | Finds one claim in the room; writes what must be true and how to know | Work in pairs; some choose the course description, which is fair |
| 50–60 | Close | Three pairs report; one sentence each | Report; the sentences are usually better than the essays |

The teacher's discipline in this hour is to resist defining validity formally. The formal definition arrives in week 3, after the experience. If a student asks for it, the answer is: "We will get there. For now, tell me whether the conclusion follows if the premises are true."

## Script 2: A lab session, 40 minutes

| Time | Move | What the teacher does |
|---|---|---|
| 0–3 | Frame | "You will be wrong. Write the prediction anyway. The prediction is the work." |
| 3–10 | Predict | Walks the room, reads predictions, says nothing about correctness |
| 10–20 | Run | Pairs run; the teacher watches faces, not screens |
| 20–28 | Explain | Asks two pairs with different predictions to explain; does not resolve |
| 28–35 | Break | "Change one thing. What breaks?" The teacher offers one hint per pair, maximum |
| 35–40 | Collect | One sentence per pair: what broke, and what that tells you about the program |

The teacher's discipline is not to answer "is this right?" during the predict phase. The prediction is diagnostic; correcting it early destroys the diagnosis.

## Script 3: A defence, 15 minutes

| Time | Move | What the teacher does |
|---|---|---|
| 0–1 | Frame | "Five minutes to show, five to bound, five to questions. I will interrupt." |
| 1–6 | Show | Watches the demonstration; notes one thing that is not shown |
| 6–11 | Bound | Asks: "What does it not know?" The student answers from the note or from memory |
| 11–14 | Questions | The three mandatory questions, in order, then one unanticipated |
| 14–15 | Close | "One thing you would do with another week." Thanks. No verdict in the room |

The examiner's discipline is to ask the third question — "what would you add, and why have you not?" — even when the defence is going well. It is the question that reveals whether the student understands the boundary or has merely documented it.

<!-- part: Part IV — Appendices -->

# ^ Appendix A — Diagnostic quiz

Ten questions, fifteen minutes, first session. Not marked; used to pitch the course.

1. If all A are B and all B are C, are all A C?
2. If all A are B and all B are C, are all C A?
3. A test is 99 per cent sensitive and 95 per cent specific. Prevalence is 1 in 1,000. Roughly what is the chance that a positive result is a true positive?
4. What does `false` mean in Prolog?
5. What is the difference between `X = 1+2` and `X is 1+2`?
6. If a rule has no base case, what happens, and why?
7. Is `\+ p` the same as "p is false"? Explain.
8. What is the difference between a valid argument and a true conclusion?
9. Give one example of a correlation that is not a cause.
10. When would you trust a machine's answer without checking it?

Answers are not collected. The distribution of answers tells the teacher which weeks need more time: question 3 usually reveals the base-rate gap, question 7 the negation gap, and question 10 the audit gap.

# ^ Appendix B — Common errors, by week

| Week | Error | Why it happens | Fix |
|---|---|---|---|
| 1 | `false` read as a world fact | The output is a word, not a report | Ask "what would you add to know?" |
| 1 | Clause order treated as style | Declarative reading taught first | Show a reordering that changes the answer |
| 2 | Warrant restates the grounds | The distinction is verbal until used | Make the warrant a predicate that fails |
| 3 | `→` read as causes | Natural language | Truth table, one row |
| 3 | Unification read as assignment | Imperative background | One hole, one filler; `f(X,X)` |
| 4 | Invalid called unsound | Vocabulary without referents | Two-column contrast |
| 4 | Tree without substitutions | Trees drawn as pictures | Mark the substitution at each arc |
| 5 | Specification assumed complete | Tests pass | Find the wrong program it admits |
| 5 | `is` used to compare terms | Arithmetic habits | Three equalities table |
| 6 | Recursion without floor | The step is the interesting part | Delete the floor and run |
| 6 | Termination assumed | Small examples terminate | Cyclic data |
| 7 | Missing clause read as type error | No static types | Add a constructor and watch |
| 8 | Prevalence omitted | The question is framed conditionally | Frequencies first |
| 8 | `p(A given B)` and `p(B given A)` conflated | Notation | Two populations, two counts |
| 9 | Fallacy named first | The names are memorable | Mark the question, not the name |
| 9 | `\+` read as negation | The symbol looks like "not" | The `\+ (X=1, X=2)` example |
| 10 | `findall` assumed to sort | The name suggests collection | `setof` contrast |
| 10 | `label` before constraints | Imperative order of thought | Post, then label |
| 11 | Redundant constraint assumed inert | Logically true | Time the model |
| 12 | Tabling assumed to be an optimisation | It is usually presented as one | Find a query that terminates only with it |
| 12 | Fluent answer trusted | Fluency is the only signal available | Out-of-scope probe |
| 13 | Debugging by staring | No procedure | Shrink to three lines |
| 13 | Boundary note as disclaimer | Fear of being wrong | Specific failures, specific mechanisms |
| 14 | Defence as performance | Assessment pressure | Ask the third question early |

# ^ Appendix C — Software notes

## ^ Installation

SWI-Prolog from the distribution or from the upstream package. The libraries used are `clpfd`, `tables`, `lists`, `dcg` and `apply`. Verify with:

```prolog
?- use_module(library(clpfd)).
?- use_module(library(tables)).
```

s(CASP) is installed separately; the course container has it prebuilt. If building from source, follow the repository instructions and test with the bird example in week 12.

## ^ A minimal working file

```prolog
:- use_module(library(clpfd)).

parent(alice, bob).
parent(bob, carol).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% ?- ancestor(alice, X).
```

Load with `swipl file.pl`, then `?- [file].` inside the shell. The course uses the plain shell, not an IDE, so that `trace` is visible.

## ^ Tracing

```prolog
?- trace.
?- notrace.
?- spy(ancestor/2).
?- nospy(ancestor/2).
```

The four-level port model (call, exit, redo, fail) is worth ten minutes in week 4. Students who can read the ports can read any derivation.

# ^ Appendix D — Glossary

| Term | Meaning in this course |
|---|---|
| abduction | inference to the best explanation; not valid, indispensable |
| answer set | a consistent set of atoms satisfying an ASP program |
| base rate | the prevalence of a condition in the population, before the test |
| calibration | agreement between stated confidence and observed frequency |
| closed world | the assumption that what cannot be proved is false |
| countermodel | an interpretation in which the premises are true and the conclusion false |
| cut | a commitment that prunes choice points; loses the declarative reading |
| DCG | definite clause grammar; a notation for difference lists |
| declarative reading | what the program says is true |
| derivation | a chain from premises to conclusion |
| failure | a goal that cannot be proved; not a fact about the world |
| grounding | substituting constants for variables |
| labelling | enumerating values for constrained variables |
| model | an interpretation in which a set of sentences is true |
| mode | which arguments are inputs and which are outputs |
| negation as failure | `\+`; succeeds when the goal cannot be proved |
| propagation | domain reduction without search |
| SLD resolution | the selection rule, linear strategy, depth-first search used by Prolog |
| stable model | a consistent reading of a program with default negation |
| tabling | memoising subgoals to ensure termination |
| unification | finding the substitution that makes two terms identical |
| validity | truth in every interpretation |

# ^ Appendix E — The seven production tasks, in one table

| # | Artefact | The question it answers | The boundary it must state |
|---|---|---|---|
| 1 | Argument + rule base | What is the warrant? | What the encoding loses |
| 2 | Proof + countermodel | Is it valid? | What validity does not give |
| 3 | Specification + wrong program | What did the spec omit? | Which models it still admits |
| 4 | Diagnosis + recursion | What explains the failure? | Which explanations were not tested |
| 5 | Base-rate analysis | How common is it? | What the base rate does not decide |
| 6 | Transposition + constraint model | Does the form survive? | What propagation did not prove |
| 7 | Machine-answer audit | Is there a chain? | Who is responsible |

# ^ References

This volume is self-contained, but it stands in a set. The references are grouped so that a reader can see what is a source, what is a companion, and what is background.

## ^ The central document

- *The Glass Box: a complete curriculum for logical thinking through logic programming.* CURR-PLAN-001, Version 1.0, November 2026. The backbone: four chapters, nine gates, five tracks, seven rungs, the admission rule and the assessment model. This volume is the T4-CS elaboration of chapter 16 of that document.

## ^ Companion volumes

- *Logic, Evidence and Machines.* CURR-T4-GEN-001. The T4 curriculum for students outside computer science. Same backbone, same four questions, no programming requirement.
- *Summary for the Plenary.* The two-page handout.
- *The Glass Box: a 20-minute plenary presentation.* Slides and speaker script.

## ^ Project sources

- *From Naming to Doubting: a concept ladder for logical reasoning and critical thinking, ages 4 to adult.* Version 2, November 2026. The stages and gates.
- *An Introduction to Logical Thinking.* Version 2, November 2026. The university logical-thinking sketch, units U0–U9.
- *GROUP 4) UNIVERSITY, or POST-SECONDARY.* Project brief.
- *GROUP 3) HIGH SCHOOL.* Project brief, including the 14–18 band.

## ^ Logic and argument

- Grice, H. P. "Logic and Conversation." In *Syntax and Semantics 3: Speech Acts*, edited by P. Cole and J. L. Morgan, 41–58. New York: Academic Press, 1975. The Cooperative Principle, the maxims and implicature, used in weeks 2 and 10.
- "Implicature." *Stanford Encyclopedia of Philosophy*, revised 2024. https://plato.stanford.edu/entries/implicature/. The account of what is meant but not said, and its relation to entailment.
- Toulmin, S. *The Uses of Argument.* Cambridge University Press, 1958.
- Kahneman, D. *Thinking, Fast and Slow.* Farrar, Straus and Giroux, 2011. Chapters 14–16 on base rates and representativeness.
- Frankfurt, H. *On Bullshit.* Princeton University Press, 2005.
- Van Cleave, M. J. *Introduction to Logic and Critical Thinking,* version 2.0. Chapters 1 and 4.
- Facione, P. *Critical Thinking: What It Is and Why It Counts.*
- Open Logic Project. https://openlogicproject.org. Model theory, soundness, completeness.
- Wineburg, S. and McGrew, S. Lateral reading: the Stanford History Education Group materials.

## ^ Logic programming

- Arias, J. *Logic Programming.* https://hdl.handle.net/10115/41543. The formal spine: unification, SLD, semantics.
- SWI-Prolog manual. https://www.swi-prolog.org.Reference for every predicate used.
- Clocksin, W. and Mellish, C. *Programming in Prolog.* Springer, 2003. Still the clearest introduction to the declarative reading.
- O'Keefe, R. *The Craft of Prolog.* MIT Press, 1990. Modes, determinism, and the cost of cut.
- s(CASP). https://github.com/joaomoura/sCASP. Justifications and stable models.
- CLIP Lab logic-algebra material. https://cliplab.org/logalg. Constraints and tabling.
- Logica-URJC. https://github.com/Logica-URJC. Exercise infrastructure.

## ^ Teaching

- Bruner, J. *Toward a Theory of Instruction.* Harvard University Press, 1966. Enactive, iconic, symbolic.
- Biggs, J. and Tang, C. *Teaching for Quality Learning at University.* Open University Press, 2011. Constructive alignment, which is why the outcomes and the rubric share a vocabulary.

## ^ The document set

<!-- docset:start -->
- `00_Overview_and_Map.pdf` — *The Glass Box: overview and map.* The entry point: the Gricean standard, the four bands, the constant, the dial and the assessment spine. 27 pages.
- `G1-3_Foundations.pdf` — *Foundations: grades 1–3.* Naming, fact and guess, the question and the first rule. Eighteen unit cards and a scripted lesson. 24 pages.
- `G4-6_Rules_and_Search.pdf` — *Rules and Search: grades 4–6.* Rules, needed and enough, search, recursion, sources and the closed world. Eighteen unit cards and two scripted lessons. 27 pages.
- `G7-9_Critique.pdf` — *Critique: grades 7–9.* Standard form, counterexample, implicature, fallacies as questions and the first Prolog program. Eighteen unit cards. 27 pages.
- `G10-12_Judgement.pdf` — *Judgement: grades 10–12.* Validity, models, Prolog II, uncertainty, the AI audit and the limit-of-the-model defence. Eighteen unit cards. 26 pages.
- `T4_CS_Logical_Thinking_and_Logic_Programming.pdf` — *Logical Thinking and Logic Programming for Computer Science.* The fourteen-week computer-science course: two strands, labs, project brief, rubrics and examination. 89 pages.
- `T4_GEN_Logic_Evidence_and_Machines.pdf` — *Logic, Evidence and Machines.* The fourteen-week general course: evidence, argument and machines, with workshops and a capstone. 75 pages.
- `Adult_PostCollege.pdf` — *Judgement at Work.* Ten sessions of ninety minutes, with thirty-minute cores, for workplaces and community groups. 30 pages.
<!-- docset:end -->

This volume is the T4-CS volume. Its editable source is the matching `.md` file. The design archive, `Curriculum_Plan_Logic_Programming.pdf`, contains the full stage cards and the seventeen-stage ladder; it is not required for teaching.

## ^ Figures

This volume contains no figures by design. The figures belong to the central document; a course handbook that repeats them competes with the document it serves.
