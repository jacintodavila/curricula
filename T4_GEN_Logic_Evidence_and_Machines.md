---
title: Logic, Evidence and Machines
subtitle: A fourteen-week university curriculum for students outside computer science
version: Version 1.0
date: November 2026
doccode: CURR-T4-GEN-001
audience: T4-GEN · all disciplines · 18–22
running: T4-GEN · Logic, evidence and machines
prepared: Prepared by the curriculum drafting group. Companion volume to The Glass Box.
---

# ^ Preface

This is the general university curriculum at T4. It is for students of law, medicine, history, engineering, business, education, the arts and the sciences — anyone who will have to decide, in public and under pressure, what to believe and what a machine's answer is worth.

It assumes no programming, no formal logic and no statistics beyond school arithmetic. It assumes something harder to supply: that the student has been persuaded, at least once, by an argument that turned out to be bad.

The course keeps the backbone of the central document, *The Glass Box*, and delivers it without the programming track. The concepts are the same. The resolution is different. Where the computer-science volume builds a program, this volume reads one, questions one, and writes a rule base in plain language.

## ^ The claim of the course

> **Three questions decide most public disagreements: what is the evidence, what is the argument, and what is the machine doing?**

The first is about sources: who says so, how would they know, and who else could check. The second is about form: what is claimed, what supports it, what is assumed, and what would change it. The third is about delegation: when a system produces an answer, what has been delegated, to what, and to whom is the answer owed.

The course teaches each question for five weeks, then braids them for four, then asks the student to do all three in public.

## ^ What is in this volume

- the course design, outcomes and assessment;
- fourteen week chapters with notes, worked examples, workshops and the errors to expect;
- the capstone brief, the audit templates and the rubrics;
- three fully scripted sessions;
- an appendix of worked examples that can be reused as handouts;
- an explicit list of references at the end.

## ^ What this course is not

It is not a course in statistics, though it uses base rates. It is not a course in formal logic, though it uses validity and countermodels. It is not a course about computers, though it spends a third of its time on them.

It is a course in **judgement**: the disciplined formation of a belief that you can defend, revise and act on. The three strands are the three instruments judgement needs.

## ^ Where this volume sits

This is the general university volume. It is one of eight documents in the set.

- `00_Overview_and_Map.pdf` — the entry point.
- `G1-3_Foundations.pdf` — grades 1–3.
- `G4-6_Rules_and_Search.pdf` — grades 4–6.
- `G7-9_Critique.pdf` — grades 7–9.
- `G10-12_Judgement.pdf` — grades 10–12.
- `T4_CS_Logical_Thinking_and_Logic_Programming.pdf` — the companion university volume.
- `Adult_PostCollege.pdf` — the post-college sessions.

The course assumes the band 10–12 resolution but does not assume that every student had it. Week 1 includes a diagnostic, and the first three weeks re-teach standard form, sources and countermodels at university speed. A student who can spot a bad argument and cannot say what would change her mind has not met the course's obligation.

The Gricean standard is used in two ways. It is the editorial standard: one idea per paragraph, every section answering a stated question, terms defined at first use. It is also course content: week 2 introduces implicature as the theory of the unstated warrant, and week 10 uses it to expose the frame. The references list the source.

<!-- part: Part I — The course -->

# 1. Course design

## Aims

By the end, the student can:

1. **Audit evidence.** Take a claim and establish what would count for it and against it, using independent sources rather than repetition.
2. **Reconstruct argument.** Put a real argument into a form where its premises, warrant and conclusion are separate, and test each part.
3. **Read a model.** Understand what a rule-based or learned system can and cannot know, and ask for the chain rather than the answer.
4. **Decide and defend.** Reach a judgement under uncertainty, state its scope, and defend it in public while naming what would change it.

## Outcomes

On completion, the student can:

- distinguish testimony from evidence, and corroboration from repetition;
- reconstruct an argument in standard form with an explicit warrant and qualifier;
- produce a countermodel for an invalid argument and explain what it shows;
- distinguish necessary from sufficient conditions in a diagnosis or a policy;
- read a small rule base and identify what it does not know;
- convert a base-rate problem into natural frequencies and interpret the result;
- identify the characteristic failures of a generative system and audit one answer;
- state who is responsible for a delegated decision, and why.

## Who takes it

The course is compulsory for students in programmes that require a reasoning or evidence component, and elective for everyone else. It is designed for classes of 20 to 120. The workshop format assumes tables of four to six; a lecture theatre can be adapted by pairing rows, at some cost to the discussion.

No prerequisites. A short diagnostic in week 1 establishes the range; the course is pitched so that a student who has never seen a truth table and a student who has studied philosophy can both be stretched.

## The weekly rhythm

| Segment | Minutes | What happens |
|---|---|---|
| Recall | 10 | Three questions from last week, answered cold |
| Strand A | 45 | Evidence and argument, with a worked example |
| Strand B | 35 | Machines: a case, a rule base, an audit |
| Break | 10 | — |
| Workshop | 55 | The week's production task, in groups |
| Close | 5 | One sentence per table |

The workshop is not an application of the lecture. It is where the lecture is tested. A week whose workshop can be completed by repeating the lecture has failed.

## Assessment

| Component | Weight | What it is | Due |
|---|---|---|---|
| Portfolio | 40% | Six production tasks | Weeks 2, 4, 6, 8, 10, 12 |
| Argument audit | 25% | A 1,500-word reconstruction and test of one argument | Week 9 |
| AI audit | 15% | A structured audit of one machine answer | Week 11 |
| Capstone | 20% | A public defence of one contested claim | Weeks 13–14 |

The portfolio tasks are listed in Chapter 16. The argument audit and the AI audit are separate because they test different things: one is about human reasoning, the other about delegated reasoning. A student may be good at one and bad at the other, and the transcript should say so.

## Reading

The course uses short primary readings rather than a textbook. The essential items are:

- Toulmin, *The Uses of Argument*, chapters 1–3, for the anatomy;
- Kahneman, *Thinking, Fast and Slow*, chapters 14–16, for base rates;
- Frankfurt, *On Bullshit*, for the four-way distinction;
- the Open Logic Project, chapters on models and validity, for the formal core;
- one current model card or system card, chosen each year, for the audit.

All readings are supplied in the course pack. Students are not required to buy anything.

## A note on the machines strand

The machines strand is not a tour of architectures. It is the same three questions pointed at a system: what is the evidence for its answer, what is the argument it is making, and what has been delegated.

A student who leaves thinking that a language model is a database with better grammar has learned the important thing badly. A student who leaves able to say "this answer has no chain I can check, so I will use it as a draft and verify the three claims that matter" has learned the important thing well.

<!-- part: Part II — The fourteen weeks -->

# 2. Week 1 — Sources and testimony; what a machine is

## At a glance

| Strand | Content |
|---|---|
| Evidence | Testimony, independence, the regress of sources |
| Argument | Claim and support, introduced without vocabulary |
| Machines | What a generative system is, in one page |
| Workshop | Two sources, one claim, one contradiction |
| Assessed | Nothing; diagnostic quiz |

## Outcomes

By the end of the session, the student can:

- distinguish a source from a repetition of a source;
- explain why independence, not volume, is what corroboration requires;
- state what a language model is and is not, without metaphor;
- name one thing a machine answer cannot supply.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | None; two questions on the board |
| 10–55 | Evidence | Testimony; independence; the regress |
| 55–90 | Machines | What the system is; the three layers |
| 90–100 | Break | — |
| 100–155 | Workshop | Two sources, one claim |
| 155–165 | Close | One sentence per table |

## Evidence notes

### The regress of sources

Put a claim on the board.

> The new policy will reduce waiting times.

Ask: how do you know? The first answer will be a source — a minister, a report, a news article. Ask how that source knows. The chain continues until it reaches an observation, a measurement, a stipulation or a model. Every chain ends in something that is not another source.

This is the same regress as in the logic course, and it has the same moral: **the last step of every establishment is non-deductive.** A source is a shortcut to an observation someone else made. It is legitimate. It is not self-supporting.

Draw the chain on the board:

```
claim → news report → press release → model estimate → assumptions
```

Ask where the chain becomes weakest. It is usually at the last step, and the last step is usually invisible in the reporting.

### Independence

The most common error in student research is counting repetitions as corroboration. Five articles that quote the same press release are one source, not five.

Give the test.

> Two sources are independent if they would not both change in the same way if the claim were false.

That is a counterfactual test, and it is the right one. Two newspapers owned by the same group, quoting the same agency, fail it. A government statistic and an academic replication of it may pass, if the academic had access to the raw data.

**Exercise.** Give four apparent sources for one claim and ask the class to arrange them into independent lineages. The answer is usually two lineages and four appearances.

### Testimony and interest

Testimony is evidence, and it is interested. The interest does not make it false; it tells you what to check.

| Source | What they gain if believed | What to check |
|---|---|---|
| Vendor | A sale | Independent benchmark, on your workload |
| Regulator | Compliance, reputation | The raw data, the method |
| Journalist | Attention | The primary document |
| Academic | Citation, career | The replication, the effect size |
| Friend | Being right | Whether they saw it or heard it |

The professional habit is not cynicism. It is to ask what would have to be true for this source to be wrong, and whether anyone has checked it.

## Machines notes

### What it is

Write three sentences and make the class correct them.

> A language model is a very large database.
>
> It looks up the answer and returns it.
>
> It knows what it is saying.

All three are false in instructive ways. It is not a database; it is a statistical model of sequences. It does not look up; it generates, token by token, according to learned distributions. It does not know; it produces text that is shaped by its training and its prompt.

Then give the honest one-paragraph account.

> A generative system is trained on a large corpus to predict the next piece of text. It learns statistical structure, including a great deal of structure that behaves like knowledge. When you ask it a question, it produces a continuation. The continuation is often useful and sometimes true. It is not a report from a store of facts, and it does not come with a derivation unless the system has been built to produce one.

Ask what follows for trust. The answer is not "trust nothing". It is: trust where you can check, and build the check into the workflow.

### Three layers

Distinguish three things that are often conflated.

| Layer | What it is | What can go wrong |
|---|---|---|
| The model | Weights learned from data | Bias, gaps, staleness |
| The system | Model plus prompt, tools, filters | Retrieval errors, tool misuse |
| The use | Who asks what, and acts on it | Wrong question, unverified action |

Most public arguments about AI are about the first layer and most harm happens at the third. Say this in week 1 and repeat it in week 9.

## Workshop: two sources, one claim

Each table receives a claim and four source extracts: a press release, a news report quoting it, a blog post quoting the news report, and one independent document that either supports or contradicts the claim.

Tasks:

1. Draw the lineage. How many independent sources are there?
2. Identify the interest of each source.
3. Find the point where the chain is weakest.
4. Write one sentence: "We would need ______ in order to decide."

The final sentence is collected. Tables that write "more research is needed" are sent back; the sentence must name a specific document, measurement or test.

## Homework

Find a claim in your own field that is repeated everywhere. Trace it to its origin. Write 200 words on what you found, and whether the origin supports the repetition.

## Common errors

- Counting articles as sources.
- Treating a press release as the primary document.
- Assuming a source is unbiased because it is official.
- Describing a language model as a database.
- Asking whether AI is "good" instead of what this system, in this use, can be checked for.

# 3. Week 2 — Corroboration and standard form; the limits of the system

## At a glance

| Strand | Content |
|---|---|
| Evidence | Lateral reading; corroboration; the primary document |
| Argument | Standard form; grounds, warrant, claim |
| Machines | Scope; training data; what the system cannot know |
| Workshop | Reconstruct a real paragraph |
| Assessed | Portfolio 1: a source lineage and a standard-form reconstruction |

## Outcomes

By the end of the session, the student can:

- read laterally across sources rather than down a single page;
- reconstruct a paragraph in standard form with an explicit warrant;
- state the scope of a system and identify one question outside it;
- explain why a fluent answer can be outside the system's scope.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–55 | Evidence and argument | Lateral reading; standard form |
| 55–90 | Machines | Scope and the out-of-scope probe |
| 90–100 | Break | — |
| 100–155 | Workshop | Reconstruct and probe |
| 155–165 | Close | One warrant read aloud |

## Evidence and argument notes

### Lateral reading

Reading down a page tells you what the page says. Reading laterally tells you what the field says about the page. The move is to leave the document and search for its claim, its author and its funding.

Teach three moves.

1. **Leave.** Open a new tab; do not evaluate the page from the page.
2. **Find the original.** The primary document, the dataset, the judgment, the paper.
3. **Find the reaction.** Who has cited it, replicated it, disputed it.

The test is not whether the page looks credible. It is whether the claim survives contact with sources that do not depend on it.

### Standard form

Introduce the anatomy with a paragraph from the room. Use a university policy, a news editorial or a student's own homework claim.

> "The university should stop using the ranking. The ranking rewards spending per student, and our spending is below the sector median, so the ranking will always place us low."

Standard form:

1. The ranking rewards spending per student.
2. Our spending is below the sector median.
3. Therefore the ranking will always place us low.

Warrant, unstated:

4. Spending per student is the only factor that materially determines the rank, and the sector median is the relevant comparison.

Now the argument is testable. The grounds may be true; the warrant is where it fails, because rankings weight several factors and the median is not the threshold.

**The rule to teach.** Do not attack the grounds until you have found the warrant. Most arguments are defeated by making the implicit premise explicit.

### Qualifier and rebuttal

Ask for the qualifier: how strongly is the claim made? "Will always place us low" is a strong claim. A qualified version — "is likely to place us in the lower half" — is defensible and useful. Ask for the rebuttal: what would make the claim false? A change in the ranking formula, or a change in spending.

Most public arguments omit both, and the omission is not innocent: a claim without a qualifier cannot be tested.

### Grice: the warrant as implicature

The warrant is often not stated. Grice's theory of implicature explains how an unstated warrant is still communicated, and why the speaker can deny it later.

The Cooperative Principle: make your contribution such as is required, at the stage at which it occurs, by the accepted purpose of the exchange. Four maxims follow: Quality (be true), Quantity (be as informative as required), Relation (be relevant), Manner (be perspicuous).

An **implicature** is what a speaker means without saying. Grice's example: a referee writes only that a candidate's handwriting is excellent. The reader infers that the candidate is poor at philosophy. Nothing was said; everything was meant. The inference is calculable from the words, the situation and the assumption that the referee is cooperating.

Three consequences for this course.

**The warrant is often an implicature.** Reconstruct it by asking what the speaker must have assumed for the grounds to support the claim. In the ranking argument, the unstated warrant is that spending per student is the only factor that materially determines the rank. The speaker did not say it because it is obvious to her, or because stating it would invite the test.

**Implicature is cancellable.** A speaker can add a sentence that removes the inference: *Some faculties are below median — in fact, all are.* A writer can omit the cancellation and later say she never claimed the stronger thing. The audit must reconstruct the inference and ask whether it was cancelled.

**Flouting is a signal.** A speaker flouts a maxim when she deliberately and openly breaks it. In public argument, an obviously irrelevant detail may be carrying the message: a personal anecdote in a policy debate flouts Relation, and the implicature is that the statistics are not to be trusted. In a headline, *some* triggers a scalar implicature: the reader hears *not all*, because a cooperative writer would have said *all* if all were true.

The audit question is the one the course uses for machine answers: **what would the speaker have to know, and how would she know it?** For a human, the answer is access and interest. For a model, it is a training distribution. Neither is a chain.

Do not let the vocabulary replace the reconstruction. Students should be able to say *what was left out and why it matters* without using the word *implicature*. The word is a handle, not the skill.

## Machines notes

### Scope

Every system has a scope: the distribution it was trained on, the tasks it was evaluated on, the language and period it covers. Ask what is outside. Students will say "things it doesn't know", which is circular. Push for specifics: events after the training cut-off, languages with little text, specialised notation, private data, arithmetic with many digits, the interior of a physical system.

The out-of-scope probe is the diagnostic. Ask the system something just outside its scope and read the answer. It will usually be fluent. That is the finding.

### The scope statement

Give the template.

> This system is usable for ______, where the answer can be checked by ______. It is not usable for ______, because ______. The boundary is crossed when ______.

A scope statement with no third sentence is a marketing claim.

### Why fluency misleads

Fluency is a property of the text, not of the process. A system trained to produce plausible continuations produces plausible continuations whether or not it has the facts. The signal that normally warns us — hesitation, error, odd phrasing — is absent.

This is the single most important idea in the machines strand, and it is worth the whole of week 2. **The error does not look like an error.**

## Workshop: reconstruct and probe

Part 1. Each table receives a paragraph from a newspaper, a policy document or a court judgment. They reconstruct it in standard form, write the warrant, add a qualifier and a rebuttal.

Part 2. They are given one prompt and one answer from a system. They must write the scope statement and design one out-of-scope probe. They run the probe if a device is available; otherwise they are given the transcript.

Part 3. Each table reports the warrant and the probe. The room votes on which warrant was hardest to find. The vote is a useful diagnostic: the hardest warrant is usually the one the paragraph's author shares with the reader.

## Homework

Complete the portfolio entry: the source lineage and the standard-form reconstruction. Then write one sentence on what your own paragraph assumed that it did not say.

## Common errors

- Evaluating a page by its design.
- Writing a warrant that restates the grounds.
- Producing a standard form with no qualifier and calling it complete.
- Asking whether the system "knows" something instead of testing its scope.
- Treating a fluent out-of-scope answer as a minor error rather than the central failure mode.

# 4. Week 3 — Models and countermodels; confidence

## At a glance

| Strand | Content |
|---|---|
| Evidence | Models as simplified pictures; what a model leaves out |
| Argument | Validity; countermodels; truth in all cases |
| Machines | Confidence scores; calibration; the reframe test |
| Workshop | Find the countermodel; reframe the question |
| Assessed | Portfolio 2: a model, its omission, and a countermodel |

## Outcomes

By the end of the session, the student can:

- explain what a model is and name one thing it leaves out;
- test a simple argument for validity by searching for a countermodel;
- explain why a confidence score is not a probability of correctness unless it is calibrated;
- run a reframe test and interpret the result.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–50 | Evidence | Models and omissions |
| 50–85 | Argument | Validity and countermodels |
| 85–95 | Break | — |
| 95–155 | Workshop | Countermodel and reframe |
| 155–165 | Close | One countermodel on the board |

## Evidence notes

### Models

A model is a simplified representation built for a purpose. A map, a budget, an epidemic curve and a queueing simulation are all models. None is a copy of the world; each is a choice of what to include.

The test of a model is not "is it true" but "is it adequate for this purpose". Ask three questions of any model.

| Question | What it exposes |
|---|---|
| What is included? | The mechanism the author believes in |
| What is left out? | The assumption that it does not matter |
| For what purpose? | The decision the model is meant to support |

Give a concrete case. A hospital capacity model includes beds, staff and admission rates; it leaves out cleaning turnaround and staff sickness. For a weekly forecast it is adequate. For a winter crisis it is not, because the omitted factors are exactly the ones that bind.

### The model's silence

A model does not announce its omissions. The output looks equally confident whether or not the omitted factor matters. This is the same lesson as the machine's fluency, one level up: **the artefact's confidence is not evidence about its adequacy.**

The professional habit is to ask for the omission before the number. "What does this model leave out?" is a better question than "is this model accurate?", because the second invites a single number and the first invites the boundary.

## Argument notes

### Validity

An argument is valid if the conclusion cannot be false when the premises are true. This is a claim about form, not about the world.

Use three small arguments.

```
1. All doctors are graduates. Ana is a doctor. So Ana is a graduate.        valid
2. All doctors are graduates. Ana is a graduate. So Ana is a doctor.       invalid
3. All doctors are graduates. Some graduates are rich. So some doctors are rich.  invalid
```

For each, ask for a situation in which the premises are true and the conclusion false. That situation is the countermodel.

For the second: Ana is a graduate who is not a doctor. For the third: all doctors are poor and only the non-doctors are rich. Both are easy to describe, which is the point: countermodels are usually cheap.

### The asymmetry

> To show an argument is valid, you must cover every case. To show it is invalid, you need one.

This asymmetry explains a lot of public argument. People defend a claim by producing one case that fits, when the claim is universal. "It worked for me" is a counterexample to "it never works" and no evidence for "it always works".

### Necessary and sufficient

Introduce the pair with a diagnosis.

> A fever is necessary for this infection. A rash is sufficient for it.

Ask what follows. If the patient has the infection, they have a fever. If they have the rash, they have the infection. Neither gives the other direction.

Then the clinical version, which is the one that matters: a test can be sensitive without being specific, and vice versa. Sensitivity is about finding the condition when it is there; specificity is about ruling it out when it is not. Conflating them is the most common numerical error in medicine, and it is a necessary-and-sufficient error dressed in numbers.

## Machines notes

### Confidence

A system may report a score, a probability or a phrase ("I am confident"). Ask what the number means. A score of 0.9 is a claim about the frequency of correctness among answers with that score, and it is only meaningful if it has been measured on data like yours.

Most systems are not calibrated for your distribution. They are calibrated, if at all, on a benchmark. The benchmark's distribution is not your working life.

### The reframe test

Ask the same question twice with opposite framings and compare the answers.

> "Summarise the evidence that the policy worked."
>
> "Summarise the evidence that the policy failed."

If the two summaries are equally confident and mutually inconsistent, the system is producing text shaped by the framing, not a report of a stable body of evidence. That is not proof of unreliability in every case, but it is a cheap and powerful probe.

Run it live. The result is usually more convincing than any explanation.

### The calibration question

Ask: "For the last hundred answers you gave of this kind, how many were right?" A system cannot answer this. A calibrated system could. The absence of the answer is the finding.

## Workshop: countermodel and reframe

Part 1. Four arguments, two valid and two invalid. For each, either produce a countermodel or explain why none exists. Then translate one countermodel into a realistic situation in the student's own field.

Part 2. Two prompts, opposite framings, one system. Record both answers verbatim. Mark the claims that changed. Write one paragraph: what does the change tell you about the system?

Part 3. Write three sentences: what the system is good for, what it is not, and what you would check before acting.

## Homework

Find a model in your field — a forecast, a risk score, a budget. Write the three questions and their answers in 250 words.

## Common errors

- Asking whether a model is true.
- Treating a confidence score as a property of the answer rather than of the system's history.
- Assuming an invalid argument has false premises.
- Confusing sensitivity with positive predictive value.
- Running the reframe test once and generalising to all uses.

# 5. Week 4 — Diagnosis, necessary and sufficient; the closed world

## At a glance

| Strand | Content |
|---|---|
| Evidence | Diagnosis as reasoning under uncertainty; test characteristics |
| Argument | Necessary and sufficient conditions; the two-by-two table |
| Machines | The closed world; silence read as denial |
| Workshop | Build a diagnostic rule base in plain language |
| Assessed | Nothing new; portfolio 2 returned |

## Outcomes

By the end of the session, the student can:

- distinguish a risk factor, a cause, a symptom and a diagnostic test;
- use a two-by-two table to explain sensitivity and specificity;
- read a plain-language rule base and say what it assumes;
- explain why a system's "no" may mean "not found" rather than "not so".

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–50 | Evidence | Diagnosis; test characteristics |
| 50–85 | Machines | Closed world; the rule base |
| 85–95 | Break | — |
| 95–155 | Workshop | Diagnostic rule base |
| 155–165 | Close | One rule base on the board |

## Evidence notes

### Four roles

Students conflate these constantly, and the conflation produces bad reasoning about cause and treatment.

| Role | What it is | What it licenses |
|---|---|---|
| Risk factor | Raises the probability of the outcome | Prediction, not intervention |
| Cause | Intervening on it changes the outcome | Intervention, in principle |
| Symptom | Caused by the condition | Detection |
| Test result | Evidence about the condition | Updating, with error rates |

A risk factor can be a cause, but need not be. Age is a risk factor for most things and not a cause of any of them. A symptom is downstream of the condition; a test result is downstream of both.

### The two-by-two

Draw it for a test.

|  | Condition present | Condition absent |
|---|---|---|
| Test positive | true positive | false positive |
| Test negative | false negative | true negative |

Sensitivity is the left column: of those with the condition, how many test positive. Specificity is the right column: of those without, how many test negative. Neither tells you what a positive result means for this patient; that requires the prevalence (week 7).

**Exercise.** A test has 90 per cent sensitivity and 90 per cent specificity. Ask what a positive result means. Most will say 90 per cent. Hold the question until week 7, and tell them you are holding it. The delay is deliberate; the number needs the base rate to mean anything.

### Necessary and sufficient in diagnosis

A necessary condition must be present. A sufficient condition guarantees the outcome. In diagnosis, almost nothing is either, which is why diagnosis is probabilistic.

Ask: is a fever necessary for flu? No; some cases present without. Is it sufficient? Obviously not. The clinical reasoning is not syllogistic, and a curriculum that teaches it as syllogistic produces confident errors.

## Machines notes

### The closed world

Give this rule base in plain language.

```
A person is eligible if they are registered and they have passed the module.
Ana is registered.
Ana has passed the module.
Bo is registered.
```

Ask: is Bo eligible? A rule engine says no. Ask: is Bo ineligible? The engine cannot say that; it can only say that eligibility cannot be derived from what it has.

This is the closed-world assumption: what cannot be derived is treated as false. It is a useful convention and a dangerous one. A system built on it will answer "no" to questions it has no information about.

### Silence

The same failure appears in learned systems, in a different form. Ask a system about a person, a place or an event it has no data on. It will often produce an answer rather than silence, because the training objective rewards fluent continuation, not abstention.

The two failure modes are mirror images:

| System | What it does with no information | The error |
|---|---|---|
| Rule engine | Says no | Closed-world error |
| Generative model | Says something plausible | Confabulation |

Both are failures to represent ignorance. The professional response is the same: ask what the system would say if it did not know, and check whether that answer is available.

### Reading a rule base

Give a policy rule base and ask what it assumes.

```
A student is awarded the scholarship if they are resident and their household income is below the threshold.
A student is resident if they have lived in the region for three years.
```

Questions:

- What about a student who has lived there for two years and eleven months?
- What about a household whose income is exactly the threshold?
- What about a student whose residence is disputed?
- What does the rule base do with a missing income figure?

Every one of these is a boundary. The rule base is not wrong; it is silent, and the silence is where the disputes live.

## Workshop: diagnostic rule base

Each table builds a plain-language rule base for a diagnostic or eligibility decision in their own field. It must contain:

- at least four facts;
- at least two rules;
- one condition that is necessary but not sufficient;
- one case where the rule base gives an answer the world would not;
- a written boundary note of five sentences.

The boundary note is the marked artefact. The rule base is the occasion for it.

## Homework

Take the rule base home and find one case in your own experience where it would give the wrong answer. Write it up in 200 words.

## Common errors

- Treating a risk factor as a cause.
- Reading sensitivity as the probability of disease given a positive test.
- Believing a rule engine's "no" is a finding about the world.
- Writing a rule base with no missing-data case.
- Confusing a boundary note with a disclaimer.

# 6. Week 5 — Cause and correlation; explanation and argument

## At a glance

| Strand | Content |
|---|---|
| Evidence | Correlation, reverse causation, common cause, coincidence |
| Argument | Explanation versus argument; the same sentences, two jobs |
| Machines | The proof obligation; what a chain would have to be |
| Workshop | Two explanations, one dataset |
| Assessed | Portfolio 3: a causal claim tested three ways |

## Outcomes

By the end of the session, the student can:

- generate the four alternative explanations for a correlation;
- distinguish an explanation from an argument for the same conclusion;
- state the proof obligation and apply it to a machine answer;
- design an observation that would discriminate between two explanations.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–50 | Evidence | The four alternatives; natural experiments |
| 50–85 | Argument | Explanation versus argument; the proof obligation |
| 85–95 | Break | — |
| 95–155 | Workshop | Two explanations, one dataset |
| 155–165 | Close | One discriminator on the board |

## Evidence notes

### Four alternatives

For any correlation between A and B, there are four things to consider.

| Alternative | Question | Example |
|---|---|---|
| A causes B | Does intervening on A change B? | Smoking and cancer |
| B causes A | Is the arrow reversed? | Exercise and health |
| C causes both | Is there a common cause? | Ice cream and drowning |
| Coincidence | How often would this happen by chance? | Any spurious pair |

Teach the ice-cream case properly. Ice-cream sales and drowning deaths rise together. Ice cream does not cause drowning; hot weather causes both. The example is famous because it is clean, and it is worth ten minutes because the same structure appears in serious claims: hospital staffing and mortality, school funding and attainment, regulation and growth.

### Natural experiments

When you cannot randomise, look for a source of variation that is as good as random: a policy change, a threshold, a lottery, a border. The logic is that the variation is unrelated to the outcome except through the cause.

Give one example from the students' field. Ask what the variation is, and what it would not rule out. Natural experiments are strong evidence and not proof; the exclusion restriction is an assumption, and it can fail.

### The question that does most of the work

> Compared to what?

Every causal claim implies a comparison. Compared to no policy, or a different policy? Compared to last year, or to a similar region? A claim with no comparison group is a before-and-after story, and before-and-after stories are the most common form of confident error.

## Argument notes

### Explanation versus argument

> The service failed because the database ran out of connections.

As an argument, the connection exhaustion supports the claim that it failed. As an explanation, it accounts for a failure already accepted. The same sentence, two jobs.

Ask which job a post-mortem is doing. Often both, and the confusion matters: an explanation presupposes the fact. A post-mortem that only explains can leave the cause of the outage unestablished and the fix aimed at the wrong thing.

### Criteria

Four criteria for comparing explanations:

| Criterion | Question |
|---|---|
| Scope | How much of the evidence does it account for? |
| Simplicity | How many independent assumptions does it need? |
| Testability | What observation would discriminate? |
| Fit | Does it conflict with what else we know? |

Use them on a real case. The point is not that the best explanation is true; it is that the best of the candidates is the one to test first, and the candidate set is bounded by imagination.

### The proof obligation

State it.

> Anyone who asserts that a claim is established owes the chain that supports it and a statement of what would falsify it.

Apply it to a human argument and then to a machine answer. The machine answer usually has no chain, and the absence is the finding.

## Machines notes

### What a chain would be

For a system to supply a chain, it must have one of:

- a symbolic derivation from explicit rules;
- a retrieval path to sources that can be checked;
- a computation whose steps can be inspected.

A generative model asked "why?" produces text about a reason, not the reason. That text can be useful as a hypothesis. It is not a derivation, and treating it as one is the central error of the current period.

### The three uses

| Use | What it requires | What it forbids |
|---|---|---|
| Draft | Nothing; it is a draft | Acting on it unread |
| Assistant | A check on every claim that matters | Trusting the unmarked ones |
| Oracle | A chain and a calibration | Everything else |

Most professional use is the second. The failure mode is treating it as the third because it is convenient and the check is boring.

## Workshop: two explanations, one dataset

Each table receives a small dataset and two competing explanations. They must:

1. state what each explanation predicts;
2. find the observation that discriminates;
3. say which alternative (reverse, common cause, coincidence) is most plausible;
4. write the comparison group that the claim implies;
5. apply the proof obligation to one machine-generated summary of the data, supplied on the sheet.

## Homework

Find a causal claim in the news. Write the four alternatives, the comparison group, and the one observation you would want.

## Common errors

- Accepting a correlation because the mechanism sounds plausible.
- Forgetting reverse causation.
- Treating a before-and-after comparison as a control.
- Reading an explanation as an argument.
- Accepting a machine's stated reason as its derivation.

# 7. Week 6 — Sampling and generalisation; confabulation

## At a glance

| Strand | Content |
|---|---|
| Evidence | Samples, selection, survivorship, the denominator |
| Argument | Generalisation and the counterexample |
| Machines | Confabulation; the invented citation |
| Workshop | Find the missing denominator |
| Assessed | Nothing new; portfolio 3 returned |

## Outcomes

By the end of the session, the student can:

- identify the population a sample is meant to represent;
- recognise survivorship and selection effects;
- test a generalisation with a counterexample;
- recognise a confabulated citation and check it.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–50 | Evidence | Sampling; selection; survivorship |
| 50–85 | Machines | Confabulation; the citation test |
| 85–95 | Break | — |
| 95–155 | Workshop | Denominator hunt |
| 155–165 | Close | One missing denominator |

## Evidence notes

### The population

A sample is always a sample from something. Ask what. A survey of readers of a newspaper is not a sample of the public; a trial of volunteers is not a sample of patients; a set of successful companies is not a sample of companies.

The question to teach:

> Who is missing from this sample, and would their inclusion change the answer?

### Selection and survivorship

Survivorship is the extreme case: the sample contains only those who survived the process, and the process is what you are trying to evaluate.

Give the classic case and a modern one. The classic: returning aircraft and the armour question — reinforce where the returning planes have no holes, because the planes hit there did not return. The modern: startup advice drawn from founders of successful startups, which omits the founders who did the same things and failed.

The structure is the same. **The outcome selects the sample, and the selection is correlated with the cause.**

### The denominator

A number without a denominator is a rumour. "Ten thousand cases" of what, out of how many? "Three times more likely" than what?

Teach the habit: whenever a count appears, ask for the base. Whenever a rate appears, ask for the population. Whenever a comparison appears, ask for the group.

## Machines notes

### Confabulation

A generative system can produce a citation that does not exist, in the correct format, with a plausible author and journal. This is not a lie; it is a continuation of the pattern of citations.

The test is cheap: check the DOI, the title, the author. Do it live in the session with a fabricated reference. The room's reaction is the lesson.

### The three checks

| Check | What it catches | Cost |
|---|---|---|
| Does the source exist? | Fabricated citations | Seconds |
| Does it say what is claimed? | Misattribution | Minutes |
| Is it any good? | Weak evidence | Longer |

The first two catch most of the harm. The third is the discipline of the field.

### Why it happens

The system is optimising for a plausible continuation. A citation-shaped string is a plausible continuation of "studies show that". The model has no representation of whether the cited study exists, and no mechanism that would make it abstain. Saying this precisely is more useful than saying it "hallucinates".

## Workshop: denominator hunt

Each table receives six claims, each with a number and no denominator. They must find or construct the denominator, and say what it changes.

Examples:

- "The scheme has helped 4,000 families."
- "Reported incidents rose by 30 per cent."
- "Nine out of ten students recommend the course."
- "The drug reduces risk by half."
- "Crime is up in the city centre."
- "Our graduates earn 20 per cent more."

For each, the table writes the sentence they would need to see before believing it. The sentences are collected and typed up as a class resource.

## Homework

Take one number from your own field that you have repeated. Find its denominator. Write 200 words on whether it survived.

## Common errors

- Treating a sample as the population because it is large.
- Forgetting that the outcome selected the sample.
- Reporting a relative risk without a base.
- Checking a citation's formatting instead of its existence.
- Explaining confabulation as a lie or as a "bug" without saying what the system was doing.

# 8. Week 7 — Base rates and risk; calibration

## At a glance

| Strand | Content |
|---|---|
| Evidence | Base rates; natural frequencies; Bayes in odds form |
| Argument | The statistical claim; what the number supports |
| Machines | Calibration; the score that is not a probability |
| Workshop | The screening problem, three ways |
| Assessed | Portfolio 4: a base-rate analysis |

## Outcomes

By the end of the session, the student can:

- solve a screening problem with natural frequencies;
- solve the same problem with odds and check agreement;
- explain what a calibrated score means and what it does not;
- interpret a risk statement in absolute and relative terms.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–55 | Evidence | Base rates; frequencies; odds |
| 55–90 | Machines | Calibration; the score |
| 90–100 | Break | — |
| 100–155 | Workshop | Three ways to the same answer |
| 155–165 | Close | One number |

## Evidence notes

### The screening problem, resolved

Return to the question held in week 4.

> Prevalence 1 in 1,000. Sensitivity 99 per cent. Specificity 95 per cent. A person tests positive. What is the chance they have the condition?

Frequencies:

- 1,000 people;
- 1 has it; 0.99 test positive: about 1;
- 999 do not; 5 per cent test positive: about 50;
- 51 positives; 1 true: about 2 per cent.

The answer is about 2 per cent. Ask the class what would change it. A higher prevalence, a better specificity. Ask which matters more. Specificity, at low prevalence — and this is the answer that surprises clinicians as well as students.

### Odds

```
posterior odds = prior odds × likelihood ratio
```

Prior 1:999. Likelihood ratio 0.99/0.05 ≈ 20. Posterior ≈ 20:999 ≈ 1:50 ≈ 2 per cent.

The odds form is worth teaching because it makes the prior visible. The probability form hides it in the denominator, and a hidden prior is a prior that gets forgotten.

### Absolute and relative risk

"The drug halves the risk" is compatible with a reduction from 2 in 1,000 to 1 in 1,000. The relative number is large; the absolute number is small; the decision depends on the absolute number and on the harm of the treatment.

Teach the three-number rule: always report the baseline risk, the absolute reduction, and the relative reduction. A report with only one of the three is incomplete.

### Risk and uncertainty

Risk is quantifiable; uncertainty is not. Most decisions in professional life are made under uncertainty and discussed as if they were risk. The vocabulary matters: it changes what evidence would help, and it changes how much confidence is warranted.

## Machines notes

### What calibration means

A score is calibrated if, among all the cases scored 0.8, about 80 per cent have the property. Calibration is a property of the score across a population, not of a single answer.

Ask: calibrated on whom? A model calibrated on one hospital's patients may be miscalibrated on another's. The distribution shift is the failure, and it is invisible in the score.

### The base-rate trap in deployment

A system trained where prevalence is high will be deployed where it is low. The threshold that worked in training produces a flood of false positives in deployment. This is the screening problem at organisational scale, and it is the most common reason a technically working system fails in practice.

### The question to ask a vendor

> What is the prevalence in the population where this will be used, and how does the score behave there?

A vendor who cannot answer is selling a model, not a decision.

## Workshop: three ways

Each table solves three screening problems: one with a high prevalence, one with a low prevalence, one with an base rate of one in two. They solve each by frequencies, by odds, and by drawing the two-by-two. Then they write one paragraph on which method they would use to explain it to a patient, a manager, and a regulator.

The last part is the assessed one. The mathematics is the same; the communication is not.

## Homework

Find a risk claim in a leaflet, an advertisement or a paper. Rewrite it with the three numbers. Bring it.

## Common errors

- Reporting the sensitivity as the answer.
- Forgetting the prior in the odds form.
- Treating relative risk as absolute.
- Assuming a calibrated score transfers across populations.
- Confusing risk with uncertainty.

# 9. Week 8 — Uncertainty and fallacies; bias

## At a glance

| Strand | Content |
|---|---|
| Evidence | Expected value; what it hides; regression to the mean |
| Argument | Fallacies as questions; the tiered detector |
| Machines | Bias in data, rules and use |
| Workshop | Transpose a real argument |
| Assessed | Portfolio 5: a fallacy analysis with a transposition |

## Outcomes

By the end of the session, the student can:

- compute an expected value and name what it hides;
- recognise regression to the mean in a before-and-after story;
- use the generic detector before naming a fallacy;
- distinguish bias in data, in rules and in use.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–45 | Evidence | Expected value; regression |
| 45–80 | Argument | Fallacies as questions |
| 80–90 | Break | — |
| 90–155 | Workshop | Transposition |
| 155–165 | Close | One transposition |

## Evidence notes

### Expected value

Expected value is the probability-weighted average of outcomes. It is a summary, and like all summaries it hides the distribution.

Give two projects with the same expected value and different variances. Ask which to fund. The answer depends on the budget, the number of projects, and whether a loss is survivable. Expected value assumes you can average over repetitions; many decisions cannot be repeated.

### Regression to the mean

Extreme measurements are followed by less extreme ones, without any cause. A team with its worst quarter improves; a team with its best declines. Both are partly regression, and both are attributed to whatever happened next.

Ask: a school introduces a new method after its worst year and improves. What can we conclude? Nothing, without a comparison. This is the base-rate lesson in time, and it is the most common error in policy evaluation.

### The conjunction

A detailed story feels more probable than a simple one. It cannot be: a conjunction is a subset of each conjunct. The detail makes the story representative, and representativeness is not probability.

The professional version: a failure narrative with many specific causes feels more likely than "a combination of factors". It is not. Detail is a cost.

## Argument notes

### The detector

Tier 0: "Does that actually get you there?" If the answer is no, you have found the problem and you do not need a name.

Tier 1: is the appeal about the person or the feeling rather than the claim? (ad hominem, authority, emotion, bandwagon, tu quoque)

Tier 2: are there other options, enough cases, or is the premise the conclusion? (false dilemma, hasty generalisation, circularity, straw man)

Tier 3: what is the comparison, the quantifier, the base rate? (composition, division, equivocation, post hoc, cum hoc, base rate, conjunction, survivorship)

Tier 4: who benefits if you believe this? (manipulation, framing, scapegoating)

### Transposition

Replace the content, keep the form, and see whether it still persuades. If it does, the persuasion was in the form. If it does not, the original was doing something else — often appealing to identity or emotion.

Work one example in full, then have the class transpose a second. The exercise is diagnostic: students who can transpose can see form; students who cannot are still reading content.

### The failure mode

Naming without asking. Mark against it. An answer that names a fallacy and cannot say what question killed the argument is a vocabulary answer, and vocabulary is not judgement.

## Machines notes

### Three seats of bias

| Seat | What it is | Example |
|---|---|---|
| Data | The sample under-represents a group | A face dataset with few dark-skinned faces |
| Rules | A proxy encodes a history | Postcode as a proxy for creditworthiness |
| Use | The system is applied where it was not evaluated | A triage model used in a different hospital |

The third is the most common and the least discussed. A model is not biased in the abstract; it is biased in a use.

### The audit question

> Who is missing from the data, and what happens to them at the threshold?

The threshold is where bias becomes a decision. A model can be accurate on average and wrong for a group, and the average is what the vendor reports.

## Workshop: transposition

Each table takes two arguments: one from a campaign, one from a professional document. They transpose both and report which survived.

Then they take one claim from the machines strand — a vendor's claim about accuracy, fairness or safety — and transpose it. Vendor claims transpose badly, which is the finding.

## Homework

Complete the portfolio entry. Include one fallacy you found in your own reasoning, not in someone else's.

## Common errors

- Treating expected value as a decision rule.
- Attributing regression to an intervention.
- Naming a fallacy instead of asking the question.
- Treating bias as a property of a model rather than of a use.
- Auditing the average instead of the group at the threshold.

# 10. Week 9 — The argument audit; responsibility

## At a glance

| Strand | Content |
|---|---|
| Evidence | Putting it together: the audit method |
| Argument | Steelman, burden of proof, dialogue norms |
| Machines | Responsibility, delegation, liability |
| Workshop | Audit clinic |
| Assessed | Argument audit due (25%) |

## Outcomes

By the end of the session, the student can:

- steelman a view they reject;
- allocate burden of proof in a dispute;
- state who is responsible for a delegated decision and why;
- complete an argument audit to the rubric.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–45 | Argument | Steelman; burden; dialogue |
| 45–80 | Machines | Responsibility and delegation |
| 80–90 | Break | — |
| 90–155 | Clinic | Audit surgery, table by table |
| 155–165 | Close | Submission |

## Argument notes

### Steelman

A steelman is the strongest version of the other view, stated so well that its holder would accept it. It is not a concession and not a trick; it is a test. If your argument only defeats a weak version, you have not tested it.

Procedure:

1. State the other view in its own terms.
2. Add the best evidence for it.
3. Identify the strongest objection to your own view.
4. Answer it, or revise.

The fourth step is where learning happens. Most students discover that their position was a preference, not an argument.

### Burden of proof

Who must prove what? The default in a practical dispute is that the person proposing a change bears the burden, but the default flips when the change prevents serious harm, or when the status quo is itself a claim.

Ask the class to allocate the burden in three cases: a new drug, a hiring policy, a restriction on speech. The allocations differ, and the reasons for the differences are the content of the lesson.

### Dialogue norms

Four norms that make disagreement productive:

- attack the argument, not the person;
- state the other view before criticising it;
- give the evidence that would change your mind;
- distinguish "I don't know" from "you're wrong".

These are not politeness. They are the conditions under which the exchange produces information.

## Machines notes

### Delegation

When you act on a machine's answer, you have delegated a judgement. Delegation does not remove responsibility; it distributes it, and the distribution must be explicit.

Ask: who decided to use the system, who checked the output, who acted, and who bears the consequence? Four different people, usually, and the fourth is usually not in the room.

### The responsibility statement

Give the template.

> The decision to use this system was made by ______. The output was checked by ______ against ______. The action was taken by ______. If it is wrong, the consequence falls on ______. The check that would have caught this failure was ______.

The last sentence is the one that improves systems. It converts blame into a missing control.

### Liability is not the same as responsibility

Liability is legal; responsibility is professional. A developer may not be liable for a clinician's decision, and may still be responsible for a misleading interface. Distinguish the two, and do not let the legal question absorb the professional one.

## Clinic

Students bring their argument audit drafts. In tables, each draft is read by two others against the rubric. The readers must find:

- one premise that is asserted and not supported;
- one warrant that is implicit;
- one alternative explanation that is not considered;
- one place where the qualifier is missing.

The author revises and submits at the end of the session.

## Homework

None. The audit is the work.

## Common errors

- Steelmanning as a rhetorical trick.
- Assuming the burden always lies with the proposer.
- Confusing liability with responsibility.
- Writing a responsibility statement that names roles but no check.
- Auditing the conclusion instead of the argument.

# 11. Week 10 — Manipulation and refusal; the AI audit

## At a glance

| Strand | Content |
|---|---|
| Evidence | Misinformation, disinformation and the difference |
| Argument | The four-way distinction; refusal of the frame |
| Machines | The six-step audit, applied |
| Workshop | Build a manipulation; audit an answer |
| Assessed | Portfolio 6: a manipulation artefact and a debrief |

## Outcomes

By the end of the session, the student can:

- classify speech as mistake, disagreement, bullshit, trolling or manipulation;
- build a manipulation and explain which one they would fall for;
- complete the six-step audit on a machine answer;
- write a verdict with a reason.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–45 | Evidence and argument | The four-way distinction; techniques |
| 45–80 | Machines | The audit, step by step |
| 80–90 | Break | — |
| 90–155 | Workshop | Build and audit |
| 155–165 | Close | One confession each |

## Evidence and argument notes

### The distinction

| Kind | Relation to truth | Right response |
|---|---|---|
| Mistake | Believes it, wrong | Correct |
| Disagreement | Believes it, values differ | Argue values |
| Bullshit | Indifferent | Ask for the chain |
| Trolling | Wants a reaction | Do not feed |
| Manipulation | Wants a behaviour | Name and refuse |

The responses differ, and using the wrong one is a category error. Correcting a troll rewards them; arguing values with a mistake wastes the correction.

### Techniques

Decontextualise, fabricate, impersonate, polarise, scapegoat, flood, emotion first. Teach them as verbs and in order of cost. The cheap ones do most of the work.

### Refusal

Four moves: stop, source, corroborate, trace. Two harder ones: name the technique, refuse the frame.

Refusing the frame is the skill that takes longest. The manipulator asks "why is X so bad?"; the refusal is "X is not the issue; the issue is Y." Practise it aloud; it feels rude and is not.

### Implicature and the frame

A manipulation often works through implicature: the words are true, the inference does the work, and the speaker keeps the deniability.

Three patterns.

**The dog whistle.** A phrase has an acceptable literal meaning and a particularized meaning for a subgroup. The ambiguity is the point. Ask: what does this mean to the group it is aimed at, and what does the speaker gain from the ambiguity?

**The euphemism.** *Enhanced interrogation. Collateral damage. Letting people go.* The substitution softens the act. Ask for the plain description.

**The omission.** *Crime is rising. Waiting lists are falling.* Compared with what, over what period, for whom? The sentence can be true and the inference false. Ask for the denominator.

The three-column table from week 2 applies: **said**, **meant**, **evidence for the meaning**. The third column is what separates an audit from an accusation. The evidence can be the audience, the context, the speaker's other statements, or the pattern across cases. Without it, the audit is a feeling with a vocabulary.

## Machines notes

### The six steps

1. Scope.
2. Probe.
3. Chain.
4. Calibration.
5. Responsibility.
6. Verdict.

Walk through one audit on the screen. Use an answer the students have seen. Record the probe verbatim; paraphrase destroys the evidence.

### The verdict

Three options, each with a reason.

| Verdict | When | What it commits you to |
|---|---|---|
| Use | The claim is checkable and checked | The check is named |
| Use with check | The claim is useful and unverified | The check is specified |
| Refuse | The claim cannot be checked in the time available | The reason is stated |

"Use with check" is the professional default, and it is the one students skip. They either trust or reject; the middle option is the skill.

## Workshop: build and audit

Part 1. Tables build a manipulation with a real photograph and a false caption, or a fake quote, or a polarising pair of posts. Then the debrief: which was easiest, which was most convincing, which would you fall for? The confession is collected anonymously and read aloud.

Part 2. Each student audits one machine answer using the six steps. The answer must be one they actually received. The audit is one page.

Part 3. Tables exchange audits and mark one another against the rubric. The most common failure is a scope statement with no boundary.

## Homework

Complete the audit page. Bring it to the capstone workshop; it is a model for the boundary section.

## Common errors

- Treating manipulation as a kind of lying.
- Building a manipulation and skipping the debrief.
- Auditing the answer's tone rather than its scope.
- Writing "use with caution" instead of naming the check.
- Paraphrasing the probe.

# 12. Week 11 — The capstone workshop; accountability

## At a glance

| Strand | Content |
|---|---|
| Evidence | Choosing and narrowing a claim |
| Argument | The audit structure; the defence |
| Machines | Governance, procurement, accountability |
| Workshop | Capstone surgery |
| Assessed | AI audit due (15%) |

## Outcomes

By the end of the session, the student can:

- narrow a contested claim to a defendable scope;
- structure an audit that a reader can follow;
- explain the difference between model governance and use governance;
- deliver a three-minute summary of their capstone.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–40 | Evidence and argument | Scoping the claim; the audit structure |
| 40–75 | Machines | Governance and procurement |
| 75–85 | Break | — |
| 85–150 | Surgery | Three-minute pitches, table feedback |
| 150–165 | Close | AI audit submission |

## Evidence and argument notes

### Scoping

A capstone claim is usually too broad. "Social media harms teenagers" is a book. "Heavy social-media use is associated with worse sleep in 15-year-olds in our region" is an audit.

Teach three narrowing moves:

- **population** — who exactly?
- **comparison** — compared to what?
- **outcome** — measured how, over what period?

A claim that survives all three is auditable.

### The audit structure

| Section | Content | Length |
|---|---|---|
| The claim | Quoted, sourced, dated | 100 words |
| The strongest case | The best evidence for it | 400 words |
| The test | What would falsify it; the countermodel | 400 words |
| The verdict | Qualified, with scope | 200 words |
| What would change it | One observation | 100 words |

The strongest-case section is compulsory. An audit that only attacks is a prosecution, not an audit.

## Machines notes

### Two kinds of governance

| Kind | Question | Instrument |
|---|---|---|
| Model governance | Is the model documented, tested, monitored? | Model cards, audits, versioning |
| Use governance | Who may use it, for what, with what check? | Policy, training, approval |

Most organisations do the first and neglect the second. A well-documented model used without a check is still a hazard.

### Procurement

The procurement question is where public bodies have leverage.

> What is the prevalence where we will use it, what is the failure rate for each group, and what check does the interface require before an action?

A vendor who cannot answer these is selling a demonstration, not a system.

### Accountability

Name the four roles: commissioner, operator, subject, beneficiary. Ask which of them can find out that the system was used on them. If the answer is none, the system is unaccountable regardless of its accuracy.

## Surgery

Three-minute pitches. Each student states the claim, the strongest case, the test and the verdict. The table gives one piece of feedback: what is still too broad?

The pitches are timed. A student who cannot state the claim in thirty seconds has not narrowed it.

## Homework

Revise the capstone using the feedback. Prepare the presentation: six minutes plus questions.

## Common errors

- A claim so broad it cannot be tested.
- An audit that only attacks.
- Confusing model documentation with use policy.
- Naming the commissioner but not the subject.
- A verdict with no scope.

# 13. Week 12 — Writing the verdict; the presentation

## At a glance

| Strand | Content |
|---|---|
| Evidence | Weighing evidence; the verdict sentence |
| Argument | The qualified claim; the rebuttal |
| Machines | The boundary slide |
| Workshop | Full dress rehearsal |
| Assessed | Capstone draft reviewed |

## Outcomes

By the end of the session, the student can:

- write a qualified verdict that a reader can act on;
- present an argument in six minutes;
- answer a hostile question without retreating to vagueness;
- state the boundary of their own conclusion.

## The three hours

| Time | Segment | Content |
|---|---|---|
| 0–10 | Recall | Three questions |
| 10–40 | Evidence | Weighing; the verdict sentence |
| 40–75 | Argument | Presentation structure; hostile questions |
| 75–85 | Break | — |
| 85–150 | Rehearsal | Six-minute runs, two rooms |
| 150–165 | Close | One sentence each |

## Evidence notes

### Weighing

Students ask "how much evidence is enough?" The honest answer is that it depends on the cost of being wrong. Give the decision rule.

> The evidence is sufficient when the cost of checking further exceeds the cost of acting on what you have, given the harm of error.

This is not a licence for laziness; it is a demand to estimate both costs. A medical decision and a restaurant choice have different thresholds.

### The verdict sentence

A verdict is one sentence with four parts: the claim, the scope, the confidence and the condition.

> On the evidence available, X is probably true for population P, and I would revise if observation O occurred.

Unqualified verdicts are not stronger; they are less informative.

### What a reader needs

Three things: what you concluded, why, and what would change it. Everything else is supporting material. Put those three in the first paragraph and the last.

## Argument notes

### Structure

| Minute | Content |
|---|---|
| 0–1 | The claim, scoped, and why it matters |
| 1–3 | The strongest case for the claim |
| 3–4 | The test: what would falsify it, and what survived |
| 4–5 | The verdict, qualified |
| 5–6 | What would change your mind |

The strongest-case section is what distinguishes an audit from an opinion. Present it before the test, or the audience will think you are stacking the deck.

### Hostile questions

Three types, three responses.

| Type | Example | Response |
|---|---|---|
| The scope attack | "That's only one region." | "Yes; that is the scope. It would not generalise to X." |
| The evidence attack | "That study was small." | "Yes; here is the second, independent line." |
| The values attack | "You just don't like the policy." | "My conclusion would survive if I liked it; here is what would change it." |

The discipline is to concede what is true and hold what is supported. Conceding the scope is not losing the argument; it is demonstrating that you have one.

## Machines notes

### The boundary slide

One slide, four lines: scope, known failure, assumption, condition for revision. It is the visual form of the boundary note, and it is the slide examiners remember.

### The demonstration

If the capstone uses a system, demonstrate one probe and one failure. Do not demonstrate a success; the room has seen successes. Show the boundary.

## Rehearsal

Two rooms, six minutes each, a timer, and one listener with the rubric. Each student presents once, receives two comments, and presents again in the second half if time allows. The second run is visibly better, which is the point.

## Homework

Finalise the presentation and the written capstone.

## Common errors

- A verdict with no scope.
- Presenting only the case against.
- Answering a scope attack by generalising further.
- A boundary slide with no specific failure.
- Reading the slides.

# 14. Week 13 — Presentations I

## At a glance

| Strand | Content |
|---|---|
| Evidence | The capstone, presented |
| Argument | Defence under questioning |
| Machines | The boundary, demonstrated |
| Workshop | Eight presentations |
| Assessed | Capstone (20%), part 1 |

## Outcomes

By the end of the session, the student can:

- present a scoped claim and its test in six minutes;
- answer three questions with reasons;
- name the observation that would change their mind;
- give useful feedback to a peer.

## The session

| Time | Segment |
|---|---|
| 0–10 | Framing: the rubric, the timing, the questions |
| 10–100 | Eight presentations, six minutes plus four |
| 100–110 | Break |
| 110–150 | Four more presentations |
| 150–165 | Feedback synthesis |

The audience has a job. Each listener writes one question and one thing they would check. The questions are collected and given to the presenter; the checks are read aloud at the end, and they are usually better than the presentations.

## The three questions

Every presenter is asked:

1. What is the strongest evidence against your claim?
2. What would change your mind?
3. Where does your conclusion stop being true?

The third is the one that separates a scoped judgement from a slogan.

## Feedback

Feedback is structured: one strength, one question, one thing to check. Praise without a question is not feedback; criticism without a check is not useful.

# 15. Week 14 — Presentations II; the course in one page

## At a glance

| Strand | Content |
|---|---|
| Evidence | The remaining capstones |
| Argument | The obligation, restated |
| Machines | What to ask, for the rest of your life |
| Workshop | Presentations and close |
| Assessed | Capstone (20%), part 2 |

## The session

| Time | Segment |
|---|---|
| 0–5 | Framing |
| 5–95 | Ten presentations |
| 95–105 | Break |
| 105–140 | Four presentations |
| 140–155 | The course in one page |
| 155–165 | Close |

## The course in one page

| Strand | The question | The instrument | The failure it prevents |
|---|---|---|---|
| Evidence | How would they know? | Lineage, primary source, base rate | Repetition mistaken for corroboration |
| Argument | What is the warrant? | Standard form, countermodel, qualifier | Confidence mistaken for support |
| Machines | What has been delegated? | Scope, probe, chain, responsibility | Fluency mistaken for derivation |

The three failures are the same failure at different objects: **a signal that is easy to produce is mistaken for the thing it usually accompanies.** Repetition is easy; corroboration is not. Fluency is easy; derivation is not. Confidence is easy; calibration is not.

If the course has one sentence, it is this:

> Check the thing that is expensive to produce, because the cheap signal is the one that will be faked, accidentally or otherwise.

## Close

Each student writes one question they will ask for the rest of their life, on a card. The cards are typed up and sent to the class. The best are read at the start of the next cohort.

<!-- part: Part III — Assessment and resources -->

# 16. The portfolio

Six production tasks. Each is marked out of 100 and contributes to the 40 per cent component.

| # | Week | Task | What it must contain |
|---|---|---|---|
| 1 | 2 | Source lineage and standard form | Four sources arranged into lineages; a paragraph reconstructed with warrant, qualifier, rebuttal |
| 2 | 4 | A model and its omission | Three questions answered; one countermodel; one sentence on adequacy |
| 3 | 6 | A causal claim tested | Four alternatives; the comparison group; one discriminating observation |
| 4 | 8 | A base-rate analysis | The claim, the frequencies, the corrected reading, the decision |
| 5 | 10 | Fallacy analysis and transposition | The question before the name; a transposition; an honest report |
| 6 | 12 | Manipulation artefact and debrief | The artefact; which one you would fall for; the counter-move |

## Marking

| Criterion | Weight | Full marks |
|---|---|---|
| Accuracy | 30 | The arithmetic, the lineage, the form are right |
| The boundary | 30 | A specific statement of what the artefact does not establish |
| The reasoning | 25 | Steps shown; the warrant explicit; alternatives considered |
| The writing | 15 | Plain, specific, no filler |

An entry with no boundary statement cannot exceed 70. This is stated in week 1 and applied without exception.

# 17. The argument audit

## Brief

Choose one argument from public life, a professional document or your own field. Reconstruct it, test it, and reach a qualified verdict. 1,500 words.

## Structure

| Section | Content | Words |
|---|---|---|
| The argument | Quoted, sourced, dated, and why it matters | 200 |
| Standard form | Claim, grounds, warrant, qualifier, rebuttal | 300 |
| The strongest case | The best evidence for it, stated fairly | 300 |
| The test | Countermodel, alternative explanation or missing premise | 400 |
| The verdict | Qualified, scoped, with the condition for revision | 200 |
| Sources | Lineage, not a bibliography | 100 |

## Rubric

| Criterion | Weight | 0–40 | 40–70 | 70–100 |
|---|---|---|---|---|
| Reconstruction | 25 | Confuses claim and grounds | Complete but warrant vague | Warrant explicit and testable |
| Strongest case | 20 | Absent or a straw man | Fair but thin | An advocate would accept it |
| Test | 30 | Asserts the conclusion is wrong | Finds a weakness | Finds the decisive weakness or shows there is none |
| Verdict | 25 | Unqualified | Qualified but vague | Scoped, with a revision condition |

## Model opening

> The claim, as published in the [document] of [date], is that [claim]. I reconstruct it below in standard form. The warrant is not stated; I supply the version that makes the argument strongest. On that version the argument fails, for the reason given in section 4. I conclude that the claim is probably true for [population] and unsupported for [population], and I would revise if [observation].

Note what the model does: it states the claim, names the missing warrant, commits to the strongest reading, and gives a scoped verdict with a revision condition. Every one of those moves is marked.

# 18. The AI audit

## The six steps

| Step | What to record |
|---|---|
| Scope | System, version, date, task, and the boundary you believe applies |
| Probe | One question just outside the boundary, and the answer verbatim |
| Chain | Whether a chain exists; if so, reconstruct it; if not, say so |
| Calibration | Two framings of the same question; what moved |
| Responsibility | Commissioner, operator, subject, beneficiary; the check |
| Verdict | Use, use with check, or refuse, with the reason and the check |

## One page template

```
System and version:
Date and task:
Claim being checked:

SCOPE
  Trained/validated on:
  I believe it is out of scope for:

PROBE (verbatim)
  Question:
  Answer:

CHAIN
  A chain is available: yes / no
  If yes, reconstructed:
  If no, the claim rests on:

CALIBRATION
  Framing A answer:
  Framing B answer:
  What moved:

RESPONSIBILITY
  Commissioner:
  Operator:
  Subject:
  Beneficiary:
  The check that would catch this failure:

VERDICT
  Use / use with check / refuse
  Because:
```

## Rubric

| Criterion | Weight |
|---|---|
| Scope statement is specific and testable | 25 |
| Probe is genuinely out of scope and recorded verbatim | 20 |
| The chain is reconstructed or its absence is shown | 20 |
| Calibration test is designed and interpreted | 15 |
| Responsibility names a real check | 20 |

# 19. The capstone

## Brief

Defend one contested claim in public, using the three strands, in six minutes plus questions. The written capstone is 2,000 words and follows the same structure.

## The claim

It must be:

- **contested** — reasonable people disagree;
- **scoped** — a population, a comparison, an outcome;
- **consequential** — something would change if it were settled;
- **auditable** — evidence exists and can be checked.

A claim that fails any of the four is returned in week 11.

## The structure

| Section | Content | Words |
|---|---|---|
| Claim and scope | The claim, the population, the comparison, the outcome | 200 |
| Strongest case | The best evidence for it | 600 |
| The test | What would falsify it; what survived | 600 |
| Verdict | Qualified, with confidence and condition | 300 |
| Boundary | Where it stops being true | 300 |

## Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Scoping | 20 | A claim that could be settled |
| Strongest case | 25 | An advocate would accept the statement |
| Test | 25 | A real attempt to falsify, with the result |
| Verdict and boundary | 30 | Scoped, qualified, with a revision condition and a specific limit |

## The three questions

1. What is the strongest evidence against your claim?
2. What would change your mind?
3. Where does your conclusion stop being true?

# 20. Three scripted sessions

## Script 1: Week 7, the screening problem, 20 minutes

| Time | Move | What the teacher does |
|---|---|---|
| 0–2 | Pose | Writes the numbers on the board, no formula |
| 2–5 | Poll | Asks for a show of hands: 99, 95, 50, 2 per cent |
| 5–12 | Frequencies | Draws 1,000 people as dots; counts true and false positives |
| 12–16 | Name | Writes the answer, 2 per cent, and the odds form |
| 16–20 | Turn | "What would you change to make it 50 per cent?" |

The teacher's discipline is not to say "most people get this wrong". The poll already shows it. The satisfaction of the correction is the lesson.

## Script 2: Week 10, build a manipulation, 25 minutes

| Time | Move | What the teacher does |
|---|---|---|
| 0–3 | Frame | "You are the manipulator. The goal is to be believed." |
| 3–12 | Build | Tables make one artefact, with a real photo and a false caption |
| 12–18 | Swap | Artefacts are exchanged; each table rates plausibility |
| 18–23 | Debrief | "Which was easiest? Which would you fall for?" |
| 23–25 | Name | The techniques, after the experience |

The teacher's discipline is to let the room enjoy the exercise and then to ask the uncomfortable question. The confession is the assessment.

## Script 3: A capstone defence, 10 minutes

| Time | Move | What the teacher does |
|---|---|---|
| 0–1 | Frame | "Six minutes, then three questions. I will interrupt." |
| 1–4 | Claim and case | Listens for the scope in the first thirty seconds |
| 4–6 | Test and verdict | Notes whether the test could have failed |
| 6–9 | Questions | The three mandatory questions |
| 9–10 | Close | "One thing you would check with another week." |

The examiner's discipline is to ask question 3 — "where does it stop being true?" — even when the presentation is excellent. It is the question that reveals whether the student has a judgement or a position.

# ^ Appendix A — Worked examples

These can be photocopied as handouts.

## ^ A1. Standard form: the vendor claim

> "Three universities have adopted the platform and report improved outcomes. It is clearly the right choice for us."

1. Three universities adopted the platform.
2. They report improved outcomes.
3. Therefore it is the right choice for us.

Warrant: what happened at three universities predicts what will happen here, and "improved outcomes" means the outcomes we care about.

Test: the three are unlike us in intake, staff or subject mix; "improved outcomes" is measured differently; the report comes from the vendor.

## ^ A2. Countermodel: the invalid converse

```
All doctors are graduates.
Ana is a graduate.
Therefore Ana is a doctor.
```

Countermodel: Ana is a graduate with a degree in history. Premises true, conclusion false.

## ^ A3. Base rates: the rare condition

Prevalence 1 in 10,000. Sensitivity 99 per cent. Specificity 99 per cent. One million people.

- 100 have it; 99 test positive.
- 999,900 do not; 1 per cent test positive: 9,999.
- Total positives: about 10,098.
- True positives: 99.
- Answer: about 1 per cent.

The better the test, the more the false positives dominate at low prevalence. This is not a paradox; it is arithmetic.

## ^ A4. Cause or coincidence

> Ice-cream sales and drowning deaths rise together.

Alternatives: ice cream causes drowning (absurd); drowning causes ice cream (absurd); hot weather causes both (plausible); coincidence (possible). The test: compare within seasons, or look at the correlation across regions with different climates.

## ^ A5. The closed world

```
Eligible if resident and income below threshold.
Resident if three years in region.
```

Cases the rule base cannot decide:

- two years and eleven months;
- income exactly at the threshold;
- income unknown;
- residence disputed;
- a student who is resident but whose household has two incomes, one abroad.

## ^ A6. The audit probe

Question: "Summarise the main findings of the 2024 review of the scheme."

Answer: a fluent summary with three findings and a citation.

Probe: "What is the DOI of that review?"

Answer: a plausible DOI that resolves to nothing. Verdict: use with check; the citation is fabricated, the findings unverified.

# ^ Appendix B — Diagnostic quiz

1. If all A are B, and all B are C, are all A C?
2. If all A are B, and all B are C, are all C A?
3. A test is 99 per cent sensitive and 99 per cent specific; prevalence is 1 in 10,000. Roughly what is the chance a positive is a true positive?
4. What is the difference between a valid argument and a true conclusion?
5. What is a warrant?
6. Name the four alternatives to "A causes B".
7. What does "compared to what?" ask for?
8. What is the difference between a model and the world?
9. Why can a fluent answer be wrong?
10. Who is responsible when a machine's advice is acted on?

Not marked. The distribution tells the teacher where to spend time: question 3 for base rates, question 5 for argument, question 9 for machines.

# ^ Appendix C — Common errors, by week

| Week | Error | Fix |
|---|---|---|
| 1 | Counting articles as sources | Draw the lineage |
| 1 | Calling a model a database | The three layers |
| 2 | Evaluating a page by its design | Lateral reading |
| 2 | Warrant restates the grounds | Make it a testable claim |
| 3 | Asking whether a model is true | Ask what it leaves out |
| 3 | Treating a confidence score as a probability | Ask what it was calibrated on |
| 4 | Risk factor treated as cause | The four roles |
| 4 | "No" read as a finding | The closed world |
| 5 | Correlation accepted for its mechanism | The four alternatives |
| 5 | Explanation read as argument | Which job is it doing? |
| 6 | Sample treated as population | Who is missing? |
| 6 | Citation checked for format | Check existence |
| 7 | Sensitivity reported as the answer | Frequencies first |
| 7 | Relative risk reported alone | Three numbers |
| 8 | Expected value as a decision rule | Variance and survivability |
| 8 | Fallacy named before the question | Mark the question |
| 9 | Steelman as a trick | State it so they accept it |
| 9 | Liability absorbs responsibility | Name the missing check |
| 10 | Manipulation treated as lying | The four-way distinction |
| 10 | "Use with caution" as a verdict | Name the check |
| 11 | Claim too broad | Population, comparison, outcome |
| 11 | Governance without use policy | Two kinds of governance |
| 12 | Verdict with no scope | The four-part sentence |
| 13 | Scope attack answered by generalising | Concede the scope |
| 14 | Reading the slides | The boundary slide |

# ^ Appendix D — Glossary

| Term | Meaning in this course |
|---|---|
| base rate | the prevalence of a condition before the evidence |
| calibration | agreement between a stated confidence and observed frequency |
| closed world | treating what cannot be found as false |
| confabulation | fluent production of unsupported content |
| countermodel | a situation where the premises hold and the conclusion fails |
| corroboration | independent confirmation, not repetition |
| denominator | the population a count is drawn from |
| explanation | an account of why something is so, given that it is |
| lateral reading | leaving a source to check it against others |
| necessary condition | must be present for the outcome |
| qualifier | the strength of a claim |
| regression to the mean | extreme values followed by less extreme ones |
| selection effect | the sample is chosen by the outcome |
| specificity | of those without the condition, the proportion testing negative |
| sufficient condition | guarantees the outcome |
| survivorship | the sample contains only those who survived the process |
| validity | the conclusion cannot be false when the premises are true |
| warrant | the principle that connects grounds to claim |

# ^ References

This volume is self-contained, but it stands in a set. The references are grouped so that a reader can see what is a source, what is a companion, and what is background.

## ^ The central document

- *The Glass Box: a complete curriculum for logical thinking through logic programming.* CURR-PLAN-001, Version 1.0, November 2026. The backbone: four chapters, nine gates, five tracks, seven rungs, the admission rule and the assessment model. This volume is the T4-GEN elaboration of chapter 16 of that document.

## ^ Companion volumes

- *Logical Thinking and Logic Programming for Computer Science.* CURR-T4-CS-001. The T4 curriculum for computer-science students, with the fourteen-week programming track.
- *Summary for the Plenary.* The two-page handout.
- *The Glass Box: a 20-minute plenary presentation.* Slides and speaker script.

## ^ Project sources

- *From Naming to Doubting: a concept ladder for logical reasoning and critical thinking, ages 4 to adult.* Version 2, November 2026.
- *An Introduction to Logical Thinking.* Version 2, November 2026.
- *GROUP 4) UNIVERSITY, or POST-SECONDARY.* Project brief, including the two-track proposal and the AI-literacy request.
- *GROUP 5) OUTSIDE ACADEMIA.* Project brief for the adult track.

## ^ Evidence and argument

- Grice, H. P. "Logic and Conversation." In *Syntax and Semantics 3: Speech Acts*, edited by P. Cole and J. L. Morgan, 41–58. New York: Academic Press, 1975. The Cooperative Principle, the maxims and implicature, used in weeks 2 and 10.
- "Implicature." *Stanford Encyclopedia of Philosophy*, revised 2024. https://plato.stanford.edu/entries/implicature/. The account of what is meant but not said, and its relation to entailment.
- Toulmin, S. *The Uses of Argument.* Cambridge University Press, 1958.
- Kahneman, D. *Thinking, Fast and Slow.* Farrar, Straus and Giroux, 2011.
- Frankfurt, H. *On Bullshit.* Princeton University Press, 2005.
- Facione, P. *Critical Thinking: What It Is and Why It Counts.*
- Van Cleave, M. J. *Introduction to Logic and Critical Thinking,* version 2.0.
- Open Logic Project. https://openlogicproject.org.
- Wineburg, S. and McGrew, S. Lateral reading materials, Stanford History Education Group.
- O'Neill, O. *A Question of Trust.* Cambridge University Press, 2002. On testimony and accountability.

## ^ Machines

- Mitchell, M. *Artificial Intelligence: A Guide for Thinking Humans.* Pelican, 2019.
- O'Neil, C. *Weapons of Math Destruction.* Crown, 2016.
- Gebru, T. et al. "Datasheets for Datasets." Communications of the ACM, 2021.
- Mitchell, M. et al. "Model Cards for Model Reporting." FAT*, 2019.
- NIST. *AI Risk Management Framework.* 2023. For the governance vocabulary.

## ^ Teaching

- Bruner, J. *Toward a Theory of Instruction.* Harvard University Press, 1966.
- Biggs, J. and Tang, C. *Teaching for Quality Learning at University.* Open University Press, 2011.

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

This volume is the T4-GEN volume. Its editable source is the matching `.md` file. The design archive, `Curriculum_Plan_Logic_Programming.pdf`, contains the full stage cards and the seventeen-stage ladder; it is not required for teaching.

## ^ Figures

This volume contains no figures by design. The figures belong to the central document; a course handbook that repeats them competes with the document it serves.
