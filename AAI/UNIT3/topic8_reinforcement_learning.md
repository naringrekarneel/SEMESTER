# Topic 8: Reinforcement Learning for Agents
**Module 3 | Very important for Agentic AI**

Now we move from **planning** to **learning**.

In classical planning, the agent is usually given a model of the environment. In Reinforcement Learning, the agent can **learn what actions are useful by interacting with the environment**.

---

## 1. What is Reinforcement Learning?

**Definition (exam-ready):**
> Reinforcement Learning (RL) is a machine learning approach in which an agent learns to make decisions by interacting with an environment and receiving rewards or penalties for its actions.

The objective is to learn a strategy that maximizes the **cumulative reward** over time.

### ELI5

Imagine training a dog.
* Dog sits → you give a treat.
* Dog does something undesirable → no treat or negative feedback.
* Over time, the dog learns which actions produce better outcomes.

RL works similarly.

```text
        Action
Agent ───────────→ Environment
  ↑                     │
  │                     │
  └── State + Reward ←──┘
```

The agent repeatedly interacts with the environment and learns from the feedback.

---

## 2. Main Components of RL

There are five major components.

| Component | Meaning | Example |
| :--- | :--- | :--- |
| **Agent** | Learner/decision maker | Robot |
| **Environment** | World in which agent operates | Room |
| **State** | Current situation | Robot at position A |
| **Action** | Choice made by agent | Move right |
| **Reward** | Feedback from environment | +10 for reaching goal |

### Example: Game-playing agent
Suppose an AI is playing a game.

```text
Agent → Move Right → Game
                    ↓
                 Reward +1
                    ↓
Agent ← New State ← Game
```

The agent learns which moves tend to produce higher rewards.

---

## 3. RL Interaction Cycle

The basic RL loop is:

```text
        ┌──────────────┐
        │    Agent     │
        └──────┬───────┘
               │
             Action
               ↓
        ┌──────────────┐
        │ Environment  │
        └──────┬───────┘
               │
        State + Reward
               ↓
        ┌──────────────┐
        │    Agent     │
        └──────────────┘
```

Step-by-step:
1. Agent observes the current state.
2. Agent selects an action.
3. Environment executes the action.
4. Environment returns a new state.
5. Agent receives a reward.
6. Agent updates its knowledge.
7. Repeat.

---

## 4. The Goal of Reinforcement Learning

The agent doesn't simply try to maximize the **immediate reward**.
It tries to maximize the **long-term cumulative reward**.

The return from time $t$ is:
$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots$$

where:
* **$G_t$** = return
* **$R_{t+1}$** = reward received after the next action
* **$\gamma$** = discount factor
* **$0 \leq \gamma \leq 1$**

The discount factor determines how much the agent values future rewards.

---

## 5. Discount Factor

The discount factor $\gamma$ is extremely important.

### If $\gamma$ is close to 0
The agent strongly prefers **immediate rewards**.

### If $\gamma$ is close to 1
The agent strongly considers **future rewards**.

For example:
```text
Immediate reward = 5
Future reward = 10
```

If $\gamma = 0.5$, then the discounted future reward is:
$$0.5 \times 10 = 5$$
So both have equal discounted value.

---

## 6. Worked Example

Suppose an agent receives the following rewards:
```text
Step 1 → +2
Step 2 → +4
Step 3 → +10
```

Let $\gamma = 0.5$.

The return from the beginning is:
$$G_0 = 2 + 0.5(4) + 0.5^2(10)$$

Therefore:
$$G_0 = 2 + 2 + 2.5$$
$$G_0 = 6.5$$

So the total discounted return is **6.5**.

---

## 7. Policy

A **policy** determines which action an agent should take in a given state.
It is represented by:
$$\pi(a|s)$$

This means:
> Probability of selecting action $a$ when the agent is in state $s$.

For a deterministic policy:
$$\pi(s) = a$$

Example:
```text
State: Robot at A

Policy:
If at A → Move Right
If at B → Move Right
If at C → Pick Up Object
```

The policy is essentially the agent's **decision-making strategy**.

---

## 8. Value Function

The value function measures how useful a state is in terms of expected future rewards.

It is represented as:
$$V^\pi(s)$$

It answers:
> "How good is it to be in state $s$ when following policy $\pi$?"

The value function is:
$$V^\pi(s) = E_\pi[G_t | S_t = s]$$

In simple terms:
**Value = expected future reward from a state.**

---

## 9. Action-Value Function

The action-value function, or **Q-function**, evaluates a particular action in a particular state.

$$Q^\pi(s,a)$$

It answers:
> "How good is it to perform action $a$ when I am in state $s$?"

For example:

| State | Action | Q-value |
| :--- | :--- | ---: |
| A | Left | 2 |
| A | Right | 8 |
| A | Up | 4 |

The agent would prefer **Right**, because:
$$Q(A, Right) = 8$$

This concept becomes extremely important when we study **Q-Learning**.

---

## 10. Exploration vs Exploitation

This is one of the most important RL concepts.

### Exploitation
Choose the action that currently appears to be the best.
> "I know Right gives good rewards, so I'll choose Right."

### Exploration
Try an unfamiliar action to discover whether it might be better.
> "Maybe Up is actually better. Let's try it."

The agent needs to balance both.
```text
Exploration
    ↕
Exploitation
```
* **Too much exploration** → agent wastes time trying poor actions.
* **Too much exploitation** → agent may never discover a better strategy.

---

## 11. Example: Robot Navigation

Imagine a robot learning to reach a charging station.

```text
Start
  ↓
Move Left → -1
Move Right → -1
Move Right → -1
Reach Charger → +10
```

Initially, the robot doesn't know which route is best.
Through repeated attempts, it learns:
```text
Action → Result → Reward
```

Eventually it develops a policy that tends to select actions leading toward the charger.
This is fundamentally different from classical planning.

---

## 12. Classical Planning vs Reinforcement Learning

Very important comparison:

| Classical Planning | Reinforcement Learning |
| :--- | :--- |
| Usually has a known model | Can learn from interaction |
| Actions have known effects | Effects/rewards can be learned |
| Searches for a plan | Learns a policy/value function |
| Usually goal-oriented | Optimizes cumulative reward |
| Deterministic assumptions are common | Can handle stochastic environments |
| Planning happens using an explicit model | Learning happens through experience |

### Simple distinction

**Planning:**
> "I know how the world works. Which actions should I perform?"

**RL:**
> "I'm not sure what works. I'll interact, receive rewards, and learn what actions are good."

---

## 13. RL in Agentic AI

Reinforcement learning can help agents improve their decision-making over repeated interactions.

For example, an AI agent may need to decide:
```text
User Request
     ↓
Possible Actions
   ↙ ↓ ↘
Tool A Tool B Tool C
   ↓
Outcome
   ↓
Reward / Feedback
   ↓
Improve Future Decisions
```

Potential applications include:
* Game-playing agents
* Robotics
* Autonomous navigation
* Recommendation systems
* Resource allocation
* Adaptive decision-making
* Tool-selection strategies in agent systems

---

## 📝 Quick Revision Sheet

### Reinforcement Learning — Must Remember

* RL is **learning through interaction and feedback**.
* **Agent** interacts with an **environment**.
* Agent observes a **state**.
* Agent chooses an **action**.
* Environment returns a **reward** and next state.
* The objective is to maximize **long-term cumulative reward**.
* Discounted return: $G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots$
* **Policy** tells the agent how to choose actions.
* **Value function** evaluates states.
* **Q-function** evaluates state-action pairs.
* RL must balance **exploration and exploitation**.

### One-line memory trick
> **State → Action → Reward → Learn → Better Action**

---

## 🧠 Active Learning

### Q1 — Conceptual
What is Reinforcement Learning? Explain the interaction between **agent and environment**.

### Q2 — Conceptual
What is the difference between **exploration and exploitation**?

### Q3 — Conceptual
Differentiate between **value function $V(s)$** and **Q-function $Q(s,a)$**.

### Q4 — Practical
An agent receives rewards:
```text
R₁ = 5
R₂ = 10
R₃ = 20
```

If the discount factor is $\gamma = 0.5$, calculate the discounted return from the beginning.

> *Reply with your answers or say **NEXT** to continue to **Topic 9: Markov Decision Process (MDP)**.*
