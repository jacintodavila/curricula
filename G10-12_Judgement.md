---
title: Judgement
subtitle: Logical thinking for grades 10–12, ages 15–18
version: Version 2.0
date: November 2026
doccode: CURR-G10-12-001
audience: Teachers of grades 10–12 · ages 15–18
running: JUDGEMENT · GRADES 10–12
prepared: Prepared by the curriculum drafting group. One of four grade-band documents in The Glass Box set.
---

# ^ Preface

This is the curriculum for grades 10–12. It is for young people who are about to vote, work, borrow, consent and be responsible for a decision that a system made about them.

The band has one job: **the learner can judge validity, weigh uncertainty, audit a machine answer, and defend a boundary.** The three years build that job from the formal test of validity to the public defence of a model's limits.

The document is standalone. It contains the year map, eighteen unit cards, a scripted defence lesson, the Gricean audit, the assessment, the common errors and the out-of-bounds list.

Three principles shape the band.

**Validity is a standard, not a trophy.** A valid argument from a false premise is the most persuasive lie there is. The learner must be able to say both things in one breath.

**Uncertainty is not a failure of rigour.** A decision under uncertainty can be rigorous. The learner learns to state the base rate, the sensitivity and the cost of being wrong.

**Every model has an edge, and the edge is the lesson.** The program, the statistic, the policy and the machine answer all stop somewhere. The learner's final task is to say where, and to defend the line.

# ^ How to use this document

## ^ The shape of the year

One 55-minute lesson each week, for 36 weeks. Three years, 108 lessons. The lessons sit inside mathematics, science, civics, philosophy, computer science or a weekly seminar.

Each unit is six lessons. The sixth lesson is the defence: the learner presents the artefact and answers three questions — *what does it claim, what does it not claim, and where does it stop?*

## ^ The shape of a unit card

**Question.** The one question the unit teaches the learner to ask.

**Do.** Three activities that make the question operational.

**Words.** The vocabulary the learner should be able to use by the end.

**Evidence.** What the teacher keeps, and what it shows.

**Out of bounds.** What not to introduce in this unit, even if a learner asks.

## ^ The five-move lesson, at this resolution

The shape is unchanged: a thing in the hand, a question with a gap, a try, a compare, a name. The thing is now a formal object — a truth table, a program, a statistic, a policy — and the name is a distinction the learner will use in public.

The discipline is the same. The teacher does not define validity before the class has tried to break an argument. She does not define a base rate before the class has been fooled by a test result. She does not define the closed world before the program has said *no* to a fact it did not have.

# ^ The band at a glance

| Year | Grade | The question | Units | The artefact |
|---|---|---|---|---|
| 1 | 10 | Does it follow, and from what? | 6 | A proof and a countermodel for the same sentence |
| 2 | 11 | What does the machine do, and how sure are we? | 6 | A program with a cut, a base-rate analysis and a causal diagram |
| 3 | 12 | Where does the model end, and who is accountable? | 6 | A *Limit of the Model* defence and a machine audit |

## ^ What the learner can do at the end

A learner who completes the band can:

- test an argument for validity with a truth table and a countermodel;
- explain why a valid argument can be unsound;
- use quantifiers without confusing *all* with *some*;
- read a proof as a chain from premises, not as a proof of the premises;
- write a Prolog program with recursion, lists, cut and negation;
- explain what cut costs and why a faster program can be a worse one;
- explain the difference between a stable model and a single answer;
- calculate a posterior probability from a base rate and a test;
- distinguish correlation from intervention, and name a confounder;
- audit a public argument for its hidden premise and its missing comparison;
- audit a machine answer for its chain, its confidence and its accountability;
- defend a model's boundary in five minutes, under three questions.

## ^ What the band does not do

It does not prove completeness. It does not teach graduate model theory. It does not teach the full probability calculus. It does not teach machine-learning engineering. It does not pretend that a valid argument is a true one, or that a fluent answer is a chain.

# ^ The Gricean audit

## ^ Cooperation and strategy

Grice's Cooperative Principle assumes a shared purpose. Most conversation has one. Public argument often does not.

A speaker may be trying to inform, to persuade, to win, to confuse, to signal to one group while sounding acceptable to another, or to avoid liability. The cooperative presumption is still there — the listener cannot help assuming it — and that is exactly what makes strategic communication possible.

The audit therefore asks two questions, not one.

1. **What would this mean if the speaker were cooperating?**
2. **What is the speaker actually doing?**

The gap between the answers is the space of strategy, manipulation and deniability.

## ^ The four maxims as audit questions

| Maxim | The question | The public failure |
|---|---|---|
| Quality | Is it true, and what is the evidence? | Assertion without a source; confidence without a chain |
| Quantity | What is left out? | The missing denominator; the omitted comparison; the buried caveat |
| Relation | Does it answer the question? | The red herring; the irrelevant frame |
| Manner | Is it clear, and to whom? | Ambiguity that protects the speaker; jargon that excludes |

## ^ Implicature in public argument

The reference letter from grades 7–9 is the model. A speaker says something true and means something more. The audience infers the meaning because it assumes cooperation. The speaker can later deny the meaning because it was never said.

Three public patterns matter.

**The dog whistle.** A phrase has a literal meaning that is acceptable to the general audience and a particularized implicature for a subgroup. The deniability is the point. The audit asks: what does this phrase mean to the group it is aimed at, and what does the speaker gain from the ambiguity?

**The euphemism.** *Enhanced interrogation. Collateral damage. Letting people go.* The words soften the act. The implicature is carried by the substitution. The audit asks: what is the plain description?

**The omission.** *Crime is rising.* Compared with what? Over what period? For whom? The sentence can be true and the implicature false. The audit asks for the denominator.

## ^ The machine that sounds cooperative

A language model is trained to produce text that fits the local context: relevant, informative, clear, confident. It is, in Grice's terms, a cooperative-sounding text generator. It has no purpose, no evidence and no accountability.

The cooperative presumption does the rest. The fluent answer feels like a helpful speaker. The audit must break the illusion with three questions:

1. **What would the speaker have to know?** The model would have to know the facts, the sources, the current date and the limits of its training.
2. **How would she know it?** The model has a training distribution, not an investigation.
3. **Who is accountable if it is wrong?** The model is not. The person who used it is.

The answer is not *never use the machine*. It is *use it as a draft, a prompt or a search aid, and supply the chain yourself*.

## ^ What Grice does not say

He does not say that all communication is cooperative. He does not say that implicature is always intended. He does not say that the maxims are rules everyone follows. They are assumptions listeners make, and speakers can exploit. That is why the audit is necessary.

<!-- part: Part I — The three years -->

# 1. Year 1 — Validity and models

## ^ The year's question

Does it follow, and from what?

The first year gives the learner the formal apparatus and, at the same time, its limit. A truth table shows validity for a small finite language. It does not show that the premises are true. A proof shows that the conclusion follows. It does not show that the conclusion matters.

## Validity, again

**Question.** What exactly does validity claim?

**Do.** Three arguments: one valid and sound, one valid and unsound, one invalid. The learner states what validity claims — *if the premises are true, the conclusion cannot be false* — and what it does not claim — *the premises are true*. Then she writes the two verdicts separately for each argument.

**Words.** validity, soundness, premise, conclusion, cannot be false, if the premises are true.

**Evidence.** The learner writes a validity verdict and a soundness verdict for each of the three arguments.

**Out of bounds.** Do not use "true in all models" until unit 1.3. The conditional definition comes first.

## Truth tables

**Question.** Can a table show that an argument is valid?

**Do.** Build the truth table for *P → Q*. Mark the one row where it is false. Then test the argument *P → Q; P; therefore Q*. Find the row where both premises are true and the conclusion false. There is none. Then test *P → Q; Q; therefore P*. Find the row. The table is a search over all the cases.

**Words.** truth table, row, true, false, conditional, premise, conclusion, valid.

**Evidence.** The learner completes two tables and marks the invalid row.

**Out of bounds.** Do not go beyond three variables. Do not teach natural deduction yet.

## Countermodels

**Question.** What is the smallest world in which the argument fails?

**Do.** Draw a world with two objects and one property. Make the premises true and the conclusion false. Then a world with three objects. The drawing is a model. A countermodel is a model of the premises that is not a model of the conclusion. The learner sees that validity is the absence of a countermodel, not the presence of a warm feeling.

**Words.** model, countermodel, world, object, property, interpretation, true in a model.

**Evidence.** The learner draws a countermodel for an invalid argument and explains why the valid one has none.

**Out of bounds.** Do not teach the formal definition of satisfaction. The drawing is the definition at this resolution.

## Quantifiers

**Question.** What does *all* commit you to?

**Do.** A domain of five objects. *All ravens are black. Some ravens are black. No ravens are black.* Draw the cases. Then the countermodel to *all*: one non-black raven. Then the countermodel to *some*: no ravens at all. The learner sees that *all ravens are black* can be true when there are no ravens, while *some ravens are black* requires at least one. That is the difference the quantifiers mark.

**Words.** all, every, some, none, domain, object, countermodel, existential.

**Evidence.** The learner draws a countermodel for *all* and for *some*.

**Out of bounds.** Do not teach the square of opposition or syllogistic figures. Do not use `∀` and `∃` until the pictures are secure.

## Proof and derivation

**Question.** What does a proof prove?

**Do.** A short natural-deduction proof. The class checks each step against a rule. Then the teacher changes one premise and asks: does the proof still work? The proof shows that the conclusion follows from the premises. It does not show that the premises are true. The learner writes the two claims separately.

**Words.** proof, derivation, step, rule, assumption, discharge, follows from, premise.

**Evidence.** The learner writes a four-step proof and states what it does and does not establish.

**Out of bounds.** Do not require a full proof system. Four rules are enough: assumption, implication introduction, implication elimination, and one quantifier rule.

## Soundness and the truth of premises

**Question.** How do we know the premises?

**Do.** Take a valid argument from a newspaper. Check the form. Then check the premises against sources. The form is good; the premise is unsupported. The argument is valid and unsound. Then the reverse: a true conclusion from a bad argument. The learner writes a verdict that names both the form and the input.

**Words.** sound, unsound, premise, source, support, valid, true, verdict.

**Evidence.** The learner writes a two-part verdict for a real argument: form and input.

**Out of bounds.** Do not let "sound" become a synonym for "convincing". It has a definition: valid and all premises true.

# 2. Year 2 — Machines and uncertainty

## ^ The year's question

What does the machine do, and how sure are we?

The second year has two halves. The first half goes deeper into logic programming: lists, cut, negation, and multiple models. The second half turns to uncertainty: base rates, sensitivity, risk, and the difference between correlation and intervention. The two halves meet in the idea of a model with a boundary.

## Prolog II: lists and recursion

**Question.** How does a program work over a structure it did not name in advance?

**Do.** The list. `[a, b, c]` is `[a | [b, c]]`. Write `member/2`:

```prolog
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).
```

Trace `?- member(b, [a, b, c]).` Then `?- member(X, [a, b, c]).` The second query returns three answers. The learner draws the tree and marks the base case.

**Words.** list, head, tail, recursion, base case, member, trace, choice point.

**Evidence.** The learner traces a list query and explains the base case.

**Out of bounds.** Do not teach difference lists yet. Do not teach DCGs.

## Cut and commitment

**Question.** What does it cost to tell the machine *do not look back*?

**Do.** Write a rule that lists all of a person's children:

```prolog
child(alice, bob).
child(alice, carol).

children(P, C) :- child(P, C).
```

The query `?- children(alice, C).` returns two answers. Now add a cut after the first match:

```prolog
first_child(P, C) :- child(P, C), !.
```

The query returns one answer. The predicate has changed from *C is a child of P* to *the first child the program happens to find*. The cut bought speed and lost the declarative reading. Then show a legitimate use: a maximum rule where the cut prunes only alternatives that cannot succeed, and note that the answers do not change there. The learner writes the declarative reading that was lost in the first case, and the one that was preserved in the second.

**Words.** cut, commitment, choice point, prune, declarative reading, procedural reading, cost.

**Evidence.** The learner shows one query whose meaning changes when the cut is added.

**Out of bounds.** Do not teach the full operational semantics of cut. One transparent example is enough.

## Negation as failure

**Question.** What does the machine mean by *no*?

**Do.** Revisit the grade 9 lesson with a sharper case. `\+ parent(alice, carol)` succeeds because the fact is absent. Add the fact; it fails. The *no* is *not provable*, not *false in the world*. Then a rule with negation in the body. What happens when the fact is unknown? The program makes a choice on incomplete information. The learner writes the assumption.

**Words.** negation as failure, not provable, absent, unknown, assumption, closed world, incomplete.

**Evidence.** The learner explains a query result with the words *not provable* and names the assumption.

**Out of bounds.** Do not teach stable-model semantics yet. Unit 2.4 introduces it.

## Answer-set programming

**Question.** Can a program have more than one correct answer?

**Do.** A small ASP program:

```prolog
p :- not q.
q :- not p.
```

The program has two answer sets: `{p}` and `{q}`. Neither is forced. The learner draws both. Then a program with a constraint that removes one. The lesson: a declarative program can describe a set of models, not a single output.

**Words.** answer set, stable model, default negation, constraint, multiple models, choice.

**Evidence.** The learner writes the two answer sets for one program and explains why there are two.

**Out of bounds.** Do not teach the full ASP semantics. Two rules and one constraint are enough.

## Base rates and risk

**Question.** How likely is it, given the test?

**Do.** The disease case. Prevalence 1%. Sensitivity 99%. Specificity 99%. A person tests positive. What is the probability she has the disease? Most say 99%. The natural-frequency table:

- 10,000 people.
- 100 have the disease. 99 test positive.
- 9,900 do not. 99 test positive falsely.
- 198 positives. 99 have the disease. The answer is 50%.

Then absolute versus relative risk: a drug reduces the risk from 2 in 1,000 to 1 in 1,000. Relative risk: 50%. Absolute risk: 1 in 1,000. Number needed to treat: 1,000.

**Words.** base rate, prevalence, sensitivity, specificity, false positive, posterior, absolute risk, relative risk, number needed to treat.

**Evidence.** The learner calculates the posterior from a natural-frequency table and states the absolute risk.

**Out of bounds.** Do not teach Bayes' theorem as a formula before the table. The table is the theorem at this resolution.

## Correlation, cause and intervention

**Question.** Would intervening change the outcome?

**Do.** Ice-cream sales and drowning. A third variable: temperature. The correlation is real and not causal. Then a randomised trial and a natural experiment. The learner draws a causal diagram with one confounder and one intervention. The question is not *what goes with what?* but *what happens if we change it?*

**Words.** correlation, cause, confounder, intervention, randomised trial, natural experiment, diagram.

**Evidence.** The learner draws a diagram with a confounder and states what an intervention would change.

**Out of bounds.** Do not teach structural equation modelling. One confounder and one intervention are enough.

# 3. Year 3 — Judgement in public

## ^ The year's question

Where does the model end, and who is accountable?

The final year braids the strands. The learner audits a public argument, audits a machine answer, analyses strategic communication, and defends a model's boundary in public. The capstone is not a new topic. It is the whole band, performed.

## The public argument audit

**Question.** Can I take a public argument apart without taking it personally?

**Do.** Choose a live argument: a budget, a climate policy, a court judgment, a school rule. Reconstruct it in standard form. Find the hidden premise. Find the missing comparison. Find the interest. Write a verdict that separates *valid*, *sound* and *persuasive*. Then write the strongest version of the other side.

**Words.** audit, reconstruction, hidden premise, comparison, interest, valid, sound, persuasive, steelman.

**Evidence.** The audit, with a steelman of the opposing view.

**Out of bounds.** Do not require neutrality. Require fairness: the strongest version, not the easiest.

## The machine audit

**Question.** What is a machine answer worth?

**Do.** A machine answer to a real question with consequences: a medical summary, a legal memo, a credit decision, a hiring shortlist. The learner fills a five-row audit: claim, chain, missing premise, confidence, accountable person. Then she writes a use decision: *use*, *use with a named check*, *do not use*. The check must be executable by someone.

**Words.** claim, chain, missing premise, confidence, calibration, accountability, use decision, check.

**Evidence.** The five-row audit and the use decision. This is the band artefact.

**Out of bounds.** Do not teach model architecture. Do not accept "the AI is biased" as an audit. Name the bias, the group and the consequence.

## Cooperation and strategy

**Question.** Is this speaker trying to help me understand, or trying to make me agree?

**Do.** Three transcripts: a scientist explaining uncertainty, a politician answering a different question, a salesperson using a true but incomplete comparison. The learner marks the purpose, the maxim most exploited, and the evidence that the speaker is not cooperating. Then the hard case: a speaker who is cooperating and still wrong.

**Words.** cooperation, strategy, purpose, exploit, relevance, omission, frame, accountability.

**Evidence.** The learner marks the purpose and the exploited maxim in three transcripts.

**Out of bounds.** Do not teach the full Gricean calculus. The audit questions are enough.

## Implicature in public argument

**Question.** How does a speaker mean something and deny it?

**Do.** Three cases: a dog whistle, a euphemism, an omission. For each: what is said, what is meant, what is the evidence for the meaning, what does the speaker gain from deniability? Then the learner writes a paragraph that makes the implicature explicit without overclaiming. The paragraph must survive the reply *I never said that*.

**Words.** dog whistle, euphemism, omission, deniability, implicature, audience, evidence, overclaim.

**Evidence.** The learner writes one explicit paragraph and one reply to the deniability defence.

**Out of bounds.** Do not teach the full taxonomy of implicature. Do not let the learner attribute an intention without evidence. The evidence can be the audience, the context, the pattern, or the speaker's other statements.

## The capstone: the limit of the model

**Question.** Where does my model stop being a model of the world?

**Do.** The learner chooses a model she has built: a Prolog program, a statistical analysis, a policy, a decision tool. She writes a one-page boundary note with four boxes: *what it knows*, *what it derives*, *what it cannot know*, *what it cannot decide*. Then she writes the decision the model supports and the decision it does not support. The note is the capstone.

**Words.** model, boundary, knows, derives, cannot know, cannot decide, supports, does not support.

**Evidence.** The one-page boundary note and the two decisions. This is the capstone.

**Out of bounds.** Do not require a novel model. A small model with a sharp boundary is better than a large model with a vague one.

## The defence

**Question.** Can I defend the boundary in five minutes?

**Do.** The learner presents for three minutes, then answers three questions for two minutes:

1. What does your model not know?
2. What would change your conclusion?
3. Who is accountable if it is wrong?

The class audits with the four-box sheet. The teacher models a weak defence first: the learner who says "it is only a model" and cannot name the edge. Then a strong defence: the learner who names the missing fact, the assumption and the owner. The learner revises the boundary note after the defence.

**Words.** defence, boundary, assumption, change my mind, accountable, revise, limit.

**Evidence.** The defence, the class audit, and the revised note.

**Out of bounds.** Do not grade confidence. Grade the named boundary and the named owner.

## The defence protocol

Use the same five steps every time.

1. **Three minutes, no slides.** The model, the claim, the boundary.
2. **Three questions, in order.** Not knowing, changing, accountability.
3. **One clarification.** The presenter may ask one question back.
4. **Class audit.** Four boxes, one sentence each.
5. **Revision.** The presenter rewrites one box of the boundary note.

The protocol is the assessment. A learner who can name the edge under pressure has the band. A learner who can only present the model has a demonstration.

<!-- part: Part II — Teaching and assessment -->

# 4. A scripted lesson: the defence

**Year 3, unit 3.6. Time: 55 minutes. Group: 20 learners.**

**Question.** What makes a defence of a model credible?

**Materials.** Two boundary notes, both about the same small program. A four-box audit sheet. A timer.

## ^ Minute 0–5: the setup

> **Teacher:** Today we are not building anything. We are defending. A model without a boundary is a sales pitch. A model with a boundary is a tool.

The teacher shows the program: a rule base that decides whether a learner may borrow a laptop. Three facts, two rules, one query.

## ^ Minute 5–15: the weak defence

The teacher plays a student. She presents the program confidently.

> **Weak presenter:** This program decides who can borrow a laptop. It has three facts and two rules. It works. Any questions?

The class asks the three questions.

> **Class:** What does it not know?
>
> **Weak presenter:** It is only a model. It does not know everything.

The teacher stops the role-play.

> **Teacher:** What is wrong with that answer?

The class says: it names no fact. It is a shrug in a sentence. The teacher writes the weak answer on the board and labels it *the blanket*. The blanket is the most common defence and the least useful.

## ^ Minute 15–30: the strong defence

The teacher presents the same program again, with a boundary note.

> **Strong presenter:** This program decides who may borrow a laptop. It knows three facts: the learner is enrolled, the learner has no outstanding loan, and the learner has a signed form. It derives *may borrow* when all three hold. It cannot know whether the learner needs the laptop for a lesson, because that fact is not in the program. It cannot decide whether to make an exception, because that is a judgement, not a rule. If the school changes the loan policy, the program will keep giving the old answer until the facts are updated. The person accountable for an exception is the head of year, not the program.

The class audits the defence against the four boxes. The teacher asks: which sentence was the boundary? Which sentence was the owner? Which sentence was the assumption?

## ^ Minute 30–42: the swap

Pairs take a model they have built. Each presents for three minutes; the partner asks the three questions and fills the audit sheet. The presenter must name one fact, one assumption and one owner. If she cannot, the partner points to the box that is empty.

## ^ Minute 42–50: the revision

Each learner rewrites one box of the boundary note. The revision must be a sentence that could be false. *It does not know everything* cannot be false in a useful way. *It does not know whether the learner needs the laptop for a lesson* can.

## ^ Minute 50–55: the exit ticket

> Write the one sentence you would say if a senior leader asked, "Can we trust this model?"

The strong answer has three parts: what it does, what it does not do, and who decides. The teacher collects the tickets and reads three aloud. The class says which part is missing from each.

## ^ What the teacher watches for

- A learner who says "it depends" without saying *on what* has the shape of a boundary and not the content. Ask: on which fact?
- A learner who says "the model is biased" without naming the group and the consequence has a slogan. Ask: for whom, and what happens?
- A learner who says "a human is responsible" without naming the human has moved the problem. Ask: which human, and what check?

## ^ What not to do

Do not let the defence become a presentation of the model. The model is already built. The defence is about the edge. Do not reward confidence. Reward the named fact, the named assumption and the named owner.

# 5. Assessment

## The three artefacts

**The proof and the countermodel.** One sentence, proved valid in one reading and shown invalid in another, with both models drawn. The learner writes what the proof establishes and what it does not.

**The program and the base-rate analysis.** A small Prolog program with recursion, a list, a cut and negation. A trace. A boundary note. A separate base-rate analysis with a natural-frequency table and an absolute-risk statement.

**The capstone.** A one-page boundary note and a five-minute defence. The note has four boxes. The defence answers the three questions. The learner revises one box after the defence.

**The machine audit.** A five-row audit of a real machine answer, with a use decision and a named check.

## The gate descriptors

| Gate | The learner can... | The evidence |
|---|---|---|
| 8 | test validity and construct a countermodel | the table and the drawn countermodel |
| 8 | distinguish validity from soundness | the two-part verdict on a real argument |
| 8 | explain what a proof does not establish | the four-step proof and the sentence beside it |
| 9 | write and trace a recursive program | the trace tree and the base case |
| 9 | explain the cost of cut | one query whose meaning changes |
| 9 | explain a stable model | two answer sets for one program |
| 9 | calculate a posterior from a base rate | the natural-frequency table |
| 9 | distinguish correlation from intervention | the causal diagram and the intervention |
| 9 | audit a machine answer | the five rows and the use decision |
| 9 | defend a boundary | the three answers and the revised note |

## Moderation

Two teachers, one artefact, blind. Each writes one sentence: what the learner can do, and what she cannot yet do. If the sentences disagree, the task is ambiguous. Fix the task.

## What not to assess

Do not assess the length of the program. Do not assess the speed of the defence. Do not assess whether the learner is optimistic or pessimistic about technology. Assess the chain, the boundary and the owner.

# 6. Common errors, and what to do

| What the learner says | What it means | What to do |
|---|---|---|
| "It's valid, so it's true." | Validity and truth collapsed | The rich-teacher argument; valid form, false premise |
| "The proof proves the premise." | The direction of the proof confused | Change one premise; the proof still works, the conclusion fails |
| "The table has no false row, so the premise is true." | The table tests form, not fact | Check the premise against a source |
| "The test is 99% accurate, so the positive is 99% likely." | Base rate ignored | The 10,000-person table; count the false positives |
| "Ice-cream sales cause drowning." | Correlation read as intervention | The confounder; ask what a change would do |
| "The machine is unbiased because it is maths." | The model treated as neutral | Ask who chose the data and the target |
| "The machine said it, so it must be neutral." | Fluency read as fairness | The five-row audit; name the training distribution |
| "Cut is better because it is faster." | Speed read as quality | Show the query whose meaning changed |
| "It is only a model." | The blanket defence | Ask: which fact does it not know? |
| "A human is responsible." | Responsibility moved, not named | Ask: which human, what check, what record? |

## The one error to pre-empt

**The model is the world.** It appears as *the test says so*, *the algorithm decided*, *the data speaks for itself*, *the map is the territory*. The correction is a sentence the learner will need in every institution she enters: **the model is a map; the map has an edge; someone drew it.**

# 7. Out of bounds

| Not this | Why not yet | Where it enters |
|---|---|---|
| Completeness and soundness proofs | The proof would replace the use | University |
| Graduate model theory | The definition would replace the defence | University |
| Modal and temporal logic | The vocabulary would arrive before the need | University |
| The full probability calculus | The formula would replace the table | University |
| Machine-learning engineering | The tool would replace the audit | University or industry |
| The full Gricean taxonomy | The labels would replace the audit questions | University |
| An unsupervised AI system | The audit must be taught before the tool is used | Work and adult life |

## The two prohibitions that matter most

**No proof without a premise check.** A learner who can prove validity and cannot check a premise has learned half the standard. The other half is the source.

**No machine audit without an owner.** A learner who can list the model's limits and cannot name who is accountable has moved the problem, not solved it.

# 8. What a school needs to provide

## Time and space

One 55-minute lesson per week, 36 weeks a year. A room with a board, a projector and space for pair defence. A folder of real public arguments and real machine answers, refreshed each term.

## Materials

- A set of truth-table and countermodel sheets.
- One computer per pair for Prolog and ASP, with a teacher account.
- A class set of the five-row machine audit.
- A timer for the defence.
- A folder of anonymised machine answers, with the source and date recorded.

## People

One teacher per class, with two days of training: one on validity and models, one on Prolog, base rates and the audit. The teacher does not need to be a software engineer. She needs to be able to read a trace, count a table and ask the three questions.

## What success looks like

A learner reads a policy and asks, "What is the hidden premise?" A learner reads a statistic and asks, "What is the denominator?" A learner uses a machine and asks, "What is the chain, and who is accountable?" Those three questions are the band. They are also the citizen.

# ^ References

## ^ The standard

- Grice, H. P. "Logic and Conversation." In *Syntax and Semantics 3: Speech Acts*, edited by P. Cole and J. L. Morgan, 41–58. New York: Academic Press, 1975. The Cooperative Principle, the maxims and implicature.
- "Implicature." *Stanford Encyclopedia of Philosophy*, revised 2024. https://plato.stanford.edu/entries/implicature/. Conversational implicature, flouting, cancellability, and the distinction from entailment and presupposition.

## ^ Project sources

- *From Naming to Doubting: a concept ladder for logical reasoning and critical thinking, ages 4 to adult.* Version 2, November 2026. Stages 8–12, 15 and gates 8–9.
- *GROUP 3) HIGH SCHOOL.* Project brief, including the 14–18 band.
- *GROUP 4) UNIVERSITY, or POST-SECONDARY.* Project brief, for the transition.
- *The Glass Box: overview and map.* CURR-OVERVIEW-001.

## ^ Logic and argument

- Van Cleave, M. J. *Introduction to Logic and Critical Thinking,* version 2.0. Chapters 1 and 4.
- Open Logic Project. https://openlogicproject.org. Truth tables, quantifiers, natural deduction.
- Toulmin, S. *The Uses of Argument.* Cambridge: Cambridge University Press, 1958.
- Kahneman, D. *Thinking, Fast and Slow.* New York: Farrar, Straus and Giroux, 2011. Base rates and representativeness.
- Gigerenzer, G. *Reckoning with Risk.* Penguin, 2002. Natural frequencies, which is why the band counts people before it uses a formula.

## ^ Logic programming

- Arias, J. *Logic Programming.* https://hdl.handle.net/10115/41543. The formal spine: unification, SLD, semantics.
- SWI-Prolog. https://www.swi-prolog.org. The reference implementation for Prolog, CLP(FD) and tabling.
- s(CASP). https://github.com/joaomoura/sCASP. Answer sets and justifications.
- Clocksin, W. and Mellish, C. *Programming in Prolog.* Springer, 2003.
- O'Keefe, R. *The Craft of Prolog.* MIT Press, 1990. Modes, determinism and the cost of cut.

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

The design archive is `Curriculum_Plan_Logic_Programming.pdf`. It contains the full stage cards and the seventeen-stage ladder. It is not required for teaching this band.
