# Topic 7: STRIPS and Classical Planning Algorithms
**Module 2 | Very important for exams**

## 1. What is STRIPS?

**STRIPS** stands for **Stanford Research Institute Planning System**.

It is a formal language and representation used to describe **classical planning problems** using:
* Initial state
* Goal state
* Actions
* Preconditions
* Effects

### ELI5

Imagine giving a robot a rulebook. For every action, you tell it:
> **"You can do this action only if these conditions are true, and after doing it, these things will change."**

That's basically STRIPS.

For example:
> **Pick up a box**

You can pick it up only if:
* Robot is beside the box.
* Robot's hand is empty.
* Box is on the floor.

After picking it up:
* Robot is holding the box.
* Box is no longer on the floor.

---

## 2. STRIPS Action Representation

A STRIPS action has three major components:
$$Action = (Preconditions, Add\ List, Delete\ List)$$

### 1. Preconditions
Conditions that must already be true.

### 2. Add List
Facts that become **true** after executing the action.

### 3. Delete List
Facts that become **false** after executing the action.

This is extremely important.

---

## 3. Example of a STRIPS Action

Consider:
```text
Action: PICKUP(Box)
```

**Preconditions:**
```text
At(Robot, RoomA)
At(Box, RoomA)
HandEmpty
```

**Add List:**
```text
Holding(Box)
```

**Delete List:**
```text
At(Box, RoomA)
HandEmpty
```

Therefore:
$$PICKUP(Box) = (Preconditions, AddList, DeleteList)$$

The resulting state is obtained by:
$$S' = (S - DeleteList) \cup AddList$$

This formula is **very important for exams**.
It means:
1. Remove facts made false by the action.
2. Add facts made true by the action.

---

## 4. Worked Example

Suppose the current state is:
```text
At(Robot, A)
At(Box, A)
HandEmpty
```

Execute:
```text
PICKUP(Box)
```

### Before action
```text
At(Robot, A)
At(Box, A)
HandEmpty
```

### Delete List
```text
At(Box, A)
HandEmpty
```
Remove them.

### Add List
```text
Holding(Box)
```

### New state
```text
At(Robot, A)
Holding(Box)
```

So:
$$S' = (S - \{At(Box, A), HandEmpty\}) \cup \{Holding(Box)\}$$

---

## 5. STRIPS Planning Example

Let's solve a simple problem.

**Initial state:**
```text
At(Robot, A)
At(Box, A)
HandEmpty
```

**Goal:**
```text
At(Box, B)
```

**Available actions:**

#### PICKUP(Box)
**Preconditions:**
```text
At(Robot, A)
At(Box, A)
HandEmpty
```
**Effects:**
```text
+ Holding(Box)
- At(Box, A)
- HandEmpty
```

#### MOVE(A, B)
**Precondition:**
```text
At(Robot, A)
```
**Effects:**
```text
+ At(Robot, B)
- At(Robot, A)
```

#### PUTDOWN(Box)
**Preconditions:**
```text
At(Robot, B)
Holding(Box)
```
**Effects:**
```text
+ At(Box, B)
+ HandEmpty
- Holding(Box)
```

---

## 6. Finding the Plan

Start:
```text
At(Robot, A)
At(Box, A)
HandEmpty
```

### Step 1
Execute: `PICKUP(Box)`
State becomes:
```text
At(Robot, A)
Holding(Box)
```

### Step 2
Execute: `MOVE(A, B)`
State becomes:
```text
At(Robot, B)
Holding(Box)
```

### Step 3
Execute: `PUTDOWN(Box)`
Final state:
```text
At(Robot, B)
At(Box, B)
HandEmpty
```

Goal satisfied.
Therefore:
**PICKUP → MOVE → PUTDOWN**
is a valid plan.

---

## 7. Classical Planning Algorithms

Several algorithms can be used to find plans.

### 1. Forward State-Space Planning
Starts from the initial state and applies actions.
```text
Initial
   ↓
Action
   ↓
New State
   ↓
Action
   ↓
Goal
```
This is also called **progression planning**.

### 2. Backward State-Space Planning
Starts from the goal and works backward.
```text
Goal
 ↑
Required Action
 ↑
Previous State
 ↑
Required Action
 ↑
Initial
```
This is also called **regression planning**.

### 3. Partial-Order Planning
Instead of fixing the complete order of actions immediately, partial-order planning specifies only the ordering constraints that are necessary.

For example:
```text
Make coffee
Wash cup
Add coffee
Pour water
```
Some actions may be performed in different orders without affecting the final result.

The planner therefore specifies relationships such as:
$$WashCup \prec AddCoffee$$
meaning:
> Wash the cup must happen before adding coffee.

This provides flexibility.

---

## 8. Forward vs Backward vs Partial-Order Planning

| Feature | Forward | Backward | Partial-Order |
| :--- | :--- | :--- | :--- |
| **Starting point** | Initial state | Goal | Goals/subgoals |
| **Direction** | Forward | Backward | Flexible |
| **Also called** | Progression | Regression | Least-commitment planning |
| **Main idea** | Apply applicable actions | Find actions that achieve goals | Specify only necessary ordering |
| **Advantage** | Easy to understand | Focuses on goal | Flexible plans |
| **Disadvantage** | May explore irrelevant states | Can have many predecessor choices | More complex representation |

---

## 9. Why STRIPS is Important

STRIPS introduced a structured way of representing planning actions.

Instead of simply saying:
> "Move the robot."

We explicitly describe:
```text
Action
   ↓
Preconditions
   ↓
Effects
      ↙     ↘
   Add       Delete
```

This makes automated planning possible. STRIPS became a foundation for many later planning systems and languages.

---

## 10. STRIPS vs Ordinary Search

This distinction is useful in exams.

| Ordinary Search | STRIPS Planning |
| :--- | :--- |
| States and transitions | States, actions and logical conditions |
| Generic search representation | Structured planning representation |
| Action described mainly by transition | Action explicitly has preconditions/effects |
| Can search paths | Can construct plans satisfying logical goals |

---

## 11. Connection to Agentic AI

Modern AI agents often perform something conceptually similar to STRIPS planning.

Suppose an agent receives:
> "Prepare a presentation and send it to the team."

The agent could represent:
```text
Goal:
PresentationSent
```

Possible actions:
```text
CollectInformation
CreateSlides
ReviewSlides
ExportPDF
SendEmail
```

Each action has requirements. For example:
```text
SendEmail

Preconditions:
PDFExists
RecipientKnown

Effect:
PresentationSent
```

The agent therefore cannot legitimately execute `SendEmail` before the presentation exists.
This is the core idea behind **planning with preconditions and effects**.

---

## 📝 Quick Revision Sheet

### STRIPS — Must Remember
* **STRIPS represents:** State + Actions + Preconditions + Effects
* **Action representation:** $Action = (Preconditions, AddList, DeleteList)$
* **State transition:** $S' = (S - DeleteList) \cup AddList$

### Three important planning approaches:
* **Forward planning** → Initial → Goal
* **Backward planning** → Goal → Initial
* **Partial-order planning** → Only necessary action ordering is specified

> **Golden exam point:**
> Preconditions determine when an action can be executed, while Add and Delete effects determine how the state changes after execution.

---

## 🧠 Active Learning

### Q1 — Conceptual
What is STRIPS? Explain its three main components.

### Q2 — Conceptual
What is the difference between an **Add List** and a **Delete List**?

### Q3 — Conceptual
Differentiate between forward planning, backward planning and partial-order planning.

### Q4 — Practical
Given:
**Current state:**
```text
At(Robot,A)
At(Box,A)
HandEmpty
```

**Action: PICKUP(Box)**

**Preconditions:**
```text
At(Robot,A)
At(Box,A)
HandEmpty
```

**Add List:**
```text
Holding(Box)
```

**Delete List:**
```text
At(Box,A)
HandEmpty
```

What will the **new state** be after executing `PICKUP(Box)`?

> *Reply with your answers or say **NEXT** to move to **Topic 8: Reinforcement Learning for Agents**.*
