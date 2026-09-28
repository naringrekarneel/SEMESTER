# Topic 15: Connecting Search, Planning and Reinforcement Learning in Agentic AI

This is the **final topic** in our Agentic AI roadmap. The goal here is to understand how all the concepts we've studied work together to create an intelligent agent.

---

## 1. Big Picture — ELI5

Think of an AI agent as a person trying to complete a difficult task.

It needs three major abilities:

### Search
> **“What possible path can I take?”**

### Planning
> **“What sequence of actions should I perform?”**

### Reinforcement Learning
> **“Which decisions tend to give better results?”**

Agentic AI combines these capabilities to solve complex, multi-step problems.

---

## 2. Search, Planning and RL

| Technique | Main Question | Purpose |
| :--- | :--- | :--- |
| **Search** | Which path can reach the goal? | Find a solution/path |
| **Planning** | What actions should I perform and in what order? | Construct an action sequence |
| **RL** | Which actions give better long-term rewards? | Learn better decisions |
| **MDP** | How can decisions be modeled under uncertainty? | Model sequential decision-making |
| **Policy** | What should I do in this state? | Select actions |
| **Task Decomposition** | How can I break this large goal into smaller tasks? | Manage complexity |

---

## 3. Search in Agentic AI

Search algorithms explore possible states and actions.

For example:
```text
Start
  ↓
 ┌───────┐
 ↓       ↓
 A       B
 ↓       ↓
 C       D
  \     /
    Goal
```

The agent searches for a path from:
$$Initial\ State \rightarrow Goal\ State$$

Examples:
* BFS
* DFS
* Uniform Cost Search
* Greedy Best-First Search
* A*

A* uses:
$$f(n) = g(n) + h(n)$$
where:
* **$g(n)$** = cost already spent
* **$h(n)$** = estimated remaining cost

---

## 4. Planning in Agentic AI

Planning focuses on constructing an **action sequence** that achieves a goal.

Example:
> Goal: Make coffee.

```text
Get Cup
   ↓
Add Coffee
   ↓
Boil Water
   ↓
Pour Water
   ↓
Add Sugar
   ↓
Coffee Ready
```

Classical planning can represent:
$$P = (S, A, s_0, G)$$
where:
* **$S$** = states
* **$A$** = actions
* **$s_0$** = initial state
* **$G$** = goal

---

## 5. Reinforcement Learning in Agentic AI

RL is useful when the agent must **learn from experience**.

The basic interaction is:
```text
State
 ↓
Action
 ↓
Environment
 ↓
Reward
 ↓
New State
 ↓
Action
 ↓
...
```

The objective is to maximize cumulative reward:
$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots$$

RL is particularly useful when:
* The environment is uncertain.
* The correct strategy isn't known beforehand.
* The agent can learn through repeated interaction.

---

## 6. Combining Them

Now let's combine the three.

```text
                 USER GOAL
                     ↓
             Task Decomposition
                     ↓
                  Planning
                     ↓
              Search / A*
                     ↓
              Select Actions
                     ↓
                Execute
                     ↓
             Observe Environment
                     ↓
               Reward / Result
                     ↓
                    RL
                     ↓
            Improve Decision Policy
                     ↓
              Better Future Actions
```

This creates a much more capable agent than using any single technique alone.

---

## 7. Example — Autonomous Delivery Robot

Suppose the goal is:
> **Deliver a package to Building C.**

### Step 1 — Task Decomposition
Break the task into:
```text
Deliver Package
    ↓
Navigate to Building C
    ↓
Avoid obstacles
    ↓
Reach destination
    ↓
Deliver package
```

### Step 2 — Search
The robot searches for a route.
Possible algorithms: BFS, Dijkstra/UCS, A*

Suppose A* finds:
```text
Start
 ↓
A
 ↓
B
 ↓
D
 ↓
Building C
```

### Step 3 — Planning
The robot creates an action sequence:
$$Move(A) \rightarrow Move(B) \rightarrow Move(D) \rightarrow Deliver$$

### Step 4 — Execution
The robot begins following the plan.
But then something happens:
> **A path becomes blocked.**

The original plan is no longer valid.

### Step 5 — Replanning
The agent observes the environment:
```text
Obstacle detected
       ↓
Current plan invalid
       ↓
Search for alternative route
       ↓
New plan
       ↓
Continue
```

### Step 6 — Reinforcement Learning
Over repeated deliveries, the robot learns:
> “This route is frequently blocked.”

It can update its policy so that it avoids that route in the future.
This is where **RL improves long-term behavior**.

---

## 8. Search vs Planning vs RL — Example

Imagine an AI playing a game.

### Search
Looks through possible moves:
```text
Move A
Move B
Move C
```
and evaluates possible paths.

### Planning
Creates a sequence:
```text
Collect weapon → Enter room → Defeat enemy → Reach exit
```

### RL
Learns:
> “Using this strategy usually gives higher rewards.”

So:
```text
Search → Find possible solutions
Planning → Organize actions
RL → Learn which decisions work best
```

---

## 9. Role of MDP

MDP provides the mathematical framework connecting decision-making and RL.

Recall:
$$M = (S, A, P, R, \gamma)$$

The agent has states, actions, transition probabilities, rewards, and a discount factor.
The policy then determines $\pi(a|s)$ and the agent attempts to maximize long-term reward.

---

## 10. Role of Value Functions

Value functions help the agent evaluate future consequences.

State value:
$$V^\pi(s) = E_\pi[G_t | S_t = s]$$

Q-value:
$$Q^\pi(s,a) = E_\pi[G_t | S_t = s, A_t = a]$$

So the agent can reason:
> “If I take this action now, how valuable is the resulting situation?”

---

## 11. Role of Q-Learning

Q-Learning allows an agent to learn action values from experience.

Its update rule is:
$$Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$$

The agent gradually learns which actions tend to produce better long-term outcomes.

---

## 12. Complete Agentic AI Architecture

A simplified architecture can look like this:

```text
                 USER GOAL
                     ↓
            Goal Understanding
                     ↓
             Task Decomposition
                     ↓
                 Planner
                     ↓
           ┌─────────┴─────────┐
           ↓                   ↓
        Search              Policy/RL
           ↓                   ↓
           └─────────┬─────────┘
                     ↓
                Action Selection
                     ↓
                  Tool Use
                     ↓
                Environment
                     ↓
             Observation/Result
                     ↓
                  Evaluation
                     ↓
             ┌───────┴───────┐
             ↓               ↓
          Success          Failure
             ↓               ↓
        Next Task          Replan
             ↓               ↓
             └───────←───────┘
```

This is the core idea behind many **agentic systems**.

---

## 13. Why Combine These Techniques?

No single technique is ideal for every situation.

### Search is good for:
* Finding paths
* Exploring possible states
* Structured problems

### Planning is good for:
* Goal-oriented tasks
* Action sequencing
* Tasks with known conditions/effects

### RL is good for:
* Learning from experience
* Uncertainty
* Long-term decision making

### Task decomposition is good for:
* Complex goals
* Multi-step workflows
* Hierarchical tasks

Combining them allows an agent to handle more complex environments.

---

## 14. Real-World Agentic AI Example

Consider an AI software-development agent.

User says:
> **“Build a web application and deploy it.”**

The agent can perform:
```text
User Goal
   ↓
Task Decomposition
   ↓
Requirements
   ↓
Planning
   ↓
Search/select implementation approach
   ↓
Generate Code
   ↓
Run Tests
   ↓
Observe Results
   ↓
Error?
  ↙    ↘
Yes     No
 ↓       ↓
Fix    Continue
 ↓       ↓
Test   Deploy
  \      /
   ↓    ↓
   Final Application
```

If the agent performs this task repeatedly, RL-style feedback can potentially help improve future decisions about strategies or action selection.

---

## 15. Important Exam Comparison

| Feature | Search | Planning | Reinforcement Learning |
| :--- | :--- | :--- | :--- |
| **Main goal** | Find solution/path | Create action sequence | Learn good decisions |
| **Learning required** | No | Usually no | Yes |
| **Environment** | Usually modeled | Usually modeled | Can be unknown |
| **Uncertainty** | Limited depending on method | Usually handled explicitly only in extensions | Naturally supported |
| **Feedback** | Path cost/goal | Goal achievement | Rewards |
| **Example** | A* | STRIPS | Q-Learning |
| **Output** | Path/solution | Plan | Policy/value function |

---

## 16. Final Agentic AI Loop

The complete concept we've studied can be summarized as:

$$\boxed{Goal \rightarrow Decompose \rightarrow Plan \rightarrow Search \rightarrow Act \rightarrow Observe \rightarrow Evaluate \rightarrow Learn \rightarrow Replan}$$

This is the big picture.

---

## 🎓 Final Revision Sheet — Entire Syllabus

| Topic | One-line meaning |
| :--- | :--- |
| **Problem Solving by Search** | Find a path from initial state to goal |
| **State-Space Representation** | Represent possible states and transitions |
| **BFS** | Search level-by-level |
| **DFS** | Search deeply before backtracking |
| **UCS** | Expand lowest path cost |
| **Greedy Search** | Use estimated cost $h(n)$ |
| **A\*** | Use $f(n) = g(n) + h(n)$ |
| **Classical Planning** | Construct actions to achieve a goal |
| **STRIPS** | Represent actions using preconditions/effects |
| **RL** | Learn decisions from rewards |
| **MDP** | Model sequential decisions under uncertainty |
| **Value Function** | Estimate long-term value of a state |
| **Q-Function** | Estimate value of an action in a state |
| **Bellman Equation** | Current value = reward + discounted future value |
| **Policy** | Strategy for choosing actions |
| **Q-Learning** | Learn optimal Q-values from experience |
| **Task Decomposition** | Break large goals into smaller tasks |
| **Multi-Step Execution** | Plan, execute, observe and adapt |
| **Agentic AI** | Combine these capabilities to achieve goals autonomously |

### The five formulas worth memorizing

1. **A\***: $f(n) = g(n) + h(n)$
2. **Return**: $G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots$
3. **MDP**: $M = (S, A, P, R, \gamma)$
4. **Bellman**: $V(s) = R(s,a) + \gamma V(s')$
5. **Q-Learning**: $Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$

### 💡 Final Memory Trick
> **SEARCH** finds a path.
> **PLANNING** creates a strategy.
> **POLICY** chooses actions.
> **RL** learns from experience.
> **DECOMPOSITION** breaks big goals into smaller ones.
> **AGENTIC AI** combines them to **plan → act → observe → learn → adapt**.
