# An Introduction to Logical Thinking

## at College/University Level

by the PEG

with Suggested Themes, Root Questions and Supporting Examples

**Version 2 — November 2026.** Supersedes the September 2026 sketch. Every theme and every worked example from v1 is preserved; what changes is the order, and three additions. The map from v1 to v2 is in the Appendix.

This sketch is the conceptual companion to the two T4 course volumes, `T4_CS_Logical_Thinking_and_Logic_Programming.pdf` and `T4_GEN_Logic_Evidence_and_Machines.pdf`. The teachable school sequence is in the four band documents, `G1-3_Foundations.pdf`, `G4-6_Rules_and_Search.pdf`, `G7-9_Critique.pdf` and `G10-12_Judgement.pdf`. The map of the whole set is `00_Overview_and_Map.pdf`. The sketch keeps its original form; the course volumes are where the weekly plans, labs and rubrics live.

---

## 0. What changed, and why

Five changes. Each is an **ordering** decision, not a change of content.

1. **Two units added at the front.** *U0 Epistemics: how you know* and *U2 Models, lightly*. The course asks "how do you know?"; a course that answers it only for arguments, and never for premises, produces graduates who can dissect an argument and still be fooled by a confident source.
2. **Model theory is spiralled.** A light version at U2 — so that "valid" can be *defined* rather than memorised — and the full version at U7, where v1 already had it. Same logic as the school ladder: three passes, never formal first.
3. **Common-sense reasoning moves to the end of the core (U9).** It is the unit the whole course builds toward, and the direct heir of the "hidden assumptions" work the children do at ten.
4. **Three capstones added:** fallacies and argumentation, uncertainty and causal reasoning, and AI and the proof obligation. They can run as a second semester.
5. **One production task per unit.** v1 listed root questions and worked examples but not what the student *makes*. Recognition is not the skill: a student can nod at a validity proof and still be unable to write a paragraph that survives one.

One root question is amended. v1 asked *"Why must all arguments be valid?"* Read literally, that asserts something false — inductive arguments are not valid, and they are indispensable. The intended question is the better one: **"Why does validity matter — and when is it the wrong standard?"** That is the gateway to induction, abduction and strength, which the same unit already teaches.

---

## 1. The sequence at a glance

Ten core units, then three capstones.

| # | Unit | Gate | Production task |
|---|---|---|---|
| U0 | Epistemics: how you know | 7 | Audit three sources on one claim; state what would change your mind |
| U1 | Logic in effective communication | 3, 5, 6 | Reconstruct a real argument in standard form; attack it and defend it |
| U2 | Models, lightly | 8 | Draw a model that makes a given argument invalid |
| U3 | Problem solving, goals, backward reasoning | 4, 5 | Specify a goal and derive a plan backwards from it |
| U4 | Search and non-determinism | 5 | Compare two strategies on one problem; show where one loops |
| U5 | Forward reasoning, condition/action rules | 4 | Build a small production system; defend its rule order |
| U6 | Hypothetical reasoning and abduction | 6, 7 | Rank three explanations by explicitness, not taste |
| U7 | Semantics: an introduction to model theory | 8 | Prove validity and invalidity for the same sentence, both ways |
| U8 | Temporal logic and action theories | 8 | Model a changing world; find the frame problem in your own model |
| U9 | Common-sense reasoning and non-monotonicity | 7, 8 | List the hidden assumptions in a policy; withdraw one and re-derive |
| C1 | Fallacies and argumentation | 6 | Transpose a real argument; show what survives the transposition |
| C2 | Uncertainty, risk and causal reasoning | — | Base rates, sensitivity, correlation vs. intervention, decision under risk |
| C3 | AI and the proof obligation | 9 | Take a machine answer apart; produce the chain or refuse the claim |

---

## 2. Core units

### U0. Epistemics: how you know

**Theme.** Before arguments, sources. Where beliefs come from, and how to rank them.

**Root questions.** What is it to know something, as opposed to believing it? What makes a source good? Is expertise different from authority? What is the difference between "I disagree" and "you are lying"? What would change your mind?

**Why here.** Unit 1 teaches students to evaluate an argument while leaving its *inputs* unexamined. That is the gap through which confident nonsense enters — and it is the one gap that an intelligent person is least protected against, because intelligence is better at defending a premise than at checking one.

**Production task.** Take one contested claim. Find three sources. Rank them, justify the ranking, and state precisely what evidence would move each one down.

**Supporting examples.** To be built. Suggested: two reports of the same event from opposed outlets; a Wikipedia article and the primary source it cites; an expert who is right in one domain and out of it in another.

**Prolog / LE support.** None. This unit is deliberately tool-free.

---

### U1. Logic in effective communication

**Theme.** The logical forms behind natural language.

**Root questions.** What is Logic? What is it good for? What is an argument? How do you identify the conclusion of an argument? What are the parts of an argument? How does one know an argument is valid? **Why does validity matter — and when is it the wrong standard?** What is falsifiability, and why is it so important for science? What is induction? What is deduction? What is abduction?

**Why here.** This is the unit that gives the course its vocabulary, and it should come early — but it must not be the *first* thing, because validity presupposes a notion of model (U2) and argument evaluation presupposes a notion of source (U0).

**The four skills.** The unit should aim at four things, not two:

|  | **Valid** | **Invalid** |
|---|---|---|
| **Good argument** | sound deductive | **strong inductive** |
| **Bad argument** | **valid but false premise** | fallacy |

The two bold cells are the ones students most need. *Invalid but good* (induction, abduction, most of medicine and history) stops them despising ordinary reasoning, or dressing it up as deductive. *Valid but bad* stops them trusting confident reasoning, because a valid argument from a false premise is the most persuasive lie there is.

So: (1) recognise when an argument *claims* deductive force; (2) make such arguments valid; (3) detect invalid ones and see what went wrong; (4) recognise when validity is **not** the right standard, and switch to strength, evidence and base rates.

**The Gricean layer.** Standard form reconstructs what was said. It does not reconstruct what was meant. Grice's Cooperative Principle — make your contribution such as is required by the accepted purpose of the exchange — and its maxims of Quality, Quantity, Relation and Manner give the missing theory. An implicature is a meaning conveyed without being said: the referee who mentions only handwriting means that the candidate is poor at philosophy. The inference is calculable from the words, the situation and the assumption of cooperation, and it is cancellable.

The layer matters here for three reasons. It explains why a warrant can be communicated and denied. It explains how a true sentence can mislead through omission. And it gives the audit question for a machine answer: what would the speaker have to know, and how would she know it? Add one session to U1 on the said/meant distinction, and return to it in C1 and C3.

**Production task.** Find a real argument from a newspaper, a policy document or a court judgment. Put it in standard form. Attack it. Then defend it against your own attack.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=rkBook/underground_emergency
https://lps2.logicalcontracts.com/ide?example=rkbook/underground

**Prolog / LE support.** The `underground` examples let the class see an argument's *form* made explicit and checkable before any notation is introduced.

---

### U2. Models, lightly

**Theme.** What it means for a sentence to be true, and for an argument to fail.

**Root questions.** What would have to be true for this to be false? Can you draw a world where the premises hold and the conclusion fails? What is the difference between "I cannot see how it could fail" and "it cannot fail"?

**Why here.** This is the unit v1 did not have, and its absence is why "valid" has to be memorised in Unit 1 rather than understood. Validity is *truth in every model*; a countermodel is the picture of a failure. Both fit on one side of paper, and both make Unit 1's central question answerable.

This is a **light** pass: pictures, tables, small finite worlds. The formal treatment is U7.

**Production task.** Given a valid argument, draw the (empty) set of countermodels and explain why it is empty. Given an invalid one, draw the countermodel.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=propositional

**Prolog / LE support.** The propositional example gives a machine-checkable notion of "true in a model" that the class can interrogate.

---

### U3. Problem solving, goals and backward reasoning

**Theme.** Logic programming and resolution, introduced as a way of *planning*.

**Root questions.** What is a problem? What is a goal? What types of goals are there? What is a conditional goal? What is a refutation? What is the difference between goals and beliefs?

**Why here.** With rules (U1) and models (U2) in hand, the student can ask the question that organises the rest of the course: *given what I want, what would have to be true?* Backward reasoning is the procedural face of the same idea.

The distinction between **goals and beliefs** is the hinge of the unit and deserves more time than the rest of it. A belief is a claim about the world; a goal is a claim about a world we want. Confusing them is the most common error in professional reasoning, and it is the seed of wishful thinking.

**Production task.** Specify a goal formally. Derive a plan backwards from it. Identify which steps are beliefs and which are choices.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=rkBook/fox_and_crow
https://le2.logicalcontracts.com/editor/index.html?example=rkBook/behaviourist_fox
https://lps2.logicalcontracts.com/ide?example=rkbook/fox_crow

**Prolog / LE support.** The fox and crow examples are ideal: the goal is explicit, the beliefs are explicit, and the failure is instructive.

---

### U4. Search and non-determinism

**Theme.** What a search space is, and what a strategy costs.

**Root questions.** What is search? What do you need to know before searching? Can we search in our heads? What is a search strategy?

**Why here.** Backward reasoning generates choices; search is what you do with them. This unit is also where students first meet the difference between **finding an answer** and **having found them all** — the school ladder's gate 5, at professional resolution.

**Production task.** Run two strategies on the same problem. Show where one loops and the other terminates. Then say which you would ship, and why.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=enclosure
https://le2.logicalcontracts.com/editor/index.html?example=royal_family
https://le2.logicalcontracts.com/editor/index.html?example=language%2Fmemoization%2Ffamily_relatives&line=23&scenario=tudors&query=relatives&answer=1

**Prolog / LE support.** The family-relations example is the best vehicle in the set: the search space is familiar, the branching is visible, and the same query can be run with and without memoization.

---

### U5. Forward reasoning and condition/action rules

**Theme.** Production systems: what happens when the rules fire rather than being called.

**Root questions.** What is a production system? When two rules could fire, which one should? What happens when a rule fires twice?

**Why here.** The mirror image of U3. Students who have only done backward reasoning believe that reasoning is goal-directed; most of the world's automated reasoning is not. Seeing both makes the choice between them a *design* decision rather than a fact of nature.

**Production task.** Build a small production system. Defend its conflict-resolution order. Then break it by adding one rule.

**Supporting examples.**
https://lps2.logicalcontracts.com/ide?example=rkbook/fox_crow
https://lps2.logicalcontracts.com/ide?example=rkbook/hunger
https://lps2.logicalcontracts.com/ide?example=rkbook/louse

**Prolog / LE support.** `hunger` and `louse` are compact enough to trace entirely by hand before running them.

---

### U6. Hypothetical reasoning and abduction

**Theme.** Reasoning to the best explanation.

**Root questions.** What is a hypothesis? What is an axiom? What makes one explanation better than another — and is "better" one thing or several?

**Why here.** Everything so far has assumed the rules are given. This unit asks where rules come from when they are not given, which is the normal condition of professional life.

The unit must end with **criteria**, not with admiration for abduction: explicitness, parsimony, testability, fit with what else we know. Without criteria, "inference to the best explanation" is a licence to believe what one likes.

**Production task.** Three explanations for one observation. Rank them. Justify the ranking by named criteria, not by taste. Then say what evidence would demote the winner.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=abduction/grass_is_wet
https://le2.logicalcontracts.com/editor/index.html?example=abduction/sunglasses
https://le2.logicalcontracts.com/editor/index.html?example=abduction/diagnosis
https://le2.logicalcontracts.com/editor/index.html?example=abduction/loan_approval

**Prolog / LE support.** `grass_is_wet` and `sunglasses` are the two that make the criteria visible; `diagnosis` and `loan_approval` show what happens when the criteria conflict.

---

### U7. Semantics: an introduction to model theory

**Theme.** Meaning, interpretation, model — the full pass.

**Root questions.** How does one explain meaning? What is an interpretation? What is a model? What is the difference between a model and the world?

**Why here.** This is the deepening of U2, and it belongs after the student has used models informally for five units. The formal definitions now compress experience rather than replacing it.

**The point of the unit** is gate 8: a model is a map, and soundness and completeness are properties *of the map*. A student who can say "this derivation is valid and its premise is false" without discomfort has the unit. A student who experiences every valid argument as a fact does not, and will be worse to argue with than an untrained one.

**Production task.** Take one sentence. Prove it valid in one reading and invalid in another, with both models drawn.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=propositional

**Prolog / LE support.** The propositional example, revisited: what was a truth-table exercise in U2 is now a question about the space of interpretations.

---

### U8. Temporal logic and action theories

**Theme.** Describing a changing world; situation calculus and event calculus compared.

**Root questions.** How do you describe a changing world? How do the situation calculus and the event calculus compare? What stays true when something changes, and how do you know?

**Why here.** Every previous unit assumed a static world. This one introduces time, and with it the **frame problem** — the question of what does *not* change, which is invisible until you try to write it down.

**Production task.** Model a small changing world in both calculi. Identify, in your own model, one thing you assumed would stay true and did not state.

**Supporting examples.**
https://lps2.logicalcontracts.com/ide?example=rkbook/event_calculus
https://lps2.logicalcontracts.com/ide?example=rkbook/citizenship_time

**Prolog / LE support.** `citizenship_time` is the strongest example in the whole set for a law or policy audience: the rule is real, the time-dependence is real, and the derivation is auditable.

---

### U9. Common-sense reasoning and non-monotonicity

**Theme.** Rational assumptions, defaults, and the hidden premises of ordinary reasoning.

**Root questions.** What is a rational assumption? What are the most common hidden assumptions in arguments? What are the most common hidden assumptions in arithmetic? What happens to my conclusions when I learn something new?

**Why here, and why last.** This is the capstone of the core, and it is the direct heir of the "ghost rule" exercise the children do at ten: *write down what they did not say, then judge the ghost.* At university resolution the same move is called non-monotonic reasoning, and it carries a technical consequence — conclusions are defeasible, and a knowledge base must be revisable.

**Production task.** Take a real policy. List its unstated assumptions. Withdraw one. Re-derive. Report what breaks — and whether the policy should have broken.

**Supporting examples.**
https://le2.logicalcontracts.com/editor/index.html?example=happy_dragon

**Prolog / LE support.** `happy_dragon` is the gentlest possible entry to a hard idea, which is exactly what is needed at the end of a long course.

---

## 3. Capstones

### C1. Fallacies and argumentation

**Theme.** Bad arguments as a subject, not an anecdote.

**Root questions.** Why is this fallacy seductive? What would the argument look like if it were good? Which fallacies are only fallacies in some contexts?

**Why a capstone.** Students need the whole apparatus first — models, counterexamples, hidden premises — or the fallacy names become a vocabulary quiz and then a debate tactic. This unit should be taught with the **transposition** technique: replace the content-carrying terms, preserve the form, and see what survives.

**Production task.** Take a real argument you find persuasive. Transpose it. Report honestly whether you still find it persuasive.

---

### C2. Uncertainty, risk and causal reasoning

**Theme.** The unit v1 did not have, and the one most likely to matter in professional life.

**Root questions.** What is a base rate, and why does it dominate? What is the difference between correlation and intervention? What does "probably" commit me to? How should I decide when I cannot know?

**Why it matters.** A logically impeccable argument from a base rate of 0.3% is still a bad decision. No amount of validity fixes a bad input, and this is the unit where the course stops being about arguments and starts being about judgement.

**Production task.** One decision under uncertainty. State the base rate, the evidence, the sensitivity of the conclusion to each assumption, and the decision rule you would defend in public.

---

### C3. AI and the proof obligation

**Theme.** What a machine answer is, and what it is not.

**Root questions.** When is a fluent answer evidence? What is the difference between a derivation and an output? Who is responsible for a delegated decision? What can a model not tell you about itself?

**Why a capstone.** It is gate 9, and it is the reason the course exists in its present form. Every failure mode of a generative system maps onto a unit the student has already done: hallucination is U1 and U7; sycophancy is C1; the closed-world error is U9; bias is U7 applied to rules rather than to the world.

**Production task.** Take one machine answer to a real question. Reconstruct its chain or refuse the claim. Then state what you would have to check, and who would have to check it.

---

## 4. Notes on ordering

**Why models come before validity is defined.** Validity is truth in all models. Teaching the definition first and the idea later is the standard mistake, and it produces students who can recite the definition and cannot find a counterexample.

**Why U9 is last.** Non-monotonicity is only interesting once you have built something that works and then watched it break. Taught early, it is a curiosity; taught last, it is a reckoning.

**Why the capstones are separate.** C1–C3 are integrative: each requires most of the core. Running them inside the core forces them to be taught before the material they integrate exists.

**What to keep from v1.** The root-question format — it is the best feature of the original sketch and should not be lost to a topic list. The worked examples, all of them, unchanged. And the ambition: a course for the general student, not only for computer scientists.

---

## 5. Assessment

Three components, weighted to match the four skills:

| Component | Weight | What it tests |
|---|---|---|
| Portfolio of production tasks | 40% | Can the student *make* the artefact, not just recognise it |
| Argument audit (transposition) | 30% | Can the student separate form from content under emotional load |
| Written examination | 30% | Validity, models, countermodels, soundness — the technical floor |

Plus one oral requirement, ungraded but compulsory: **explain one unit to a first-year student in five minutes.** If it cannot be explained simply, it has not been understood — and the exercise doubles as the near-peer mentoring pipeline the PEG mission asks for.

---

\newpage

## Appendix: map from v1 to v2

| v1 unit | v2 position | Change |
|---|---|---|
| 1. Logic in effective communication | U0 + U1 | Split; one root question amended |
| 2. Problem solving, goals, backward reasoning | U3 | Unchanged; production task added |
| 3. Search and non-determinism | U4 | Unchanged; completeness and looping made explicit |
| 4. Forward reasoning, condition/action rules | U5 | Unchanged; conflict resolution added |
| 5. Hypothetical reasoning, abduction | U6 | Unchanged; ranking criteria added |
| 6. Semantics, model theory | U2 + U7 | Spiralled: light pass early, full pass in place |
| 7. Temporal logic, action theories | U8 | Unchanged; frame problem made explicit |
| 8. Common-sense reasoning | U9 | Moved to the end of the core; elevated |
| — | C1, C2, C3 | New capstones: fallacies, uncertainty, AI |

## References

- Grice, H. P. "Logic and Conversation." In *Syntax and Semantics 3: Speech Acts*, edited by P. Cole and J. L. Morgan, 41–58. New York: Academic Press, 1975.
- "Implicature." *Stanford Encyclopedia of Philosophy*, revised 2024. https://plato.stanford.edu/entries/implicature/.
- *The Glass Box: overview and map.* CURR-OVERVIEW-001, November 2026. The set and the reading routes.
- *Logical Thinking and Logic Programming for Computer Science.* CURR-T4-CS-001. The computer-science course.
- *Logic, Evidence and Machines.* CURR-T4-GEN-001. The general course.
- *Foundations; Rules and Search; Critique; Judgement.* CURR-G1-3-001 to CURR-G10-12-001. The four school bands.
- *Judgement at Work.* CURR-ADULT-001. The post-college sessions.
