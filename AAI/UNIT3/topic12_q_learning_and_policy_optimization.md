# Topic 12: Q-Learning and Policy Optimization

This topic is especially important because **Q-Learning is one of the most common Reinforcement Learning algorithms**.

---

## 1. ELI5 — What is Q-Learning?

Imagine a robot learning to escape a maze.

At first, the robot doesn't know which action is good.
It tries different actions:
* Move left
* Move right
* Move forward
* Move backward

Whenever an action leads to a good result, it gets a positive reward.

Over time, it builds a table like:

| State | Action | Q-value |
| :--- | :--- | ---: |
| A | Left | 2 |
| A | Right | 8 |
| B | Left | 5 |
| B | Right | 1 |

The robot learns:
> **“When I'm in State A, Right is probably the best action.”**

This is the basic idea of **Q-Learning**.

---

## 2. What is Q-Learning?

**Q-Learning** is a **model-free, off-policy reinforcement learning algorithm** that learns the optimal action-value function $Q^*(s,a)$.

Its goal is to learn:
$$Q^*(s,a)$$
which represents the expected long-term reward for taking action $a$ in state $s$ and then behaving optimally.

---

## 3. Why is it Called Q-Learning?

The letter **Q** represents the **quality of an action**.

So:
$$Q(s,a)$$
means:
> **How good is action $a$ when the agent is in state $s$?**

The agent chooses actions with higher Q-values.

---

## 4. Q-Table

For small environments, Q-values can be stored in a table.

Example:

| State | Left | Right | Forward |
| :--- | ---: | ---: | ---: |
| $S_1$ | 2 | **8** | 4 |
| $S_2$ | **7** | 3 | 5 |
| $S_3$ | 1 | 4 | **9** |

For $S_1$:
$$Q(S_1, Right) = 8$$

Therefore, the agent would generally choose **Right**.

---

## 5. Q-Learning Update Rule

This is the **most important formula**.

$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]$$

Where:

| Symbol | Meaning |
| :--- | :--- |
| **$s$** | Current state |
| **$a$** | Current action |
| **$r$** | Reward received |
| **$s'$** | Next state |
| **$\alpha$** | Learning rate |
| **$\gamma$** | Discount factor |
| **$\max_{a'} Q(s',a')$** | Best future Q-value |

---

## 6. Understanding the Formula

The formula can be understood as:
$$New\ Q = Old\ Q + Learning\ Rate \times Error$$

The error is:
$$TD\ Error = Target - Old\ Q$$

where the target is:
$$Target = r + \gamma \max_{a'} Q(s',a')$$

Therefore:
> **Q-Learning updates its knowledge based on the difference between what it expected and what actually happened.**

---

## 7. Numerical Example

Suppose:
* Current Q-value = 5
* Reward = 10
* $\gamma = 0.9$
* Best Q-value of next state = 8
* $\alpha = 0.1$

Formula:
$$Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

Substitute:
$$Q(s,a) = 5 + 0.1[10 + (0.9)(8) - 5]$$

Calculate:
$$= 5 + 0.1[10 + 7.2 - 5]$$
$$= 5 + 0.1(12.2)$$
$$= 5 + 1.22$$
$$\boxed{Q(s,a) = 6.22}$$

So the Q-value increases from **5 to 6.22**.

---

## 8. Q-Learning Algorithm

**Step 1:** Initialize Q-values. Usually: $Q(s,a) = 0$
**Step 2:** Observe the current state $s$.
**Step 3:** Choose an action $a$.
**Step 4:** Perform the action.
**Step 5:** Receive reward $r$ and observe next state $s'$.
**Step 6:** Update Q-value:
$$Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$
**Step 7:** Set $s \leftarrow s'$
**Step 8:** Repeat until the task is completed.

---

## 9. Exploration and Exploitation in Q-Learning

The agent needs to decide whether to:

### Exploit
Choose the action with the highest Q-value.
$$a = \arg\max_a Q(s,a)$$

### Explore
Try another action to discover whether it might be better.

A common strategy is **$\epsilon$-greedy**.
* With probability $\epsilon$: Choose a random action.
* With probability $1-\epsilon$: Choose the action with the highest Q-value.

Example: $\epsilon = 0.2$
Then approximately:
* 20% → explore
* 80% → exploit

---

## 10. Why is Q-Learning Model-Free?

A model-based method needs to know the environment's transition model: $P(s'|s,a)$

Q-Learning doesn't need to know this beforehand.
It simply learns from experience:

```text
State
  ↓
Action
  ↓
Environment
  ↓
Reward + Next State
  ↓
Update Q
  ↓
Repeat
```

Therefore:
> **Q-Learning learns directly from interaction without explicitly knowing the environment model.**

---

## 11. Why is Q-Learning Off-Policy?

Q-Learning is called **off-policy** because:
> The policy used to explore the environment can be different from the policy being learned.

The update uses:
$$\max_{a'} Q(s',a')$$

It assumes the agent will choose the **best possible future action**, even if the current behavior policy sometimes chooses random actions for exploration.

---

## 12. Q-Learning vs SARSA

This is a common comparison.

| Q-Learning | SARSA |
| :--- | :--- |
| Off-policy | On-policy |
| Uses maximum next Q-value | Uses Q-value of actual next action |
| More greedy | Considers current behavior |
| Update uses $\max_{a'} Q(s',a')$ | Update uses $Q(s',a')$ for selected action |
| Learns optimal policy | Learns policy being followed |

### Q-Learning:
$$Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

### SARSA:
$$Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma Q(s',a') - Q(s,a)]$$

---

## 13. Policy Optimization

Q-Learning learns values and derives a policy from them.
**Policy optimization**, on the other hand, directly tries to improve the policy.

Instead of learning $Q(s,a)$ and then choosing the best action, we directly optimize:
$$\pi_\theta(a|s)$$
where $\theta$ represents the parameters of the policy.

The goal is:
$$\max_\theta J(\theta)$$
where $J(\theta)$ represents the expected return.

---

## 14. Policy Gradient

A basic policy-gradient method updates the policy parameters in the direction that increases expected reward:
$$\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)$$

The intuition is:
```text
Current Policy
      ↓
Take Actions
      ↓
Receive Rewards
      ↓
Determine good/bad actions
      ↓
Adjust Policy Parameters
      ↓
Improved Policy
```

---

## 15. Q-Learning vs Policy Optimization

| Feature | Q-Learning | Policy Optimization |
| :--- | :--- | :--- |
| **Main object learned** | Q-function | Policy |
| **Representation** | $Q(s,a)$ | $\pi_\theta(a \| s)$ |
| **Policy** | Derived from Q | Directly learned |
| **Exploration** | Often $\epsilon$-greedy | Usually built into stochastic policy |
| **Discrete actions** | Very suitable | Suitable |
| **Continuous actions** | Difficult with basic Q-table | Often more suitable |
| **Example** | Q-Learning | Policy Gradient |

---

## 16. Agentic AI Connection

Q-Learning can help an agent learn which actions produce better long-term outcomes.

For example, a game-playing agent:
```text
Game State
    ↓
Choose Action
    ↓
Receive Reward
    ↓
Observe New State
    ↓
Update Q-value
    ↓
Choose Better Action
```

For more complex Agentic AI systems, policy optimization and actor-critic methods can handle large or continuous action spaces.

---

## 📝 Quick Revision

### Q-value
$Q(s,a)$ → How good is action $a$ in state $s$?

### Q-Learning update
$$Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

### $\epsilon$-greedy
* $\epsilon$ → exploration
* $1 - \epsilon$ → exploitation

### Q-Learning
* Model-free
* Off-policy
* Learns Q-values
* Can derive optimal policy

### Policy Optimization
* Directly optimizes policy
* Uses parameters $\theta$
* Useful for complex/continuous action spaces

---

## 💡 Exam Shortcut

For a **10-mark Q-Learning question**, remember this sequence:
**Definition → Q-table → Q-value → Update formula → Explain parameters → Numerical example → Algorithm → $\epsilon$-greedy → Model-free/off-policy → Applications**

### One-line memory trick:
> **Q-Learning = Try → Get reward → Update Q → Choose better action → Repeat.**

> **Next: Topic 13 — Multi-Step Task Decomposition**, where we move from individual RL decisions to how an Agentic AI breaks a large goal into smaller executable tasks.
