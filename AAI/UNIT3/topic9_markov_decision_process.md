# Topic 9: Markov Decision Process (MDP)

## 1. What is an MDP? — ELI5

Imagine a **game-playing agent**.

At every moment:
1. The agent looks at the **current situation**.
2. It chooses an **action**.
3. The environment changes.
4. The agent receives a **reward or penalty**.
5. It reaches a **new situation**.
6. It repeats this process.

An **MDP (Markov Decision Process)** is a mathematical framework used to represent this kind of **decision-making under uncertainty**.

> **Simple idea:** MDP tells an agent:
> **“Given where I am now, what can I do, what might happen, and what reward might I get?”**

---

## 2. Formal Definition

An MDP is generally represented as:
$$M = (S, A, P, R, \gamma)$$

where:

| Component | Meaning |
| :--- | :--- |
| **$S$** | Set of all possible **states** |
| **$A$** | Set of possible **actions** |
| **$P$** | **Transition probability** |
| **$R$** | **Reward function** |
| **$\gamma$** | **Discount factor** |

These five components completely describe the decision-making problem.

---

## 3. Components of MDP

### 1. State ($S$)
A **state** represents the current situation of the agent.

Example for a robot:
* $S_1$ = Robot at Room A
* $S_2$ = Robot at Room B
* $S_3$ = Robot at Room C

So:
$$S = \{S_1, S_2, S_3\}$$

### 2. Action ($A$)
An action is something the agent can perform.

For example:
$$A = \{MoveLeft, MoveRight, MoveForward, Stop\}$$

The available actions may depend on the current state.

### 3. Transition Probability ($P$)
The transition function describes **how likely the agent is to move from one state to another after taking an action**.

It is represented as:
$$P(s'|s,a)$$

Meaning:
> Probability of reaching next state $s'$ when action $a$ is taken in current state $s$.

### Example
A robot wants to move forward.

Normally:
* 90% → moves forward
* 10% → slips and moves sideways

Therefore:
$$P(s'|s,a) = 0.9$$

This is what makes MDP useful for **uncertain environments**.

---

## 4. Reward Function ($R$)

The reward tells the agent how good or bad an outcome is.

For example:

| Situation | Reward |
| :--- | ---: |
| Reaches destination | +10 |
| Moves normally | +1 |
| Hits obstacle | -10 |
| Reaches dangerous area | -20 |

The agent's objective is generally to maximize its **long-term cumulative reward**.

---

## 5. Discount Factor ($\gamma$)

The discount factor determines how much the agent values **future rewards**.
$$0 \leq \gamma \leq 1$$

### If $\gamma$ is close to 0
The agent focuses mainly on **immediate rewards**.

### If $\gamma$ is close to 1
The agent gives more importance to **future rewards**.

The return is:
$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots$$

---

## 6. Markov Property — VERY IMPORTANT

The key idea behind an MDP is the **Markov property**.

It states:
> The future depends only on the **current state and current action**, not on the complete history of previous states.

Mathematically:
$$P(S_{t+1} | S_t, A_t, S_{t-1}, A_{t-1}, \dots) = P(S_{t+1} | S_t, A_t)$$

### Simple example
Suppose a robot is currently at Room B.
To determine where it will go next, we only need:
* Current state = Room B
* Current action = Move Forward

We don't need to know whether the robot came from Room A or Room C.
That's the **Markov property**.

---

## 7. Simple MDP Example

Consider a robot navigating between three locations:
```text
Start → Room A → Room B → Goal
```

### States
$$S = \{Start, A, B, Goal\}$$

### Actions
$$A = \{Move, Stay\}$$

### Rewards
* Reaching Goal → +10
* Moving → -1
* Staying → -2

The robot has to find a sequence of actions that maximizes its total reward.

For example:
```text
Start
  ↓ Move
Room A
  ↓ Move
Room B
  ↓ Move
Goal
```

Rewards:
$$-1, -1, +10$$

The agent learns that reaching the goal is valuable even though it has to accept some short-term negative rewards.

---

## 8. Deterministic vs Stochastic MDP

### Deterministic
The same action always produces the same result.
Example:
$$P(S_2 | S_1, A) = 1$$
So:
```text
S1 + Action → S2
```
with certainty.

### Stochastic
The result is uncertain.
Example:
$$P(S_2 | S_1, A) = 0.8$$
$$P(S_3 | S_1, A) = 0.2$$

So the same action can lead to different states.
**Most real-world environments are stochastic.**

---

## 9. Policy in MDP

A **policy** tells the agent which action to choose in a particular state.
It is represented as:
$$\pi(a|s)$$

For a deterministic policy:
$$\pi(s) = a$$

Example:

| State | Policy |
| :--- | :--- |
| Start | Move |
| Room A | Move |
| Room B | Move |
| Goal | Stop |

So the policy is essentially the agent's **strategy for making decisions**.

---

## 10. MDP and Reinforcement Learning

This distinction is important.

### MDP
MDP provides the **mathematical model of the decision-making problem**.

### Reinforcement Learning
RL is a **learning approach** that allows an agent to learn a good policy through interaction and rewards.

In simple terms:
```text
MDP
 ↓
Defines states, actions, transitions and rewards
 ↓
RL Agent
 ↓
Learns
 ↓
Optimal / good Policy
```

The environment can be modeled as an MDP even when the agent does not initially know its transition probabilities or rewards.

---

## 11. MDP vs Classical Planning

| Feature | Classical Planning | MDP |
| :--- | :--- | :--- |
| **Environment** | Usually deterministic | Can be stochastic |
| **Uncertainty** | Usually low/absent | Explicitly modeled |
| **Transitions** | Known outcomes | Probabilistic outcomes |
| **Rewards** | Often goal-based | Reward-based |
| **Decision making** | Plan a sequence | Choose actions under uncertainty |
| **Feedback** | Usually predetermined | Rewards provide feedback |
| **Example** | Robot moves through known rooms | Robot navigates with uncertain movement |

---

## 12. MDP in Agentic AI

MDPs are useful for Agentic AI because agents often need to make **multiple decisions under uncertainty**.

For example, an AI travel agent:
```text
Current situation
      ↓
Choose action
      ↓
Book flight / Search hotel / Change plan
      ↓
Environment changes
      ↓
Receive reward/feedback
      ↓
New state
      ↓
Choose next action
```

The agent must consider not just the immediate action but its **future consequences**.

---

## 13. 10-Mark Exam Answer Structure

If asked:
**"Explain Markov Decision Process (MDP)."**

Write in this order:
1. Definition of MDP
2. MDP tuple: $M = (S, A, P, R, \gamma)$
3. Explain states
4. Explain actions
5. Explain transition probabilities
6. Explain rewards
7. Explain discount factor
8. Explain Markov property
9. Give a simple robot/navigation example
10. Explain MDP's role in Reinforcement Learning/Agentic AI

---

## 📝 Quick Revision

Remember:
**MDP = Decision-making framework under uncertainty**
$$M = (S, A, P, R, \gamma)$$

* **$S$** → States
* **$A$** → Actions
* **$P$** → Transition probabilities
* **$R$** → Rewards
* **$\gamma$** → Discount factor
* **Markov property** → Future depends on current state and action, not the entire history.
* **Policy** → Strategy for choosing actions.
* **RL** → Learns a good policy through interaction and rewards.

### One-line memory trick:
> **“State → Action → Probability → Reward → Future value.”**

---

## 🧠 Quick Check

**Q1.** What is the difference between a state and an action in an MDP?
**Q2.** What does the Markov property mean?
**Q3.** If $\gamma = 0$, does the agent care about future rewards? Why?
**Q4.** An agent receives rewards $5, 10, 20$ for three consecutive steps with $\gamma = 0.5$. Calculate the discounted return.

> *Say **NEXT** when you're ready for **Topic 10: Value Functions and Bellman Equations**.*
