# Automata and Compiler Design

## DFA, DFA to NFA and NFA to DFA

This project explains three important concepts in Automata Theory:

1. Deterministic Finite Automaton (DFA)
2. Conversion of DFA to NFA
3. Conversion of NFA to DFA

---

# 1. Deterministic Finite Automaton (DFA)

## Definition

A **Deterministic Finite Automaton (DFA)** is a finite automaton in which, for every state and every input symbol, there is exactly one transition to the next state.

The word **deterministic** means that there is only one possible path for processing an input string.

A DFA is represented by a 5-tuple:

**DFA = (Q, Σ, δ, q₀, F)**

Where:

- **Q** = Finite set of states
- **Σ** = Input alphabet
- **δ** = Transition function
- **q₀** = Initial state
- **F** = Set of final/accepting states

The transition function is:

**δ : Q × Σ → Q**

This means that for every state and input symbol, exactly one state is obtained.

---

## Characteristics of DFA

- A DFA has a finite number of states.
- It has one initial state.
- It can have one or more final states.
- For every state and input symbol, exactly one transition exists.
- Epsilon (ε) transitions are not allowed.
- For a given input string, there is only one computation path.
- DFA recognizes regular languages.

---

## Example of DFA

Consider the language:

**L = { w ∈ {0,1}* | w contains `101` as a substring }**

The DFA uses four states:

- **q₀** → No part of `101` has been matched.
- **q₁** → `1` has been matched.
- **q₂** → `10` has been matched.
- **q₃** → `101` has been matched.

Here, **q₀** is the initial state and **q₃** is the final state.

### Transition Table

| State | 0 | 1 |
|-------|---|---|
| → q₀ | q₀ | q₁ |
| q₁ | q₂ | q₁ |
| q₂ | q₀ | q₃ |
| ★ q₃ | q₃ | q₃ |

The important sequence is:

**q₀ → q₁ → q₂ → q₃**

with input:

**1 → 0 → 1**

Therefore, whenever `101` occurs in the input string, the DFA reaches the final state q₃.

---

# 2. DFA to NFA Conversion

## Definition

An **NFA (Nondeterministic Finite Automaton)** is a finite automaton in which a state can have zero, one, or multiple transitions for the same input symbol.

A DFA is a special case of an NFA.

Therefore, every DFA can be directly represented as an equivalent NFA.

---

## DFA to NFA Conversion Principle

The conversion from DFA to NFA is very simple.

- The set of states remains the same.
- The initial state remains the same.
- The final states remain the same.
- The input alphabet remains the same.
- Each DFA transition is represented as an NFA transition with a set containing the destination state.

For example, if the DFA has:

**q₀ --1--> q₁**

then the equivalent NFA transition is:

**q₀ --1--> {q₁}**

Similarly:

**q₁ --0--> q₂**

becomes:

**q₁ --0--> {q₂}**

---

## DFA to NFA State Mapping

| DFA State | NFA State |
|-----------|-----------|
| q₀ | q₀ |
| q₁ | q₁ |
| q₂ | q₂ |
| q₃ | q₃ |

The states are unchanged.

---

## NFA Transition Table

For the DFA that accepts strings containing `101`:

| State | 0 | 1 |
|-------|---|---|
| → q₀ | {q₀} | {q₁} |
| q₁ | {q₂} | {q₁} |
| q₂ | {q₀} | {q₃} |
| ★ q₃ | {q₃} | {q₃} |

Thus, the DFA and the resulting NFA accept exactly the same language.

---

## Important Point

**DFA → NFA does not require subset construction.**

The conversion is direct because every DFA already satisfies the rules of an NFA.

Therefore:

**DFA → NFA = Same states + equivalent transitions represented as sets**

---

# 3. Nondeterministic Finite Automaton (NFA)

## Definition

An **NFA (Nondeterministic Finite Automaton)** is a finite automaton in which, for a particular state and input symbol, there may be:

- No transition
- One transition
- Multiple transitions

The transition function of an NFA is:

**δ : Q × Σ → 2ᴽ**

where **2ᴽ** represents the power set of Q.

This means that the result of a transition can be a set of states.

---

## Characteristics of NFA

- An NFA can have multiple transitions for the same input symbol.
- An NFA can have no transition for a particular input.
- An NFA may have ε-transitions in the general definition of an ε-NFA.
- An input string is accepted if at least one possible path reaches a final state.
- NFA recognizes regular languages.
- NFA and DFA have the same computational power.

---

## Example NFA

Consider an NFA for strings containing `101`.

| State | 0 | 1 |
|-------|---|---|
| → q₀ | {q₀} | {q₀, q₁} |
| q₁ | {q₂} | ∅ |
| q₂ | ∅ | {q₃} |
| ★ q₃ | {q₃} | {q₃} |

The important transition is:

**q₀ --1--> {q₀, q₁}**

This means that when the NFA is in q₀ and receives `1`, it can move to either q₀ or q₁.

This is the nondeterministic behavior of an NFA.

---

# 4. NFA to DFA Conversion

## Definition

An NFA can be converted into an equivalent DFA using a method called **Subset Construction** or **Powerset Construction**.

The main idea is:

> Each state of the resulting DFA represents a set of states of the NFA.

For example, if the NFA has:

**{q₀, q₁}**

then this entire set becomes a single state of the DFA.

---

# 5. Subset Construction

The conversion is performed step by step.

### Step 1: Start State

The NFA start state is q₀.

Therefore, the DFA start state is:

**{q₀}**

---

### Step 2: Find Transitions

For each DFA state, consider all NFA states contained in that DFA state.

For example:

**{q₀, q₁}**

For an input symbol, find the transitions from both q₀ and q₁ and combine their results.

---

### Step 3: Create New DFA States

Every new set of NFA states obtained during the process becomes a new DFA state.

For example:

**{q₀, q₂}**

is treated as one DFA state.

---

### Step 4: Repeat

Continue finding transitions for every newly created DFA state until no new states are produced.

---

### Step 5: Determine Final States

A DFA state is a final state if its set contains at least one final state of the NFA.

If q₃ is the final state of the NFA, then:

**{q₀, q₁, q₃}**

is a final state of the DFA because it contains q₃.

---

# 6. NFA to DFA Example

For the NFA:

| State | 0 | 1 |
|-------|---|---|
| → q₀ | {q₀} | {q₀,q₁} |
| q₁ | {q₂} | ∅ |
| q₂ | ∅ | {q₃} |
| ★ q₃ | {q₃} | {q₃} |

The first DFA state is:

**A = {q₀}**

From A:

- On `0` → **{q₀}**
- On `1` → **{q₀,q₁}**

Therefore, we create:

**B = {q₀,q₁}**

From B:

- On `0` → **{q₀,q₂}**
- On `1` → **{q₀,q₁}**

Therefore:

**C = {q₀,q₂}**

From C:

- On `0` → **{q₀}**
- On `1` → **{q₀,q₁,q₃}**

Therefore:

**D = {q₀,q₁,q₃}**

Since D contains q₃, D is a final DFA state.

The process continues until all reachable subsets have been processed.

---

# 7. Important Rules of NFA to DFA Conversion

### Rule 1

The DFA start state is the set containing the NFA start state.

**DFA start = {NFA start}**

---

### Rule 2

A DFA state represents one or more NFA states.

Example:

**{q₀,q₁}**

---

### Rule 3

For each input symbol, combine the transitions of all NFA states in the current set.

---

### Rule 4

If a newly obtained set has not appeared before, create a new DFA state.

---

### Rule 5

If a DFA state contains an NFA final state, it becomes a final state.

---

### Rule 6

The empty set may become a DFA dead/trap state if it is reachable.

---

# 8. DFA vs NFA

| Feature | DFA | NFA |
|---------|-----|-----|
| Full Form | Deterministic Finite Automaton | Nondeterministic Finite Automaton |
| Number of transitions | Exactly one | Zero, one, or multiple |
| Transition result | Single state | Set of states |
| ε-transition | Not allowed | Allowed in ε-NFA |
| Computation paths | One | Multiple possible paths |
| Acceptance | The single path ends in final state | At least one path reaches final state |
| Construction | Can be more complex | Often easier |
| Computational power | Same | Same |
| Conversion | Directly represented as NFA | Requires subset construction to obtain DFA |

---

# 9. Difference Between DFA to NFA and NFA to DFA

## DFA → NFA

The conversion is direct.

```text
DFA
 ↓
Same states
 ↓
Transitions represented as sets
 ↓
NFA
