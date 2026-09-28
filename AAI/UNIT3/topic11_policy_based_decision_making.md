# Topic 11: Policy-Based Decision Making

## 1. ELI5 — What is a Policy?

Imagine an AI robot navigating a maze.

At every position, it has to decide:
> **“What should I do now?”**

A **policy** is the agent's strategy for choosing an action based on the current state.

In simple terms:
> **Policy = Rule/strategy that tells an agent which action to take in each state.**

Example:
```text
State: At intersection
        ↓
Policy
        ↓
Turn Right
```

---

## 2. Formal Definition

A policy is represented by:
$$\pi(a|s)$$

It means:
> Probability of choosing action $a$ when the agent is in state $s$.

For a **deterministic policy**:
$$\pi(s) = a$$
The policy directly maps a state to one action.

For a **stochastic policy**, multiple actions can have probabilities:
$$\pi(a|s) = P(A_t = a | S_t = s)$$

---

## 3. Example

Suppose a robot has three states:
$$S = \{A, B, C\}$$

and two actions:
$$A = \{Left, Right\}$$

A deterministic policy could be:

| State | Action |
| :--- | :--- |
| A | Right |
| B | Left |
| C | Right |

Therefore:
$$\pi(A) = Right$$
$$\pi(B) = Left$$
$$\pi(C) = Right$$

This policy completely defines how the robot behaves.

---

## 4. Deterministic vs Stochastic Policy

### Deterministic Policy
One state → one fixed action.
$$\pi(s) = a$$
Example:
```text
State A → Right
```
Every time the agent reaches A, it chooses Right.

### Stochastic Policy
One state → probabilities for different actions.
Example:
$$\pi(Left|A) = 0.3$$
$$\pi(Right|A) = 0.7$$
So:
```text
             State A
             /     \
          30%       70%
          Left     Right
```
The agent chooses Right more frequently but still explores Left sometimes.

---

## 5. Why Policy-Based Decision Making?

The agent needs to make decisions repeatedly.
Instead of manually specifying every decision, the agent learns a policy.

The overall process is:
```text
Current State
      ↓
Policy
      ↓
Select Action
      ↓
Environment
      ↓
Reward + New State
      ↓
Update Policy
      ↓
Repeat
```

The objective is to find a policy that maximizes expected long-term reward.
$$\pi^* = \arg\max_\pi V^\pi(s)$$

In simple words:
> **Find the policy that gives the highest expected return.**

---

## 6. Policy Evaluation

Before improving a policy, we need to determine:
> **“How good is the current policy?”**

This is called **policy evaluation**.

We calculate the value function:
$$V^\pi(s)$$

using:
$$V^\pi(s) = \sum_a \pi(a|s) \sum_{s'} P(s'|s,a) \left[ R(s,a,s') + \gamma V^\pi(s') \right]$$

So:
```text
Policy
  ↓
Evaluate its actions
  ↓
Calculate Vπ(s)
  ↓
Know how good the policy is
```

---

## 7. Policy Improvement

Once we know the value of the current policy, we can try to improve it.
The agent selects actions with better expected values.

For example:

| Action | Q-value |
| :--- | ---: |
| Left | 4 |
| Right | 8 |
| Forward | 6 |

The agent would prefer:
$$Right$$
because:
$$Q(s, Right) = 8$$
is the highest.

This process is called **policy improvement**.

---

## 8. Policy Iteration

Policy iteration repeatedly performs:
1. **Policy Evaluation**
2. **Policy Improvement**

until the policy becomes optimal.

```text
Initial Policy
      ↓
Policy Evaluation
      ↓
Policy Improvement
      ↓
New Policy
      ↓
Policy Evaluation
      ↓
Policy Improvement
      ↓
Optimal Policy
```

Mathematically:
$$\pi_0 \rightarrow V^{\pi_0} \rightarrow \pi_1 \rightarrow V^{\pi_1} \rightarrow \dots \rightarrow \pi^*$$

---

## 9. Policy Gradient — Important for Agentic AI

In many modern RL systems, instead of storing a table of actions, we represent the policy using parameters $\theta$.

We write:
$$\pi_\theta(a|s)$$

The agent adjusts $\theta$ to improve the policy.
The basic policy-gradient objective is:
$$J(\theta) = E_{\pi_\theta}[G_t]$$

The parameters are updated approximately as:
$$\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)$$

where:
* **$\theta$** = policy parameters
* **$\alpha$** = learning rate
* **$\nabla_\theta J(\theta)$** = direction that improves expected return

### Simple intuition
```text
Current Policy
      ↓
Take actions
      ↓
Observe rewards
      ↓
Determine what worked
      ↓
Adjust policy
      ↓
Better Policy
```

---

## 10. Exploration vs Exploitation

Policy-based agents must balance:

### Exploration
Try new actions to discover potentially better strategies.

### Exploitation
Choose actions that are already known to work well.

Example:
A game-playing agent knows:
* Attack → usually +10
* Defend → usually +5
* New move → unknown

If it **always exploits**, it may never discover a better strategy.
If it **only explores**, it may perform poorly.

Therefore, a good policy balances both.

---

## 11. Policy-Based vs Value-Based Methods

This is an important comparison.

| Feature | Policy-Based | Value-Based |
| :--- | :--- | :--- |
| **Learns** | Directly learns policy $\pi(a\|s)$ | Learns value/Q-function |
| **Action choice** | Directly chooses actions | Chooses actions based on values |
| **Example** | Policy Gradient | Q-Learning |
| **Policy type** | Can naturally represent stochastic policies | Usually derives policy from Q-values |
| **Action space** | Useful for continuous action spaces | Often easier for discrete action spaces |

### Simple distinction
```text
Value-Based:
State → Q-values → Best Action

Policy-Based:
State → Policy → Action
```

---

## 12. Actor-Critic Idea

Modern RL often combines both approaches.

* **Actor:** Learns **what action to take**.
* **Critic:** Evaluates **how good the action/state is**.

```text
             State
               ↓
            Actor
               ↓
            Action
               ↓
          Environment
               ↓
          Reward/State
               ↓
            Critic
               ↓
       Evaluate performance
               ↓
        Improve Actor
```

This is called the **Actor-Critic approach**.
It is widely used in modern reinforcement-learning systems.

---

## 13. Example in Agentic AI

Consider an AI assistant that manages a multi-step task.

Current state:
> User asks: "Find a suitable flight and hotel."

Possible actions:
* Search flights
* Search hotels
* Compare prices
* Ask user for missing information
* Book an option

The policy determines what action should be taken based on the current state.

```text
User Request
     ↓
Current State
     ↓
Policy
     ↓
Search Flights
     ↓
Observe Results
     ↓
Policy
     ↓
Compare Options
     ↓
Policy
     ↓
Next Action
```
This is the foundation of **agentic decision-making**.

---

## 14. Key Advantages

1. **Direct decision making:** The policy directly tells the agent what action to take.
2. **Handles stochastic behavior:** Policies can assign probabilities to different actions.
3. **Suitable for complex environments:** Useful when the number of states/actions is very large.
4. **Works with continuous actions:** For example, controlling robot movement, steering angle, or robotic arm movement.
5. **Supports adaptive behavior:** The policy can improve through experience.

---

## 📝 Quick Revision

Remember these:

* **Policy:** $\pi(a|s) = P(A_t = a | S_t = s)$
* **Deterministic policy:** $\pi(s) = a$
* **Policy objective:** $\pi^* = \arg\max_\pi V^\pi(s)$
* **Policy gradient:** $J(\theta) = E_{\pi_\theta}[G_t]$
* **Policy iteration:** $Policy\ Evaluation \rightarrow Policy\ Improvement \rightarrow Repeat$

### One-line memory trick:
> **Policy = What should I do?**
> **Value = How good is the situation?**
> **Q-value = How good is this action?**

---

## 💡 10-Mark Exam Structure

If asked **"Explain policy-based decision making in Reinforcement Learning"**, write:

1. Definition of policy
2. Deterministic policy
3. Stochastic policy
4. Policy evaluation
5. Policy improvement
6. Policy iteration
7. Policy gradient concept
8. Exploration vs exploitation
9. Policy-based vs value-based methods
10. Applications in Agentic AI

> **Next: Topic 12 — Q-Learning and Policy Optimization.**
