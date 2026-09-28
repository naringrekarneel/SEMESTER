# Topic 10: Value Functions and Bellman Equations

This topic builds directly on **MDP + Reinforcement Learning**.

---

## 1. ELI5 — What is a Value Function?

Imagine you're playing a game.

You're currently in **State A**.

You can ask:
> **“How good is it to be in State A?”**

That's what the **Value Function** tells us.
If State A usually leads to large future rewards, its value is high.
If State A usually leads to penalties or failure, its value is low.

So:
> **Value function = expected future reward from a state.**

---

## 2. Why Do We Need Value Functions?

An agent doesn't only want to know:
> “What reward do I get right now?”

It also wants to know:
> “What rewards can I get in the future?”

For example:
```text
State A
   ↓
State B
   ↓
State C
   ↓
Goal
```

Suppose:
* A → reward = 1
* B → reward = 2
* C → reward = 10

Even though State A gives only a small immediate reward, it may be valuable because it eventually leads to the goal.

Therefore, the agent needs a way to estimate **long-term usefulness**.
That's the purpose of value functions.

---

## 3. State-Value Function

The **state-value function** tells us the expected return when the agent starts in state $s$ and follows policy $\pi$.

It is represented as:
$$V^\pi(s) = E_\pi[G_t | S_t = s]$$

Where:
* **$V^\pi(s)$** = value of state $s$
* **$\pi$** = policy being followed
* **$G_t$** = return from time $t$
* **$E$** = expected value

### Simple meaning
> **$V(s)$ = “How good is this state if I follow my current policy?”**

---

## 4. Action-Value Function

The **action-value function**, or **Q-function**, tells us how good it is to:
> Take action $a$ in state $s$ and then follow policy $\pi$.

It is represented as:
$$Q^\pi(s,a) = E_\pi[G_t | S_t = s, A_t = a]$$

### Simple meaning
> **$Q(s,a)$ = “How good is it to take this particular action in this state?”**

---

## 5. V(s) vs Q(s,a)

This is a very important exam question.

| $V(s)$ | $Q(s,a)$ |
| :--- | :--- |
| Evaluates a **state** | Evaluates a **state-action pair** |
| “How good is this state?” | “How good is this action in this state?” |
| Does not explicitly specify an action | Explicitly includes an action |
| State-value function | Action-value function |

### Example

Suppose:
```text
          Move Left
             ↓
          State B

State A
          Move Right
             ↓
          State C
```

$V(A)$ asks:
> How valuable is being in State A?

$Q(A, Left)$ asks:
> How valuable is taking Left from State A?

---

## 6. Bellman Equation

The **Bellman equation** is one of the most important concepts in Reinforcement Learning.

The basic idea is:
> **Value of current state = immediate reward + discounted value of future state.**

For a deterministic situation:
$$V(s) = R(s,a) + \gamma V(s')$$

Where:
* **$R(s,a)$** = immediate reward
* **$\gamma$** = discount factor
* **$V(s')$** = value of next state

---

## 7. Bellman Expectation Equation

For a policy $\pi$, the Bellman expectation equation is:
$$V^\pi(s) = \sum_a \pi(a|s) \sum_{s'} P(s'|s,a) \left[ R(s,a,s') + \gamma V^\pi(s') \right]$$

Don't panic about the formula.
It simply says:
> **Current value = expected immediate reward + expected discounted future value.**

The summations are needed because:
* The policy may choose different actions with different probabilities.
* The environment may transition to different states with different probabilities.

---

## 8. Simple Bellman Example

Suppose:
* Current reward = 5
* $\gamma = 0.8$
* Next state's value = 10

Then:
$$V(s) = 5 + 0.8(10)$$
$$V(s) = 5 + 8$$
$$\boxed{V(s) = 13}$$

So the current state's value is **13**.

---

## 9. Bellman Equation for Q-Value

The Bellman expectation equation for Q-values is:
$$Q^\pi(s,a) = \sum_{s'} P(s'|s,a) \left[ R(s,a,s') + \gamma \sum_{a'} \pi(a'|s') Q^\pi(s',a') \right]$$

Again, the idea is simple:
> **Q-value = immediate reward + discounted future Q-value.**

---

## 10. Optimal Value Function

So far, we've discussed values under a particular policy $\pi$.
But what if we want the **best possible policy**?

Then we use the **optimal value function**:
$$V^*(s) = \max_a Q^*(s,a)$$

It means:
> The optimal value of a state is the value obtained by choosing the best action.

The optimal Bellman equation is:
$$V^*(s) = \max_a \sum_{s'} P(s'|s,a) \left[ R(s,a,s') + \gamma V^*(s') \right]$$

---

## 11. Bellman Optimality Equation for Q

The optimal Q-value satisfies:
$$Q^*(s,a) = \sum_{s'} P(s'|s,a) \left[ R(s,a,s') + \gamma \max_{a'} Q^*(s',a') \right]$$

This equation is extremely important because **Q-learning** is based on this idea.

---

## 12. Relationship Between V and Q

The relationship is:
$$V^\pi(s) = \sum_a \pi(a|s) Q^\pi(s,a)$$

For the optimal case:
$$V^*(s) = \max_a Q^*(s,a)$$

So:
```text
              State
                ↓
          Possible actions
          /      |      \
         A1      A2      A3
         ↓       ↓       ↓
       Q1       Q2      Q3
                ↓
          Choose maximum
                ↓
             V*(s)
```

---

## 13. Worked Example

Suppose an agent is at State A.
It has two possible actions:

| Action | Immediate Reward | Future State Value |
| :--- | ---: | ---: |
| Left | 2 | 5 |
| Right | 4 | 3 |

Let $\gamma = 0.5$.

**For Left:**
$$Q(A, Left) = 2 + 0.5(5)$$
$$Q(A, Left) = 4.5$$

**For Right:**
$$Q(A, Right) = 4 + 0.5(3)$$
$$Q(A, Right) = 5.5$$

Therefore:
$$V^*(A) = \max(4.5, 5.5)$$
$$\boxed{V^*(A) = 5.5}$$

The better action according to these values is **Right**.

---

## 14. Why Bellman Equations Matter in Agentic AI

Agentic AI systems often need to make a sequence of decisions.

For example:
```text
Understand task
      ↓
Choose action
      ↓
Observe result
      ↓
Choose next action
      ↓
Observe result
      ↓
Reach goal
```

The Bellman idea helps the agent reason about:
> **Immediate reward + future consequences**

This is essential for:
* Reinforcement Learning
* Q-learning
* Dynamic Programming
* Policy optimization
* Sequential decision-making
* Autonomous agents

---

## 15. Key Difference: Reward vs Value

A common exam confusion:

### Reward
Reward is the **immediate feedback**.
Example:
$$R = +10$$

### Value
Value represents the **expected long-term return**.
Example:
$$V(s) = 50$$

So:
> **Reward = what you get now.**
> **Value = how good the future is expected to be.**

---

## 📝 Quick Revision

### Must remember:

* **State-value:** $V^\pi(s) = E_\pi[G_t | S_t = s]$
* **Action-value:** $Q^\pi(s,a) = E_\pi[G_t | S_t = s, A_t = a]$
* **Basic Bellman idea:** $Value = Immediate\ Reward + Discounted\ Future\ Value$
* **Optimal state value:** $V^*(s) = \max_a Q^*(s,a)$

### One-line memory trick:
> **V asks “How good is the state?”**
> **Q asks “How good is this action in this state?”**
> **Bellman says “Now + discounted future.”**

---

## 💡 Exam Tip — 10 Marks

If asked **“Explain Value Functions and Bellman Equations”**, write:
1. Need for value functions
2. State-value function
3. Action-value/Q-function
4. Difference between $V(s)$ and $Q(s,a)$
5. Bellman equation
6. Bellman expectation equation
7. Bellman optimality equation
8. Worked numerical example
9. Relationship between value and Q-value
10. Applications in Reinforcement Learning/Agentic AI

> **Next topic: Topic 11 — Policy-Based Decision Making.**
