# From Naming to Doubting

## A concept ladder for logical reasoning and critical thinking, ages 4 to adult

### With notes on where Prolog helps, and where it gets in the way

**Version 2.** Prepared for all five curriculum groups
Companion to: *GROUP 1) ELEMENTARY SCHOOL*, *GROUP 2) MIDDLE SCHOOL*, *GROUP 4) UNIVERSITY*, *GROUP 5) OUTSIDE ACADEMIA*, and *An Introduction to Logical Thinking*

---

## 0. What this document does

Part I (sections 1–9) takes the Elementary and Middle School concept list and reorders it. Part II (sections 10–15) carries the same ladder past 18: the university track sketched in *An Introduction to Logical Thinking*, a Logic Programming track, the AI Literacy track Group 4 was asked to produce, and the out-of-school track Group 5 owns.

The whole thing rests on one claim, which is also the pedagogical continuity your mission asks for:

> **The concepts do not change as students get older. Their resolution changes.**

Implication at eight is a permission rule ("if you ride the bike, you must wear a helmet"). At fifteen it is a resolution step. At twenty it is a model-theoretic relation. At forty it is a clause in a contract you did not read. Same gate, four resolutions. A curriculum that respects this can hand a five-year-old, a nineteen-year-old and a parent the *same* idea without insulting any of them — which is what makes a single backbone possible across five groups.

Part I does four things to your list:

1. **Reorders it** according to what a child must be able to *discriminate* before the next concept can land. Ordering by vocabulary ("when do we say the word 'variable'?") produces fragile learning; ordering by discrimination ("when can the child tell a variable from a name?") produces durable learning.
2. **Splits two items that are currently carrying too much weight** — "Facts and rules, and some methods to judge their credibility" is really two different stages separated by two years, and "Implication" is really six micro-concepts of very unequal difficulty.
3. **Adds the concepts that are missing** and without which the rest does not compose into critical thinking: negation and the closed-world assumption, quantifiers, identity vs. similarity, explanation vs. argument, causation vs. correlation, uncertainty language, calibration, and dialogue norms.
4. **Says explicitly where Prolog should not go**, and why. Prolog is a superb mirror and a poor first teacher.

Part II adds three things: the two **adult gates** (model vs. world; derivation vs. output), the **university sequence** with its three tracks, and the **life track**, organised by situations rather than concepts. Section 16 gives the delta against the K–12 list, Section 17 the delta against the college sketch — both in one table each, for meeting use.

---

## 1. Six principles that generate the order

**P1. Order by discrimination, not by vocabulary.**
The teachable moment is not when a child can *say* "variable". It is when a child can *tell* a variable from a name — that is, when they can see that "Ana" picks out one girl and "someone" could pick out any. Every stage below is defined by one discrimination, and every stage has a failure symptom that tells you the child is not there yet.

**P2. Three passes per concept, never formal first.**
Each concept is met first in the body (enactive), then in a picture or diagram (iconic), then in words (verbal), and only then, if at all, in a formalism (symbolic). This is Bruner's triad, and it is also just good sense: a child who has physically walked a maze backwards knows something about backtracking that no amount of syntax will give them.

**P3. Construct before critique.**
You cannot reliably spot a broken rule until you can build a working one and watch it work. This is the reason for the one significant reordering I propose: **recursion moves earlier, and fallacies move later.** Fallacies are a *critique* skill. They need the full apparatus — counterexample, implicit premise, consistency check — which is Stage 8. Taught before that apparatus exists, fallacies degenerate into a vocabulary quiz ("that's an ad hominem!") which is itself a substitute for thinking.

**P4. Every concept must become a question the child asks themselves.**
The test of a concept is not that the child can define it. It is that the child spontaneously asks: *Does it follow? How do you know? What's missing? What would change my mind? Who benefits if I believe this?* Each stage below names the question it installs. This is also the bridge to critical thinking: logic gives you the questions, critical thinking is the habit of actually asking them when it costs you something.

**P5. Prolog is a mirror, not a syllabus.**
The value of Prolog in this curriculum is that it makes a child's own reasoning **visible, testable and revisable** — you write down what you know, ask a question, and the machine shows the chain. That is exactly the transparency that a chatbot denies. But Prolog also has quirks (depth-first search, negation as failure, the closed-world assumption, the cut) that are *not* logic and must not be mistaken for logic. The rule is:

> Never introduce a Prolog construct before the child can do the thing by hand, and can say when the program is **wrong about the world** rather than merely wrong about the answer.

**P6. Deduction preserves truth; it does not acquire it.**
Validity guarantees that *if* the premises are true, the conclusion is. It says nothing about whether they are. So deduction is necessary for certainty and never sufficient for it: the premises of every deduction are themselves obtained non-deductively — by observation, measurement, testimony, induction, or stipulation. The regress is unavoidable: to establish Γ deductively you need Γ′ ⊢ Γ, and to establish Γ′ you need Γ″ ⊢ Γ′, and the chain ends either in axioms (stipulated) or in non-deductive warrant. **The last step of every establishment is non-deductive.**

Two consequences shape the curriculum. First, induction and abduction are taught as first-class reasoning (Stage 10, C2), not as creativity exercises, because they are where every empirical premise comes from. Second, gate 8 matters: deduction establishes truth *in a model*, and the adequacy of the model to the world is not a deductive question. The honest asymmetry is that **deduction establishes falsehood outright** (modus tollens) and establishes truth only relative to premises it did not establish.

---

## 2. The nine gates

The whole ladder can be compressed into nine discriminations. A student who has all nine can be taught formal logic quickly and will use it. A student missing one will memorise the formalism and drop it at the first exam.

| Gate | The discrimination | Age | Failure symptom if skipped |
|---|---|---|---|
| 1 | **Thing vs. name for the thing** | 5–7 | Confuses the map with the territory; thinks defining a word settles a fact |
| 2 | **Thing vs. slot for a thing** | 6–8 | Cannot ask a general question; treats "someone" as a particular person |
| 3 | **Describing vs. claiming** | 6–9 | Cannot separate "what it is like" from "whether it is so" |
| 4 | **Adding vs. conditioning** ("and" vs. "if") | 8–10 | Treats a rule as a list; cannot see that a rule *generates* new facts |
| 5 | **Finding vs. proving** | 9–12 | Thinks the first answer found is the answer; cannot see that "I found one" ≠ "that's all there are" |
| 6 | **Following vs. feeling** | 10–14 | Accepts an argument because it is fluent, confident, or emotionally satisfying |
| 7 | **Saying vs. knowing** | 13–18 | Treats testimony, repetition and virality as evidence |
| 8 | **Model vs. world** | 16–22 | Confuses the formalism with reality; thinks a proof settles a fact about the world |
| 9 | **Derivation vs. output** | 15–adult | Accepts a conclusion because it was produced fluently, not because it was earned |

Gates 1–5 are *logic*. Gates 6–7 are *critical thinking*. Gates 8–9 are *the professional and civic gates*: they are what separates someone who has been taught logic from someone who can be trusted with it — and, in the age of generative AI, gate 9 is the one that decides whether a person can check a machine.

The curriculum is designed so that each gate is secure before the next is asked for. That is why the sequence runs from symbol to fallacy and not the other way round, and why the university units are ordered the way they are in Section 11.

**Gate 8 deserves a note.** It is the gate most often missing in adults who have studied logic, and it is the reason a formally trained person can be *worse* to argue with than an untrained one. A model is a map. Soundness and completeness are properties *of the map*, not of the world. Someone who has gate 8 can say "this derivation is valid and its premise is false" without discomfort. Someone who lacks it experiences every valid argument as a fact.

**Gate 9 is new in the age of AI, but it is not new in kind.** It is the old distinction between *having a reason* and *having a conclusion*, applied to a machine that produces conclusions at scale. Its childhood seed is the five-word request taught at Stage 5: **"show me the chain."**

Dependency graph (each arrow means "must be secure before"):

```
symbol -> object/property/relation -> variable+question -> fact & source
                                                                |
                                                                v
                 and / or / not -> rule (if) -> necessary vs sufficient
                                          |
                                          v
              chaining -> search & backtracking -> recursion
                                          |
                                          v
        consistency -> counterexample -> implicit premise
                                          |
                                          v
                              fallacies -> misinformation
                                          |
                                          v
                         model vs world -> derivation vs output
```

---

## 3. The master sequence, ages 4–18

Twelve stages. Each gives: the discrimination, why it sits here, the invariant to protect, the misconception to pre-empt, an unplugged activity, and the Prolog bridge (or the explicit reason there isn't one). Stages 13–16, for university and adult learners, are in Part II.

### Stage 0 — The ground floor (3–5) *(new; currently implicit)*

**Discrimination:** same vs. different; mine vs. yours; now vs. before.
**Why first:** sorting and classification are the perceptual substrate of predication. A child who cannot group by attribute cannot later attach a property to an object.
**Invariant:** grouping is a *choice* we make for a reason, not a fact in the world.
**Misconception to pre-empt:** that there is one "right" way to sort.
**Activity:** sort a heap of mixed objects; then be asked *why* you sorted that way; then be asked to sort the same heap a different way and defend it. Introduce the two magic sentences: **"I don't know"** and **"How do you know?"** — both must be safe to say.
**Prolog:** none. Not now, not soon.

### Stage 1 — Symbol (5–7)

**Discrimination:** the sign is not the thing. "A" is not a sound; it *stands for* one.
**Why here:** everything downstream is representation. A child who has not separated symbol from object will treat a definition as a discovery.
**Invariant:** symbols are arbitrary, conventional, and context-sensitive — and that is a feature, not a flaw.
**Misconception to pre-empt:** that a symbol has one fixed meaning. (The same letter sounds different in different words; the same word means different things in different sentences.)
**Activity sequence (in this order):**
1. *Icon, index, symbol.* A photo of a dog, a pawprint, the word "dog". Which one *looks like* the thing, which one *points to* it, which one is *just a convention*? This triad does more work than it looks like it does — it is the seed of the later distinction between evidence and testimony.
2. *The map is not the territory.* Draw the classroom; hide a sweet; the map tells you where it is but you cannot eat the map.
3. *Same symbol, different meaning.* Homonyms, emoji with two readings, a word that means one thing at home and another at school.
4. *Invent a symbol.* Let them make a sign for something in the room and teach it to another child. Convention is now something they have *done*.
**Prolog bridge:** atoms and quoted atoms; the difference between a name and what it names. But no Prolog yet — the bridge is only conceptual. (Later: why `'Mary'` and `mary` can be different things, and why that is a design decision, not a law of nature.)
**Out of bounds:** no syntax, no notation drills, no alphabet racing.

### Stage 2 — Objects, properties, relations (5–8)

**Discrimination:** a thing; a thing's attribute; a link *between* things.
**Why here:** this is the vocabulary of everything that follows. It is also where "math is numbers" and "logic is formulas" get unlearned — a family tree is a relation, and it is neither.
**Invariant:** properties take one thing; relations take two or more, and **the order matters**.
**Misconception to pre-empt:** that "bigger than" and "smaller than" are the same relation. They are the same *link* read in two directions. This single confusion, unaddressed, becomes the classic Prolog bug of swapped arguments at 15.
**Activity sequence:**
1. *Describe and guess.* One child describes an animal by properties only; the others guess. Then forbid properties and allow only relations ("it is next to the elephant", "it is bigger than the cat"). The moment properties are removed, the game gets harder — that difficulty *is* the lesson.
2. *Charades and cartoon titles* (your item): pure property-guessing with a yes/no channel. Keep it: it teaches the value of a good question, which Stage 3 needs.
3. *Invent a world* (Michael's suggestion): clothes, footballers, mythological beasts. Each child writes three objects, three properties, three relations. Their world is now a small database and they do not know it yet.
4. *Draw the relation.* Family tree, seating plan, "who sits next to whom" as a grid. Two pictures of the same relations: the tree and the table. Same information, different shape.
**Prolog bridge:** `has_feathers(tweety)`, `next_to(a, b)`. Arity as a word for "how many holes". Argument order as a real decision with real consequences.
**Out of bounds:** do not introduce variables yet. A relation with a hole in it is Stage 3.

### Stage 3 — The hole: variable and question, taught together (6–9)

**This is the one structural change I would press hardest.** Your list puts "variable" at position 2, before objects and relations. But a variable is *a hole in a pattern*, and you cannot have a hole before you have a pattern. Worse, teaching "variable" as a standalone idea ("a symbol standing for possibly different objects") produces the box-with-a-label metaphor, which is fine but inert — it does not tell the child what a variable is *for*.

Taught together with the question, it does:

> "X ate the cake" with a hole in it **is** the question "who ate the cake?"
> Answering the question **is** filling the hole.

**Discrimination:** a name picks out one thing; a hole could be filled by many, but **one hole, in one sentence, must be filled the same way twice**.
**Why here:** this is Gate 2, and it is the hardest of the early gates. It is also the exact place where children (and undergraduates, and chatbots) go wrong on "everyone loves someone".
**Invariant:** the hole is not a thing. It is a place where a thing can go.
**Misconception to pre-empt:** that "someone" means a specific someone you have in mind. Test it out loud: *"Someone in this room has a dog. Who?"* — the answer is not knowable yet, and that is the point.
**Activity sequence:**
1. *Boxes and contents* (your item, kept). A box, a label, contents. Now: a box *with a question mark on it*. What can you say about what is inside without opening it?
2. *Fill the blank.* Sentences with a gap; the same gap appearing twice must take the same filler. "___ is taller than ___" — can the same child fill both? Sometimes yes, sometimes no. That discovery is the whole idea of a variable.
3. *The two-someones game.* "A child gave a present to a child." One giver, one receiver — or the same child twice? Draw it. Then: "Every child gave a present to a child." How many drawings are possible?
4. *Pattern matching / unification, physically.* Jigsaw pieces: which piece *fits* this gap? Two gaps, one piece — does it fit both? This is unification, and it is a toy.
**Prolog bridge:** `likes(X, ice_cream)`, `X = Y`, `_`. The anonymous variable as "a hole I don't care about". Unification as "does this piece fit" — and the crucial asymmetry: a variable can be filled, an atom cannot.
**Out of bounds:** scope and quantifier nesting as a formal topic. Keep it at the drawing level until 10.

### Stage 4 — Facts, sources, and the third answer (7–9) *(split out of your combined item)*

**Discrimination:** a claim that can be checked vs. a claim that cannot (yet); and **"no" vs. "not in my list"**.
**Why here:** you cannot judge the credibility of a *rule* until you have judged the credibility of a *fact*. And you cannot trust a derivation built on unchecked inputs. Garbage in, garbage out is a critical-thinking idea, not a computing idea, and 8-year-olds get it instantly.
**Invariant:** knowledge is a list you can add to, remove from, and revise — and the list is never the world.
**Misconception to pre-empt:** the biggest one in the whole curriculum. **Absence of evidence is not evidence of absence.** A child who conflates "not in my list" with "false" will grow into an adult who confuses "I couldn't find it" with "it isn't so" — and into a Prolog programmer who does not understand negation as failure.
**Activity sequence:**
1. *Yes / no / not yet.* Three cards. Every question gets one of three answers, and "not yet" is a *good* answer, not a failure. Practise saying it.
2. *Who told you?* The same fact from a friend, a teacher, a stranger, a book, a website. Rank the sources, then find a case where the ranking flips (the friend was there; the website was wrong).
3. *The changing list.* A "what we know about the class" board. Add a fact, remove a fact, see what conclusions break. This is belief revision, done with magnets.
4. *Two lists, one world.* Two groups keep separate fact lists about the same thing. Where they disagree, who is right, and **how would you find out?**
**Prolog bridge:** facts as ground atoms; a query returning `true`, `false`, or **looping** — three answers, not two. Then the honest statement: *Prolog says `false` when it means "not in the program". That is not the same as "not true".* Say this out loud, early, and repeatedly.
**Out of bounds:** no formal source-evaluation rubric yet; no CRAAP-style acronyms before 11.

### Stage 5 — Rules and implication (8–10)

Six micro-concepts of very unequal difficulty. Teach them in this order; the order matters more than the content.

**5a. And.** Two things both have to hold. Easiest, and it is the shape of every rule body.
**5b. Or.** One or the other or both. *Inclusive* or. Do not introduce the exclusive or yet — let the ambiguity be discovered ("you can have ice cream or cake" — can you have both?).
**5c. Not.** The trickiest of the three, because it has two meanings that adults conflate constantly: *"it is false that"* and *"I have no evidence that"*. Keep them apart verbally from the start: "That's wrong" vs. "I don't know that."
**5d. If.** Introduce through **permission and obligation**, not through abstract conditionals. This is the single most useful empirical finding for this curriculum: children reason far more reliably about deontic rules ("if you ride the bike, you must wear a helmet") than about abstract ones ("if it is a vowel, it has an even number"). Use permissions, promises, and house rules as the entry point, and only much later move to descriptive conditionals.
**5e. Necessary vs. sufficient.** The highest-value distinction in the entire document, and it belongs in elementary school. A key is **necessary** to open the door; it is not **sufficient** (the door may be bolted). Wearing a helmet is necessary to ride; it does not make you safe. Practise with the two sentences: *"You need it, but it's not enough"* and *"It's enough, but you don't need it."* Children of nine can do this. Many adults cannot, and it is the root of most bad policy reasoning.
**5f. Chaining and the "why" chain.** A→B, B→C, so A→C. Then the crucial habit: when someone gives you a conclusion, ask **"show me the chain"**.

**Discrimination:** adding facts (and) vs. generating facts (if).
**Invariant:** a rule is a machine for producing new facts from old ones; the arrow does not run backwards.
**Misconception to pre-empt:** **"Just because A doesn't mean B"** — your own phrase, and the right one. Affirming the consequent is the most common reasoning error in the world, and it is best killed at eight, with a story: *If it rains, the ground is wet. The ground is wet. Did it rain?* (Sprinkler.) Let them find the counterexample themselves.
**Activity:** detective stories (Laura, Stefano's "Who ate the cake?"); CLUE; rule-card games where each card is a rule and the group derives who did it. Then **the explanation game**: one child states a conclusion, another must reconstruct the chain that produced it. If the chain can't be reconstructed, the conclusion doesn't count.
**Prolog bridge:** this is where Prolog starts to earn its place. `head :- body`. `,` for and, `;` for or, `\+` for not. And the demonstration that Prolog will *show the chain* — the proof tree is the "show me how you got there" made literal. Best first Prolog lesson there is.
**Out of bounds:** **material implication.** Do not teach "a false antecedent makes the conditional true" before 14. It is true, it is useless to a child, and it destroys the intuition you just built. Teach it later, explicitly, as a *stipulation* that logicians make for convenience.

### Stage 6 — Search and backtracking (9–11)

**Discrimination:** trying vs. finding vs. having tried everything.
**Why here:** backtracking is the first concept that requires rules to exist (you need choices to backtrack over) and the first that produces a genuinely new *feeling* — the "oh, I have to undo" feeling. It is also where Gate 5 lives.
**Invariant:** order of trying affects **speed**, not **correctness**. And: an answer found is not yet the answer.
**Misconception to pre-empt:** that the first path that works is the only path, or the best path.
**Activity sequence:**
1. *The maze, physically.* Your item, and it is exactly right. Walk it. Hit a wall. **Walk backwards to the last junction** — not to the start. The child's body learns "return to the most recent choice point", which is precisely what the trail does.
2. *Guess Who / 20 questions.* Every question is a choice point; every answer prunes a branch. Draw the tree as it happens.
3. *The undo rule.* Any game where a move must be *completely* undone — counters back, cards back in order, the board exactly as it was. Sloppy undo is the classic Prolog bug and it is a physical habit before it is a technical one.
4. *Have we tried everything?* Exhaustiveness. Give a small problem with a hidden extra solution; the group that stops at one answer loses. This is the birth of "are there other explanations?"
**Prolog bridge:** the strongest Prolog case in the whole curriculum. `;` in the shell, watching the engine go back and try again; `trace`/`debug` as a slowed-down maze walk; `repeat`, `fail`. Show that the program *undoes* bindings on backtracking, and connect it to the counters going back.
**Out of bounds:** the cut. Not before 14, and then only as an efficiency tool with a warning label.

### Stage 7 — Recursion (9–12) *(moved earlier)*

**Discrimination:** "the same shape again, but smaller" vs. "a different thing that happens to repeat".
**Why here, and why earlier than your list:** recursion is a **construction** skill, and construction must precede critique (P3). It also deepens the rule concept immediately — a recursive rule is the proof that rules generate rather than list. And it is the concept most often taught too late and too formally, when it is in fact the most child-friendly idea in logic, because children's culture is saturated with it.
**Invariant:** every recursion needs a **floor** — a case that does not call itself.
**Misconception to pre-empt:** that recursion means "repeating". Repetition is a loop; recursion is a *nest*.
**Activity sequence:**
1. *Nests.* Russian dolls; the song that never ends; a story within a story; "the house that Jack built". Ask: what is at the bottom?
2. *The ancestor question.* "Who is your ancestor?" — "My parent is my ancestor, and my parent's ancestor is my ancestor." Now ask: how far back does the question go, and what stops it? The base case appears as a *necessity*, not a technique.
3. *No floor.* Tell a rule with no base case and let them watch it run forever — physically, with a chain of children each passing the question to the next. The discomfort is the lesson. Then ask what is missing.
4. *Imbricated relative clauses* (your item): "the cat that chased the rat that ate the malt that lay in the house that Jack built". Grammar as recursion; no notation needed.
**Prolog bridge:** `ancestor(X, Y) :- parent(X, Y).` / `ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).` The two-clause shape — floor, then step — is the thing to internalise. Then the deliberate infinite loop, and the question: *what would you add?*
**Out of bounds:** accumulator pairs, tail recursion, complexity. Never.

### Stage 8 — Consistency, counterexample, implicit premise (10–13) *(split out of your combined item)*

**Discrimination:** "this conclusion is wrong" vs. "these beliefs cannot all be true at once".
**Why here:** this is the hinge between logic and critical thinking, and it is the stage your list compresses into the phrase "some methods to judge their credibility". It deserves its own two years. Everything in Stage 9 depends on it.
**Invariant:** a set of beliefs is a *system*; you test the system, not the sentence.
**Misconception to pre-empt:** that inconsistency is always a lie. Usually it is two rules that were each reasonable on their own.
**Activity sequence:**
1. *Can these all be true?* Give four statements, three of which cannot coexist. Find the pair that fights. No logic notation needed — just "these two can't both be so".
2. *Hunt the counterexample.* Someone states a rule. The job is not to disagree but to find **one case** that breaks it. "All birds fly." Penguin. "Everyone who is tall plays basketball." This reframes disagreement from identity to evidence, which is a social achievement as much as a logical one.
3. *The ghost rule.* Your item, and it is the best idea in the document. Listen to an advert, a politician, a family saying. Write down **what they did not say** — the premise that has to be true for the argument to work. Then judge the ghost: true, or just dogma? Start with adverts (easy, safe), move to family sayings (harder, personal), then to public speech.
4. *Debug the rule base, not the answer.* Wlodek's declarative-diagnosis idea, and it is excellent. Give the group a rule set that produces a wrong answer. Their task: **which rule is wrong?** Not "the answer is wrong" — *which belief is wrong*. This is the single best exercise I know for making reasoning an object of inspection rather than an identity.
5. *The two-column page.* Every activity produces: **What we know** | **How we know it**. Keep the pages. At the end of the year, the child has an epistemology.
**Prolog bridge:** `\+` used honestly; a program that is *internally* consistent but *externally* wrong; adding a fact and watching a previously-true conclusion die (non-monotonicity, met as an experience, not a term).
**Out of bounds:** truth tables, validity vs. soundness as formal definitions. The *ideas* are in play; the terminology waits.

### Stage 9 — Fallacies (10–14)

See Section 5 for the full tiered sequence. The headline: **teach each fallacy as a question, not a name.** The name is a souvenir you pick up after the visit.

### Stage 10 — Arguments in the wild (12–15) *(new)*

**Discrimination:** an argument vs. an explanation; correlation vs. cause; "probably" vs. "certainly".
**Why here:** by now the child can build and check a derivation. What they cannot yet do is *find the argument* inside a paragraph of prose, or notice that a confident sentence is smuggling a probability claim.
**Content:**
- **Argument vs. explanation** (Van Cleave, ch. 1.3). "Because he was late, he missed the bus" explains; it does not argue. This distinction is routinely missed by adults and is the backbone of resisting political rhetoric.
- **Claim / grounds / warrant / rebuttal** (Toulmin, informally). The warrant is the ghost rule by another name — good continuity with Stage 8.
- **Correlation vs. cause.** Ice cream and drowning. Then the three questions: could it be reversed? could a third thing cause both? is it coincidence?
- **Uncertainty language.** Always, usually, often, sometimes, never, probably, possibly. Sort a set of claims by strength. Then: *does the evidence support that strength?* This is the direct antidote to a chatbot's confident tone.
- **Steelmanning.** Before attacking, restate the other view so well that its holder says "yes, that's what I meant". Prerequisite for detecting straw men — you cannot see a distortion without a straight version.
- **Burden of proof.** Who claimed it, who must show it. "Prove me wrong" is not an argument.
**Prolog bridge:** encode two competing explanations as two rule bases and ask which one the facts support. Not a proof of causation — and saying so is part of the lesson.

### Stage 11 — Misinformation, trolling, manipulation (14–18)

See Section 6.

### Stage 12 — Formal consolidation (15–18) *(new)*

**Why last:** the formalism is now a *compression* of things they can already do, not a substitute for them. Taught here, it sticks; taught at 12, it is dropped at 13.
**Content:** truth tables; validity vs. soundness; quantifiers properly; the limits of classical logic; and Prolog as a *logic engine* with named limitations — closed world, negation as failure, depth-first incompleteness, non-monotonicity, the cut. The mature move is: **the machine is a model of reasoning, and every model has a boundary.** Ask them to find the boundary.

---

## 4. Master matrix

| Age | Stage and concept | Key discrimination | Core activity | Prolog |
|---|---|---|---|---|
| 3–5 | 0 · Sorting, naming, true/false | same vs. different | Sort the heap twice | — |
| 5–7 | 1 · Symbol | sign vs. thing | Icon / index / symbol | conceptual only |
| 5–8 | 2 · Object, property, relation | attribute vs. link; order matters | Describe-and-guess; invent a world | atoms, arity |
| 6–9 | 3 · Variable + question | name vs. hole | Boxes; fill the blank; two-someones | variables, `=`, `_` |
| 7–9 | 4 · Facts, sources, third answer | "no" vs. "not in my list" | Yes / no / not yet; who told you? | facts, `true`/`false`/loop |
| 8–10 | 5 · Rules: and, or, not, if, necessary/sufficient, chain | adding vs. generating | Permission rules; detective stories; the why-chain | `:-` (if), `,` (and), `;` (or), `\+` (not) |
| 9–11 | 6 · Search, backtracking | trying vs. exhausting | Maze walked backwards; undo rule | `;`, `trace`, undo |
| 9–12 | 7 · Recursion | nest vs. repeat | Russian dolls; ancestor; no floor | base + step clauses |
| 10–13 | 8 · Consistency, counterexample, ghost rule | wrong answer vs. wrong belief | Can these all be true?; debug the rules | `\+`, revision |
| 10–14 | 9 · Fallacies (tiered) | follows vs. feels | Name the trick; the killing question | rule base of a bad argument |
| 12–15 | 10 · Argument, cause, uncertainty | argument vs. explanation | Sort claims by strength; steelman | competing rule bases |
| 14–18 | 11 · Misinformation, trolling | saying vs. knowing | Walk a mile in the manipulator's shoes | manipulator's rule base |
| 15–18 | 12 · Formal consolidation | model vs. world | Truth tables; find the limit | limits of Prolog |
| 18–22 | 13 · University: logical thinking | validity vs. strength; model vs. world | Audit a real argument; debug a rule base | LE2, LPS2, Prolog |
| 18–22 | 14 · University: logic programming | convenience vs. distortion | Write and defend a program; declarative debug | Prolog, CLP(FD), s(CASP) |
| 16–adult | 15 · AI literacy *(cross-cutting)* | derivation vs. output | Ask for the chain; reframe twice | none needed |
| any adult | 16 · Life: thinking skills | situation vs. concept | A 20-minute logic bite | none |

---

## 5. Fallacies: a teachable order

Three rules before the list.

**Rule 1. Teach the generic detector first.** "It doesn't follow" — the non sequitur — is the only fallacy a child needs for two years. Everything else is a *species*. Children who learn species before the genus collect Pokémon instead of thinking.

**Rule 2. Every fallacy is a question.** The name is a label for a question the child already knows how to ask. If they can ask the question, the name is optional. If they only have the name, they have nothing.

**Rule 3. Order by the cognitive demand of the *detection*, not by textbook chapter order.** Detection difficulty depends on what the child must hold in mind simultaneously: one claim (easy), two claims in relation (medium), a whole argument plus its missing parts (hard), a statistical base (hardest).

| Tier | Ages | Fallacies | The question that kills it |
|---|---|---|---|
| 0 | 6–9 | Non sequitur (unnamed) | "So what? How does that get you there?" |
| 1 | 8–11 | Ad hominem; bandwagon; appeal to authority; appeal to emotion; tu quoque; appeal to consequences | "Is that about the claim, or about the person/feeling?" |
| 2 | 9–12 | False dilemma; hasty generalization; circular reasoning; straw man; slippery slope; composition / division | "Are there other options? / How many cases? / Is the premise just the conclusion again?" |
| 3 | 10–13 | Equivocation; ambiguity; loaded question; vagueness; weasel words; framing; euphemism | "Which word changed meaning halfway?" |
| 4 | 12–16 | Post hoc; cum hoc; regression to the mean; base rate; conjunction; gambler's; small numbers; survivorship; cherry-picking; misleading graphs | "Compared to what? / How often does this happen anyway?" |
| 5 | 14–18 | Decontextualisation; fabrication; impersonation; polarisation; scapegoating; whataboutism; false balance; astroturfing; outrage bait; Gish gallop; firehose of falsehood; AI confabulation | "Who made this, what do they want, and where is the original?" |

Notes on the ordering choices:

- **Ad hominem before appeal to authority.** Attacking the person is visible to a nine-year-old; judging expertise requires a theory of expertise. Do the easy one first, then use it to motivate the hard one — and make the point that *"who says it" is sometimes exactly the right question*, which is what stops "ad hominem" from becoming a thought-terminating cliché.
- **False dilemma very early.** Binary framing is the dominant failure mode of childhood reasoning and of public debate. It is also the easiest to dramatise: give two options, then ask who was left out.
- **Straw man only after steelmanning** (Stage 10). Otherwise the child learns the label and applies it to any disagreement.
- **Circular reasoning late in Tier 2.** It requires holding a premise and a conclusion in mind and noticing they are the same object. Genuinely hard.
- **All of Tier 4 late.** Base rates require a sense of "how often, normally" that is itself a stage of development, and the conjunction fallacy is counter-intuitive even for trained adults.
- **Tier 5 is not a fallacy list at all** — it is a manipulation list. It belongs with Stage 11, and it should be taught as *techniques*, not as errors, because the people using them are not making mistakes.

**Delivery formats that work:** "Who would you believe, and why?" (your item — keep it as the Tier 1 workhorse); spot-the-trick in real adverts; the same argument with the content swapped (the *transposition* technique from your FIE talk — it is excellent, and it teaches form without notation); and **"invent the fallacy"**, where children construct a bad argument on purpose. Production beats recognition: you cannot fake having understood a trick until you can perform it.

---

## 6. Misinformation, trolling and manipulation (14–18)

The upper-grade strand should not be "media literacy" as a list of tips. It should be **a model of the information ecosystem plus a small set of portable moves.**

### 6.1 The four-way distinction (teach this first)

Most classroom failures here come from lumping four different things together:

| Type | Goal | Signature | Right response |
|---|---|---|---|
| **Mistake** | none — the speaker believes it | correctable, responds to evidence | correct it kindly |
| **Disagreement** | to persuade | reasons offered, open to counter-reasons | argue |
| **Bullshit** | indifference to truth; the goal is effect | fluency, confidence, no engagement with evidence | refuse the frame; ask for the mechanism |
| **Trolling** | **your reaction**, not your belief | provocation, absurdity, moving targets | do not feed; disengage |
| **Manipulation** | your behaviour | emotional load, urgency, in-group/out-group | name the technique; delay; verify |

The single most useful sentence for a teenager: **"Some speech is not trying to convince you. It is trying to make you react."** Once a student can ask *"what is this trying to get me to do?"* rather than *"is this true?"*, most trolling loses its grip — because the troll's product is the reaction, and the reaction is what gets sold.

### 6.2 The manipulator's toolbox (teach as technique, from the inside)

Your "walk a mile in the manipulator's shoes" instinct is right and is backed by inoculation research: **prebunking** — exposing the technique in advance, in weakened form — protects better than debunking afterwards. So have students *build* the manipulation:

1. **Decontextualise.** Take a real photo, change the caption, change the date.
2. **Fabricate.** Write a fake quote in the style of a real person.
3. **Impersonate.** Make a fake account for a real institution.
4. **Polarise.** Write two posts, one for each side, each designed to make the other side furious.
5. **Scapegoat.** Write a paragraph that names a group as the cause, using only true-but-selected facts.
6. **Flood.** Bury one true claim under twenty trivial ones.
7. **Emotion-first.** Same fact, three versions: frightening, flattering, enraging. Which travels furthest?

Then debrief: *which of these did you find easiest? Which would you fall for?* The confession is the learning.

**Prolog's role here is genuinely strong and underused:** have students encode a manipulator's rule base —

```
trusts(X, claim) :- wants(X, belong), repeats(in_group, claim).
believes(X, claim) :- feels(X, fear), simple(claim).
```

— and then query it. Seeing your own susceptibility written as a rule is more persuasive than any lecture, and it teaches the crucial point that **the manipulation is in the structure, not in the content.** This also gives the group a distinctive, defensible contribution to the media-literacy field, which is otherwise crowded with checklists.

### 6.3 The portable counter-moves

Teach as a short, memorable sequence — not a rubric:

- **Stop.** "Am I being made to feel before I'm made to think?" (The emotion is the tell.)
- **Source.** Who made it, what do they gain, are they independent, what is their evidence?
- **Corroborate.** Two *independent* sources, not two copies. (Lateral reading: leave the page and see what others say about it.)
- **Trace.** Find the original: the un-cropped image, the full quote, the actual date, the primary document.
- **Name it.** "That's a false dilemma." Naming converts a felt pressure into an object you can inspect.
- **Refuse the frame.** Do not argue inside the dichotomy; ask who was left out.
- **Ask for the mechanism.** "How, exactly, does X cause Y?" Most manipulation cannot survive one honest "how".
- **Compared to what?** Ask for the base rate before accepting the vivid case.
- **Steelman, then test.** Give the strongest version a fair run; then check it.
- **Exit.** For trolling specifically: leaving is not losing. The goal was your reaction; withholding it is the win.

### 6.4 AI-specific additions (this is where your curriculum is ahead of the field)

- **Confidence is not evidence.** Fluency, length and certainty carry no information about truth. Demonstrate with a confidently wrong answer and a hesitant right one; ask which *felt* better.
- **The proof obligation.** A chatbot gives you a conclusion with no derivation. Your students will have spent years learning to ask "show me the chain". Make that the standing rule for machine answers.
- **Sycophancy.** Ask the same question twice with opposite framings and watch the answer move. Then ask: *was it reasoning, or agreeing?*
- **The closed world, again.** "It didn't mention it" ≠ "it isn't so". Stage 4, ten years earlier, paying off.
- **Persistence.** Given the evidence in your own reading list that AI assistance reduces persistence and independent performance, the curriculum should deliberately include **no-AI tasks that are hard on purpose**, and name the discomfort as the point.

---

## 7. What is out of bounds, and when

Your email thread asks this question explicitly. A first answer:

| Age | Out of bounds | Why |
|---|---|---|
| < 7 | Any notation; any "logic" labelled as such | The label teaches that logic is a school subject |
| < 9 | Variables as a standalone topic; truth tables; named fallacies | No pattern to put a hole in; no propositions to tabulate; names without questions |
| < 10 | Prolog syntax | The concept must be doable by hand first |
| < 11 | Source-evaluation rubrics and acronyms | Checklists replace judgment at exactly the age judgment is forming |
| < 12 | Formal validity vs. soundness; quantifier nesting | Requires holding form and content apart |
| < 14 | Material implication; the cut; negation as failure as *logic* | All three are true, technical, and destructive of intuition if early |
| < 15 | Base rates, conjunction fallacy, regression | Requires statistical intuition that is still forming |
| Always | "Logic = formulas"; "critical thinking = scepticism"; fallacy-naming as a debate tactic | The three ways this curriculum can fail |
| Adults | Jargon without a situation; a course that starts with the syllabus | The life track fails the moment it looks like school |

Note on developmental stages: Piaget's concrete/formal transition (~11–12) is a useful *heuristic* for pacing, not a law, and it has been substantially criticised for underestimating children. Your group has already rejected the strong version — correctly. The ages above are calibration, not gates; the real gates are the nine in Section 2, and they are diagnosed by the failure symptoms, not by birthdays.

**One adult "out of bounds" deserves spelling out**, because it is the mistake the life track will make if nobody says it: *do not teach adults concepts in the order of a syllabus.* An adult who has lived forty years without the word "implication" does not need the word first; they need a situation in which their current reasoning visibly fails. The order in Part II is therefore a *dependency* order, not a *presentation* order.

---

## 8. How to know it worked

Do not assess by recall of names. Assess by **transfer** — does the child do it when nobody asked? Indicators, roughly in order of appearance:

- Asks **"how do you know?"** without being prompted.
- Says **"that doesn't follow"** rather than **"that's wrong"**.
- Distinguishes **"I disagree"** from **"you're lying"**.
- Can say **what would change their mind**.
- Spots a **missing rule** in a story or an advert.
- Says **"I don't know yet"** and means it as a position, not a defeat.
- Resists a conclusion they *want* to be true.
- Can **explain the reasoning to a younger child** — the near-peer mentoring in your mission is not just multiplication of reach; it is the best available test of understanding.
- Notices when a machine's answer has no chain behind it.

The last one is the whole point of the project, and it is measurable.

**For adults, the indicators change.** You cannot watch a forty-year-old for a year. You ask three questions at the end of a session and one three weeks later:

- *What did you do differently?* (not "what did you learn")
- *Which question did you catch yourself asking?*
- *Where did it fail to work?* — the last is the most valuable, because an adult who reports a failure is using the idea, not reciting it.

---

## 9. The lesson cycle and the "nugget" card

Your mission asks for a method with a name. Here is a five-move cycle that fits every stage above, and that ends where critical thinking begins:

> **See it → Say it → Play it → Prove it → Break it.**

1. **See it.** A concrete case, in the body or in a picture. No vocabulary.
2. **Say it.** The child puts the idea into their own words. Vocabulary arrives here, and only here, and only if it helps.
3. **Play it.** The idea is used in a game where it is *useful*, not displayed.
4. **Prove it.** The child shows the chain — to a partner, to the class, to the machine.
5. **Break it.** The child finds the case where the idea fails, or the rule that is wrong. **This is the critical-thinking step, and it is the one that is always missing.** A curriculum that stops at step 4 produces confident reasoners; only step 5 produces critical ones.

Every concept becomes a one-page **nugget card**, so teachers can pick up and use it:

| Field | Content |
|---|---|
| Concept | one line |
| Ages | range + the discrimination it depends on |
| The idea in one sentence | child-facing |
| The misconception | what it pre-empts |
| See it | 5-minute opener |
| Play it | main activity, with materials |
| Say it | the words to introduce, and the words to avoid |
| Prove it | how the child shows the chain |
| Break it | the counterexample or the broken rule |
| Prolog (optional) | the 3-line program, or "not yet" |
| The question it installs | the sentence the child should start saying |

**Group 4 asked for a catalogue of resources for teachers. The nugget card is that catalogue's record format.** Add four fields and the same card serves all five groups, so nothing has to be rewritten when a resource moves up or down the ladder:

| Field | Content |
|---|---|
| Gate | 1–9; the prerequisite that must already be secure |
| Level | 0–16, or a range if the card is reusable |
| Track | logical thinking / logic programming / AI literacy / life |
| Tool | unplugged · Logical English (LE2) · LPS2 · Prolog · CLP(FD) · s(CASP) · none |

One database, five audiences. A teacher in a Montessori primary, a lecturer in a STEM faculty and a librarian running an evening session are then querying the same table with different filters — which is exactly the multiplying effect the mission asks for, and it is the only way five groups can share a backbone without a committee rewriting it every year.

A proposed name for the whole thing, if you want one: **The Glass Box** — reasoning made visible, checkable, and yours. It carries the Prolog idea (transparency), the critical-thinking idea (inspection), and the anti-AI idea (nothing hidden) in one image, and it works in a classroom and in a grant application.

---

## Part II — Beyond 18

---

## 10. Why the ladder does not end at 18

Three things change when the learner becomes an adult, and one thing does not.

**1. The concepts do not change. The resolution does.** This is the table to keep on the wall, because it is the whole argument for a single backbone across five groups:

| Concept | At 8 | At 14 | At 20 | At 40 |
|---|---|---|---|---|
| Implication | a permission rule | a chain; necessary vs. sufficient | a resolution step; soundness | a clause in a contract you did not read |
| Negation | "not in my list" | contradiction | negation as failure vs. classical negation | "the policy doesn't cover it" |
| Search | the maze walked backwards | a search strategy | completeness, fairness, complexity | "we've tried everything" in a meeting |
| Recursion | Russian dolls | the ancestor rule | termination; structural induction | a procedure that calls itself |
| Credibility | who told you | source and interest | testimony in epistemology | expertise, conflict of interest |

**2. The failure mode inverts.** Children fail because they do not have the concept. Adults fail because they have a *wrong version* of it that has been socially rewarded for decades. Adult teaching is therefore **repair, not construction** — and repair is harder, because the wrong version is load-bearing. Two examples worth designing against:

- The adult who has learned "correlation is not causation" and now uses it to dismiss *all* evidence. The concept has become a shield.
- The adult who has learned "that's ad hominem" and now uses it to dodge *all* criticism. The fallacy name has become a thought-terminating cliché.

Both are gate 6 failures wearing the costume of gate 5 competence. This is why Part II insists on the "Break it" step as hard as Part I does.

**3. The horizon changes.** A child is being prepared to revisit. An adult needs the idea to work *this week*, on a decision they are actually facing. So the adult track is organised by situation, not by concept (Section 14).

**What does not change** is the five-move cycle and the questions. *See it → Say it → Play it → Prove it → Break it* works at eight and at forty-eight. Only "Play it" changes costume: for an adult it is a case study or a role-play, not a game.

---

## 11. Stage 13 — University: the Logical Thinking track

Group 4's sketch, *An Introduction to Logical Thinking*, is a good course. Its eight units and its root questions are the right ones, and the root-question format is unusually good pedagogy — it makes each unit a question rather than a topic. Three structural suggestions, then the sequence.

### 11.1 Three structural suggestions

**(a) Spiral the semantics unit.** Model theory sits at position 6 in the sketch, but unit 1 asks *"how does one know an argument is valid?"* — a question that cannot be answered without the notion of a model. Put a **light** models unit at position 2 (interpretation, truth-in-a-model, countermodel as a picture) and keep the **full** model theory at position 7 as a deepening. This is the same spiral logic as Part I: three passes, never formal first. It also means students meet "valid" as *truth in all models* rather than as a definition to memorise.

**(b) One root question carries a presupposition worth making explicit.** Unit 1 asks *"Why must all arguments be valid?"* Read as a prompt, it is a good question. Read literally, it asserts something false: inductive arguments are not valid, and they are indispensable — most of professional life runs on them. Since every other root question in the sketch is genuinely open, the charitable reading is almost certainly the intended one. But a question with the answer built in is a *loaded question*, and this curriculum teaches students to spot exactly that move (Stage 9, Tier 3). Making the presupposition explicit costs nothing and adds the distinction the unit needs anyway: **"Why does validity matter — and when is the wrong standard?"** That is the gateway to induction, abduction, strength, and to capstone C2.

**The aim is four skills, not two.** The intent behind the question — *we learn to build valid arguments and to recognise invalid ones* — is right, but stated that way it leaves out the two cases students most need:

|  | **Valid** | **Invalid** |
|---|---|---|
| **Good argument** | sound deductive | **strong inductive** |
| **Bad argument** | **valid but false premise** | fallacy |

The two bold cells do the work. *Invalid but good* (induction, abduction, most of medicine and history) stops students despising ordinary reasoning — or, worse, dressing it up as deductive ("the study *proves*…"). *Valid but bad* stops them trusting confident reasoning, because a valid argument from a false premise is the most persuasive kind of lie there is: impeccable form, rotten input.

So Unit 1 should aim at four things: (1) recognise when an argument *claims* deductive force; (2) make such arguments valid; (3) detect invalid ones and see what went wrong; (4) recognise when validity is **not** the right standard, and switch to strength, evidence and base rates. Skill 4 is the one that protects against manipulation, and it is why necessary-vs-sufficient is placed at nine and base rates at fifteen.

**(c) Every unit needs a production task.** The sketch lists root questions and worked examples; it does not list what the student *makes*. Recognition is not the skill — a student can nod at a validity proof and still be unable to write a paragraph that survives one. One artefact per unit, listed below.

### 11.2 The sequence

Ten core units, then three capstones that can run as a second semester.

| # | Unit | Gate | Seeded at | Production task |
|---|---|---|---|---|
| U0 | **Epistemics: how you know** *(new)* | 7 | Stage 4 | Audit three sources on one claim; state what would change your mind |
| U1 | **Logic in effective communication** (theirs) | 3, 5, 6 | Stages 5, 10 | Reconstruct a real argument in standard form; attack it and defend it |
| U2 | **Models, lightly** *(new position)* | 8 | Stages 1, 4 | Draw a model that makes a given argument invalid |
| U3 | **Problem solving, goals, backward reasoning** (theirs) | 4, 5 | Stages 3, 5, 6 | Specify a goal and derive a plan backwards from it |
| U4 | **Search and non-determinism** (theirs) | 5 | Stage 6 | Compare two strategies on the same problem; show where one loops |
| U5 | **Forward reasoning and condition/action rules** (theirs) | 4 | Stage 5 | Build a small production system and defend its rule order |
| U6 | **Hypothetical reasoning and abduction** (theirs) | 6, 7 | Stages 8, 10 | Rank three explanations; justify the ranking by explicitness, not taste |
| U7 | **Model theory, full** (theirs, deepened) | 8 | Stage 12 | Prove validity and invalidity for the same sentence, both ways |
| U8 | **Temporal logic and action theories** (theirs) | 8 | Stages 0, 6 | Model a changing world; identify the frame problem in your own model |
| U9 | **Common-sense reasoning and non-monotonicity** (theirs) | 7, 8 | Stage 8 | List the hidden assumptions in a policy; withdraw one and re-derive |
| C1 | **Fallacies and argumentation** *(new capstone)* | 6 | Stages 8, 9 | Transpose a real argument (their FIE technique); show what survives |
| C2 | **Uncertainty, risk and causal reasoning** *(new capstone)* | — | Stage 10 | Base rates, sensitivity, correlation vs. intervention, decision under risk |
| C3 | **AI and the proof obligation** *(new capstone; bridges to Stage 15)* | 9 | Stages 5, 11 | Take a machine answer apart; produce the chain or refuse the claim |

Note what the reordering buys: **U9 lands last among the core units, and it is the one the whole course has been building toward.** "Common-sense reasoning" in their sketch asks *"what are the most common hidden assumptions in arguments? in arithmetic?"* — that is the ghost rule from Stage 8, at professional resolution. A student who has done the ghost rule at ten meets this unit as a homecoming, not a novelty.

### 11.3 What the sketch is missing

Five gaps, in order of how much they cost a graduate:

1. **Uncertainty.** There is no unit on probability, base rates, risk, or decision under uncertainty. This is the largest gap, and the one most likely to matter in professional life. A logically impeccable argument from a base rate of 0.3% is still a bad decision.
2. **Epistemics and testimony.** The course teaches how to evaluate an argument, but never how to evaluate the *inputs* — who told you, what they gain, whether the sources are independent. Gate 7 has no home in the sketch.
3. **Fallacies and real argumentation.** Unit 1 defines validity; nothing in the sketch studies bad arguments as a subject. That is the transposition technique from your own FIE talk, and it deserves a unit rather than an anecdote.
4. **Causality.** It is implicit in abduction and never treated. Correlation, intervention, and the difference between "because" as explanation and "because" as cause is a unit, not a remark.
5. **AI literacy.** The plenary asked for it. It is Stage 15, and it can be delivered inside this course as C3 or as a standalone module.

---

## 12. Stage 14 — University: the Logic Programming track

This is the track Group 4 described as "mostly for teaching LP, mostly to STEM". It is the only stage in the whole ladder where Prolog is the **object** of study rather than a mirror — and even here, the ordering principle is unchanged:

> **Every feature is introduced after its logical concept, and every feature is taught twice: once as a convenience, once as a distortion.**

That two-sided framing is the pedagogical core of this stage. A student who knows only the convenience becomes a programmer who cannot debug. A student who knows only the distortion becomes a purist who cannot ship. The table:

| Feature | The logical concept it implements | The distortion it introduces | The question the student must answer |
|---|---|---|---|
| Unification | identity and matching (gate 2) | Bidirectional matching is not symmetric in time or cost | When is `X = Y` a test and when is it an assignment? |
| Closed world | "not in my list" (gate 4) | `false` means "not derivable", not "false" | Where does my program's silence become a lie? |
| SLD resolution | search over derivations (gate 5) | Depth-first is incomplete on infinite branches | What would a fair search have found? |
| Negation as failure | negation (gate 4) | `\+` is not classical negation; it is failure to prove | Which of my "not"s are real negations? |
| The cut | commitment (a control decision) | Destroys the declarative reading; makes correctness order-dependent | What did I lose the right to say? |
| Arithmetic | evaluation | `is` is not unification; arithmetic is not relational | Which of my relations are actually functions? |
| Recursion | self-similarity (gate 7) | Termination is not guaranteed by the syntax | What is my base case, and is it reachable? |
| DCGs | grammar as recursion (gate 7) | Parsing is not generation; left recursion loops | Does my grammar terminate in both directions? |
| `findall` / `setof` | quantifiers (gate 2) | Collecting all solutions presupposes that all are found | Did the search actually exhaust? |
| CLP(FD) | constraint satisfaction | Propagation is not search; a fixpoint is not an answer | Which part is reasoning and which is enumeration? |
| Tabling | termination for programs that should not terminate | Tabling changes the semantics, not just the speed | What does my program mean now? |
| ASP / s(CASP) / abduction | non-monotonic and hypothetical reasoning (gates 7, 8) | Stable models are not "the truth"; they are one consistent reading | Which model did I choose, and why that one? |
| Declarative debugging | diagnosis (gate 8) | The bug is in a rule, not in an answer | Which belief is wrong? |

**The habit to install: write both readings.** For every program, the student writes the *declarative* reading ("what is true") and the *procedural* reading ("what happens, in what order"). If the two diverge — and with the cut they will — the divergence is the lesson, not an accident.

**Assessment.** A student should be able to say why a program that returns the right answer is still wrong. That single question separates the track from a syntax course, and it is the same question as Stage 8's "debug the rule base, not the answer", at professional resolution.

**Resources already in the group's hands** map cleanly onto this sequence: Arias's *Logic Programming* for the core, `cliplab.org/logalg` for the constraint and tabling material, the Open Logic Project for the semantics, Logica-URJC and GitHub Classroom for the exercise infrastructure, and LE2/LPS2 for the natural-language front end that lets students meet resolution before they meet the syntax.

---

## 13. Stage 15 — The AI Literacy track

The plenary asked Group 4 for "a track for AI Literacy based on Concepts. Any idea?" Here is one.

**AI literacy is not a tour of architectures. It is the nine gates applied to a machine.** This is why a *concept-based* track is possible at all: every characteristic failure of a generative system maps onto a gate the curriculum already teaches. Hallucination is gate 9. Sycophancy is gate 6. The closed-world error is gate 4. Bias is gate 8 applied to rules rather than to the world. Nothing new has to be invented — the concepts just have to be pointed at a new object.

Ten units. Each has the same four-part shape: **(a)** the human concept, **(b)** how the machine implements it, **(c)** where the machine's version differs, **(d)** the check a user can actually perform.

| # | Unit | Gate | How the machine does it | The check the user performs |
|---|---|---|---|---|
| A1 | **Model vs. world** | 8 | A model is a compressed map of its training distribution | What was it trained on, and what is out of scope? |
| A2 | **Testimony vs. evidence** | 7 | Training data is testimony at scale, with no provenance shown | Who produced this, and are the sources independent? |
| A3 | **Derivation vs. output** | 9 | Text is generated; it is not derived from premises | Ask for the chain. If there is none, it is a claim, not a proof |
| A4 | **Confidence vs. calibration** | 6 | Fluency and certainty are stylistic, not evidential | Ask the same question twice, reframed; watch the answer move |
| A5 | **Closed world and confabulation** | 4 | Absence of data produces plausible invention, not silence | Does it know what it does not know? Test it on something absent |
| A6 | **Rules and bias** | 8 | A biased rule base yields systematically biased conclusions | Who is missing from the data; what does the rule do at the edges? |
| A7 | **Agency and delegation** | 6, 7 | The system acts; it does not bear consequences | Can I defend this decision without the tool? |
| A8 | **Alignment as conflicting rule bases** | 8 | Preferences are encoded as constraints that can conflict | Whose values are encoded, and who decided? |
| A9 | **Optimisation and attention** | 6 | Engagement is the objective function; outrage is a feature | What is this system paid to do? |
| A10 | **Verification and refusal** | 9 | Nothing obliges the user to accept the output | The discipline of not using the tool |

**Delivery by level.** Three levels, and they are not the same lesson:

- **10–13 — understanding only, no use.** The child learns what these systems *are*, through the same unplugged activities as Stage 8: "who would you believe?", "find the ghost rule", "can these all be true?". No accounts, no chatbots. This is consistent with the evidence in your own reading list on early AI use.
- **14–18 — supervised use.** The student uses the tools *and* audits them, with the proof obligation as a standing rule: any machine answer must come with a chain the student can reconstruct.
- **Adult — professional use.** The units become decisions about delegation, liability, and verification in a workplace.

**One design commitment, taken from your reading list:** the curriculum must contain **no-AI tasks that are hard on purpose**, and must name the discomfort as the point. If the only tasks students do are ones a machine can do, the skill being trained is delegation, not thinking.

---

## 14. Stage 16 — Outside academia: thinking skills for life

Group 5's audience has no syllabus, no cohort, no grades, and no obligation. That changes the pedagogy completely, and it is why this stage cannot be Part I with longer words.

### 14.1 Five principles for the life track

1. **Situations, not concepts.** Adults enter through a decision they are facing, not through a topic.
2. **One question per session.** A session that installs one sentence ("compared to what?") has succeeded. A session that covers five concepts has failed.
3. **No jargon, ever.** The people who most need this are the ones most excluded by vocabulary. The word "fallacy" can come at minute thirty, if at all.
4. **Twenty to forty minutes, no homework, no assessment.** Anything that looks like school reproduces the barrier that kept them out.
5. **Peer facilitation, not lecturing.** The facilitator is a neighbour who has done the session before, not an expert.

### 14.2 The situation catalogue

| Situation | The concepts it pulls | The question it installs |
|---|---|---|
| The doctor's waiting room | authority, base rates, necessary vs. sufficient, risk | "What happens to 100 people like me?" |
| The contract you did not read | implicit premises, definitions, necessary vs. sufficient | "What has to be true for this to be fair?" |
| The thing you want to share | source, corroboration, emotion-first design | "Am I being made to feel before I'm made to think?" |
| The family argument | ghost rule, steelman, ad hominem, false dilemma | "What did they not say?" |
| The number in the meeting | base rate, cherry-picking, framing | "Compared to what?" |
| The loan, the purchase | uncertainty language, sunk cost, risk | "What would change my mind?" |
| The political claim | false dilemma, scapegoating, burden of proof | "Who benefits if I believe this?" |
| The AI answer at work | derivation vs. output, confidence, responsibility | "Show me the chain." |
| The "study says" headline | correlation vs. cause, sample, regression | "How often does this happen anyway?" |
| The neighbour, the colleague | dialogue norms, charity, de-escalation | "What is the strongest version of their point?" |

### 14.3 Delivery, and the loop that closes

Delivery channels that already exist and cost nothing to enter: public libraries, unions, community centres, parents' associations, workplace learning, a radio or podcast series, a MOOC with a printed one-page card per session. Plus a **one-day train-the-trainer** so that each session can be run by someone who has done it once.

And here is the structural point that makes Group 5 central rather than peripheral:

> **The parents in this track are the first teachers of the children in Part I.**

A parent who has done "the family argument" can run Stage 0–2 at home. A teacher who has done "the number in the meeting" can run Stage 5 in a classroom. Group 5 is therefore not the tail of the ladder — **it is also the entrance**, and it is the only route to the multiplying effect the mission asks for that does not depend on an institution adopting anything.

The near-peer pipeline closes it: a university student (Group 4) who facilitates two life sessions as a final assignment has satisfied the mentoring requirement in your mission, earned service-learning credit, and tested their own understanding in the hardest possible audience. That is the same mechanism, running in the opposite direction.

---

## 15. The continuity map

This is the deliverable that answers "pedagogical continuity from one level to the next" in one page. Each gate is seeded in Part I, formalised in Part II, and used in Stage 16.

| Gate | Seeded (Part I) | Formalised (Part II) | Used in life (Stage 16) |
|---|---|---|---|
| 1 · symbol vs. thing | Stage 1 | U2, U7 (interpretation) | the contract; the headline |
| 2 · thing vs. slot | Stage 3 | U3 (goals), U4 (search) | the question you did not ask |
| 3 · describing vs. claiming | Stage 2, 4 | U1 (standard form) | the difference between an opinion and a fact |
| 4 · adding vs. conditioning | Stage 5 | U3, U5 (rules), U9 (defaults) | the policy that "doesn't cover it" |
| 5 · finding vs. proving | Stage 6 | U4 (search), U7 (models) | "we've tried everything" |
| 6 · following vs. feeling | Stages 9, 10 | U1, C1, C2 | the thing you want to share |
| 7 · saying vs. knowing | Stages 4, 11 | U0, U6, U9 | the doctor, the expert, the feed |
| 8 · model vs. world | Stage 12 | U2, U7, U8 | the forecast, the risk |
| 9 · derivation vs. output | Stage 5 ("show me the chain") | C3, Stage 15 | the AI answer at work |

**Who owns what.** Group 1 owns Stages 0–5. Group 2 owns Stages 4–9 and the interactive-fiction work. Groups 1 and 2 jointly own Stages 10–11. Group 4 owns Stages 13–14 and co-owns 15. Group 5 owns 16 and, through parents, feeds Stages 0–2 back into Group 1. Nothing in the ladder is owned by nobody, and nothing is owned twice.

---

## 16. Delta against the K–12 list

| Your item | Verdict | Change |
|---|---|---|
| Symbol | Keep | Stage 1; add the icon/index/symbol triad and "the map is not the territory" |
| Variable | Merge | Stage 3, taught *with* questions; a variable is a hole, a question is a hole. Move after objects and relations |
| Objects, properties, relations | Keep | Stage 2; add **arity** and **argument order** (the swapped-arguments bug starts here) |
| Implication | Split | Stage 5, as six micro-steps: and → or → not → if → **necessary vs. sufficient** → chain |
| Backtracking | Keep | Stage 6; add **undo/state** and **exhaustiveness** |
| Facts and rules + credibility | Split | Stage 4 (facts, sources, the third answer) *before* rules; Stage 8 (consistency, counterexample, ghost rule) *after* them |
| Recursion | Earlier | Stage 7, right after rules — it is construction, and construction precedes critique |
| Fallacies | Later | Stage 9, after Stage 8's apparatus; tiered; as questions, not names |
| Misinformation, trolling | Expand | Stage 11; add the mistake/disagreement/bullshit/troll/manipulation distinction and the 10 counter-moves |
| — | **Add** | Negation and the **closed-world assumption**; **quantifiers**; **identity vs. similarity**; **explanation vs. argument**; **causation vs. correlation**; **uncertainty language**; **calibration and "I don't know"**; **dialogue norms** (burden of proof, steelmanning); **attention/algorithm literacy**; **debugging as diagnosis** |

The four additions I would argue hardest for are **the closed-world assumption** (it is the single most transferable Prolog idea and the single most common adult error), **necessary vs. sufficient** (highest value per minute in the whole curriculum), **the ghost rule** (already yours, and the best activity in the set), and **"break it" as a mandatory lesson step**.

---

## 17. Delta against the college sketch

| Item in *An Introduction to Logical Thinking* | Verdict | Change |
|---|---|---|
| Unit 1 · Logic in effective communication | Keep | Split into **U0** (epistemics) and **U1** (argument). Make the presupposition in "why must all arguments be valid?" explicit — inductive arguments are not valid, and that is not a defect |
| Unit 2 · Problem solving, goals, backward reasoning | Keep | U3; add the production task "derive a plan backwards" |
| Unit 3 · Search and non-determinism | Keep | U4; add completeness, fairness and the loop as first-class content |
| Unit 4 · Forward reasoning, production systems | Keep | U5; add conflict resolution as a *design* decision |
| Unit 5 · Hypothetical reasoning, abduction | Keep | U6; add ranking criteria (explicitness, parsimony, testability) |
| Unit 6 · Semantics, model theory | **Spiral** | Light version at U2 (so "valid" is definable), full version at U7 |
| Unit 7 · Temporal logic, situation vs. event calculus | Keep | U8; add the frame problem explicitly |
| Unit 8 · Common-sense reasoning | Keep, and **elevate** | U9; it is the capstone of the core, and the direct heir of the ghost rule |
| — | **Add** | **U0 epistemics and testimony** (gate 7); **C1 fallacies and argumentation**; **C2 uncertainty, risk and causal reasoning**; **C3 AI and the proof obligation** |
| — | **Add (structural)** | One **production artefact per unit**; the **declarative + procedural** double reading in the LP track; the **convenience/distortion** pairing for every feature |

The two additions I would argue hardest for at this level are **C2, uncertainty** — because a valid argument from a bad base rate is still a bad decision, and the sketch currently has no quantitative reasoning at all — and **U0, epistemics** — because the course teaches students to evaluate arguments while leaving the *inputs* unexamined, which is precisely the gap that makes intelligent people vulnerable to confident nonsense.

---

## 18. Open questions for the group

1. **Does the "third answer" belong to logic or to epistemology?** I have placed it at Stage 4 because Prolog forces the issue. It may deserve to be a strand of its own, running from age 4 to adult.
2. **How much of Stage 8 can be done without any formalism?** My view: all of it, and it should be. But this is exactly the question your Montessori contacts can answer.
3. **Where does the manipulator's rule base go?** It is the most distinctive thing this group could publish, and it sits awkwardly between logic and media literacy. It may deserve its own strand across Stages 9–11.
4. **What is the smallest viable pilot?** I would propose Stage 5e (necessary vs. sufficient) plus Stage 8's ghost rule, taught to 9–10-year-olds, measured by the Section 8 indicators. It is two lessons, it needs no technology, and it is the pair of ideas most likely to show a measurable effect.
5. **Do we teach the names of the fallacies at all?** My answer: yes, but late, and only as a shared shorthand for a question the class already asks. Otherwise the names become the curriculum, and naming becomes the substitute for thinking — which is the exact failure mode this project exists to prevent.
6. **Is Stage 13 one course or two?** Ten core units plus three capstones is a full year at most institutions. My preference is one course with C1–C3 as an optional second semester, so that the core is available to every student and the capstones to those who continue.
7. **Who owns the AI literacy track?** It is cross-cutting: Group 4 asked for it, but Stages 10–12 need it too. If it is owned by one group it will be written for one audience. I would make it a shared module with one author and three delivery variants.
8. **Who maintains the catalogue?** Section 9's schema only works if there is one database and one person who owns its fields. Five groups contributing to five spreadsheets is how backbones die.
9. **Does the life track get its own name?** "The Glass Box" works for a classroom. It may not work in a union hall. A separate name for Stage 16 may be worth the cost of losing the single brand.

---

## 19. References worth keeping on the shelf

- Bruner, J. *Toward a Theory of Instruction* — enactive / iconic / symbolic.
- Van Cleave, M. J. *Introduction to Logic and Critical Thinking*, v2.0 — already in your folder; ch. 1 (argument vs. explanation, missing premises, evaluative language) and ch. 4 (fallacies) are the most directly usable.
- Facione, P. *Critical Thinking: What It Is and Why It Counts* — already in your folder; the consensus list of skills and *habits of mind* is the best short statement of the affective side, which any curriculum on this topic under-serves.
- Toulmin, S. *The Uses of Argument* — claim / grounds / warrant / rebuttal, in child-friendly form.
- Kahneman, D. *Thinking, Fast and Slow* — why fallacies need practice in context, not definitions.
- Frankfurt, H. *On Bullshit* — the indifference-to-truth category, which is the right frame for most online speech.
- McGuire, W. / Compton, J. — inoculation theory; the basis for "walk a mile in the manipulator's shoes".
- Wineburg, S. & McGrew, S. — lateral reading; the strongest evidence-based alternative to checklist source evaluation.
- Voss, Q. *Logical Fallacies for Kids* — the attachment; useful as a Tier 1–2 activity source, with the caveat in Section 5, Rule 1.
- Arias, J. *Logic Programming* — https://hdl.handle.net/10115/41543 — the spine of Stage 14.
- The Open Logic Project — https://openlogicproject.org/ — for model theory, soundness and completeness at Stage 13, U2 and U7.
- CLIP Lab logic-algebra material — https://cliplab.org/logalg — constraint and tabling material for Stage 14.
- Logica-URJC — https://github.com/Logica-URJC — exercise infrastructure for the LP track.
- Logical English / LE2 — https://le2.logicalcontracts.com/ — the natural-language front end that lets students meet resolution before syntax. The `rkBook` examples (fox and crow, underground, hunger, louse, event calculus) are the ones cited in the college sketch and are ready to use.
- *An Introduction to Logical Thinking* — the Group 4/5 sketch; its root-question format is the model to keep.
- Your own: Wlodek's declarative diagnosis; Jason's possible-worlds game and Alligator Eggs; Simon's FOLL-E; Stefano's "Who ate the cake?"; Laura's detective work; Michael's world-building; the Doughnut Economics entry point.
