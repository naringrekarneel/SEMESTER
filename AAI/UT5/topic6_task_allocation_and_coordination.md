# Topic 6: Task Allocation and Coordination in Multi-Agent Systems — 10 Marks

## 1. ELI5 — The Core Intuition

Imagine you and four classmates are chosen to organize your university's annual technical symposium:
* **The List of Tasks:**
  1. Build the online registration portal.
  2. Order food and catering.
  3. Set up audio-visual equipment in the auditorium.
  4. Coordinate corporate sponsors.
  5. Manage security and crowd control.

To pull this off without disaster, you must solve two distinct problems:
1. **Task Allocation:** *Who does what?* You assign the web developer to the portal, the outgoing negotiator to sponsors, and the sound technician to audio-visuals based on skills, availability, and capacity.
2. **Coordination:** *How do they work together smoothly?* Even if everyone knows their job, the sound team cannot set up until the stage is built; the registration team needs live updates on whether food passes are sold out; and emergency exits must be kept clear. Coordination ensures their actions synchronize in time and space without collisions or deadlocks.

```text
               MISSION SUCCESS: HOST TECH FESTIVAL
                                │
     ┌──────────────────────────┴──────────────────────────┐
     ▼                                                     ▼
[TASK ALLOCATION]                                     [COORDINATION]
"Who does what?"                                      "How and when do they sync?"
Assigns tasks to agents based on skills,              Resolves dependencies, resource contention,
capabilities, battery, and cost.                      timing bottlenecks, and spatial deadlocks.
```

### Exam Definitions:
> **Task Allocation** is the process of partitioning and mapping a set of tasks to a set of autonomous agents based on their capabilities, cost, availability, and utility functions.
>
> **Coordination** is the process of managing dependencies, communication, scheduling, and conflict resolution among multiple agents so that their collective actions align harmoniously toward global objectives.

---

## 2. Core Differences: Task Allocation vs. Coordination

| Dimension | Task Allocation (The "Who") | Coordination (The "How & When") |
| :--- | :--- | :--- |
| **Primary Question** | *"Which agent is responsible for which task?"* | *"How do agents execute tasks without interfering?"* |
| **Focus** | Resource assignment, matching, bidding | Synchronization, scheduling, conflict resolution |
| **Temporal Stage** | Solved **before** or at task assignment | Executed **during** and throughout runtime |
| **Typical Mechanism**| Auctions (CNP), Linear Programming, Matching | Plan merging, priority rules, mutual adjustment |
| **Failure Mode** | Suboptimal assignments, idle resources | Deadlocks, livelocks, spatial collisions, race conditions |
| **Real Example** | Assigning Delivery Robot #2 to Ward 4 | Ensuring Robot #1 yields to Robot #2 in a narrow doorway |

---

## 3. Mechanisms for Multi-Agent Task Allocation (MATA)

Task allocation models fall into three major structural paradigms:

```text
                     TASK ALLOCATION ARCHITECTURES
                                   │
     ┌─────────────────────────────┼─────────────────────────────┐
     ▼                             ▼                             ▼
[Centralized Allocation]     [Distributed Allocation]      [Market / Auction Based]
Single Master Node           Peer-to-Peer Negotiation     Contract Net Protocol
Global optimum; bottleneck   Robust; communication heavy   Decentralized bidding
```

### A. Centralized Task Allocation
* **Mechanism:** A single designated master/coordinator agent maintains a global state of all tasks and all agents. It solves an optimization problem (e.g., Hungarian algorithm, Mixed-Integer Linear Program) and assigns tasks directly.
* **Advantages:** Computes globally optimal assignments; easy to track and audit.
* **Limitations:** The central node is a **Single Point of Failure (SPOF)** and a computational bottleneck as $N$ scales.

### B. Distributed / Peer-to-Peer Task Allocation
* **Mechanism:** Agents use local communication to dynamically self-organize, trade tasks, or claim open tasks from shared environments without a master supervisor.
* **Advantages:** High fault tolerance; resilient to node dropouts; highly scalable.
* **Limitations:** May converge to locally suboptimal allocations; risk of race conditions where multiple agents claim the same task simultaneously.

### C. Market-Based / Auction Allocation (Contract Net Protocol)
* **Mechanism:** Tasks are modeled as commodities auctioned across a virtual marketplace. Agents calculate private cost/utility functions and submit competitive bids.

---

## 4. Benchmark Algorithm: Contract Net Protocol (CNP)

Developed by Reid G. Smith (1980), the **Contract Net Protocol (CNP)** is the international standard for distributed, market-based task allocation in MAS.

```text
   MANAGER AGENT                                                    CONTRACTOR AGENTS
         │                                                      Agent 1        Agent 2
         │─── 1. Call for Proposals (CFP: Spec, Deadline) ───────►│              │
         │────────────────────────────────────────────────────────┼─────────────►│
         │                                                        │              │
         │◄── 2. Submit Bid (Cost: 8m, Battery: 90%) ─────────────│              │
         │◄── 2. Submit Bid (Cost: 5m, Battery: 75%) ─────────────┼──────────────│
         │                                                        │              │
         │ [3. Manager Evaluates Bids: Agent 2 is Best!]          │              │
         │                                                        │              │
         │─── 4. Reject-Proposal ────────────────────────────────►│              │
         │─── 4. Accept-Proposal (Contract Awarded) ──────────────┼─────────────►│
         │                                                        │              │
         │                                                        │       [Executes Task]
         │                                                        │              │
         │◄── 5. Inform-Done (Task Finished / Results) ───────────┼──────────────│
         ▼                                                        ▼              ▼
```

### The 5 Formal Phases of CNP:
1. **Task Announcement (CFP):** The Manager broadcasts a formal Call for Proposals detailing task preconditions, requirements, and deadlines.
2. **Bidding:** Contractors evaluate the specification against their local state (distance, battery, tool availability) and return a `propose` message with a numerical bid (or `refuse`).
3. **Bid Evaluation:** The Manager evaluates incoming bids against an objective selection function.
4. **Contract Award:** The Manager sends an `accept-proposal` to the winning contractor and `reject-proposal` messages to all unselected candidates.
5. **Execution & Reporting:** The winning contractor executes the commitment and replies with an `inform-done` (or `failure`) performative.

---

## 5. Mathematical Formulation of the Assignment Problem

Formally, consider a system with $n$ agents ($A = \{a_1, a_2, \dots, a_n\}$) and $m$ tasks ($T = \{t_1, t_2, \dots, t_m\}$).

### Decision Variable:
Let $x_{ij} \in \{0, 1\}$ represent the binary assignment matrix:

$$x_{ij} = \begin{cases} 1 & \text{if agent } i \text{ is assigned to task } j \\ 0 & \text{otherwise} \end{cases}$$

### Cost / Utility Matrix:
Let $c_{ij} \ge 0$ denote the cost (e.g., time, battery, distance) incurred if agent $i$ performs task $j$.

### Optimization Objective (Cost Minimization):
$$\min_{X} \sum_{i=1}^{n} \sum_{j=1}^{m} c_{ij} x_{ij}$$

### Subject to Operational Constraints:
1. **Task Completeness Constraint:** Every task $j$ must be assigned to exactly one agent:
   $$\sum_{i=1}^{n} x_{ij} = 1 \quad \forall j \in \{1, 2, \dots, m\}$$
2. **Agent Capacity Constraint:** Each agent $i$ can execute at most $C_i$ tasks simultaneously:
   $$\sum_{j=1}^{m} x_{ij} \le C_i \quad \forall i \in \{1, 2, \dots, n\}$$

> When $n = m$ and $C_i = 1$, this reduces to the classical **Linear Sum Assignment Problem**, solvable in $O(n^3)$ polynomial time using the **Hungarian Algorithm**.

---

## 6. Multi-Agent Coordination Mechanisms

Once tasks are assigned, agents must execute them in a shared environment without conflicts.

```text
                         COORDINATION MECHANISMS
                                    │
     ┌──────────────────┬───────────┴───────────┬──────────────────┐
     ▼                  ▼                       ▼                  ▼
[Plan Merging]      [Priority Rules]        [Negotiation]      [Social Norms]
Combine local paths Preemptive rights for   Iterative trading  Hard constraints &
into conflict-free  emergency agents        of space/resources right-of-way rules
```

### 1. Plan Merging & Partial Global Planning (PGP)
* Agents construct individual candidate plans locally.
* They exchange plan summaries. Where routes overlap in space-time coordinates, a plan merger algorithm modifies arrival times or injects temporary holding delays to avoid collision.

### 2. Priority Rules & Preemption
* Strict hierarchy resolves deadlocks instantaneously.
* *Example:* In a hospital corridor, an **ICU Emergency Transport Agent** possesses priority level $\mathcal{P}=1$. A standard **Linen Delivery Agent** ($\mathcal{P}=5$) must pull into a side alcove and yield right-of-way.

### 3. Dynamic Replanning & Reactive Coordination
* If an unexpected obstacle (e.g., fallen debris) blocks an assigned path, the agent detects the blockage, updates its local cost graph, broadcasts an advisory warning to neighboring agents, and recalculates an alternate route.

---

## 7. Step-by-Step Worked Example: Warehouse Delivery

**Problem:** A logistics warehouse needs to allocate one high-priority delivery task ($T_{\text{urgent}}$). Three autonomous mobile robots submit bids:

| Robot | Travel Time ($t$) | Battery Level ($B$) | In-Transit Load ($L$) | Bid Score Formula: $S = t + 0.1(100 - B) + 2(L)$ |
| :---: | :---: | :---: | :---: | :--- |
| **Robot A** | $8\text{ min}$ | $90\%$ | $0\text{ packages}$ | $S_A = 8 + 0.1(10) + 0 = \mathbf{9.0}$ |
| **Robot B** | $5\text{ min}$ | $75\%$ | $1\text{ package}$ | $S_B = 5 + 0.1(25) + 2(1) = \mathbf{9.5}$ |
| **Robot C** | $6\text{ min}$ | $30\%$ | $0\text{ packages}$ | **Disqualified:** Battery $< 50\%$ safety floor |

### Evaluation:
* **Constraint Check:** Robot C fails the mandatory safety threshold ($B \ge 50\%$) and is eliminated.
* **Cost Evaluation:** Lower score indicates higher efficiency. Robot A scores $9.0$, beating Robot B's score of $9.5$.
* **Contract Award:** Manager issues `accept-proposal` to **Robot A**, while Robot B is sent a `reject-proposal`.

---

## 8. Advantages and Technical Challenges

### Advantages:
* **Optimal Resource Utilization:** Matches high-capability agents to complex tasks while keeping operational costs low.
* **High Adaptability:** Dynamic bidding adjusts instantly when agent availability or battery levels fluctuate.
* **Elimination of Bottlenecks:** Distributed auctions distribute computing loads across the entire agent collective.

### Technical Challenges:
* **The "Lying Bidder" Problem:** Self-interested agents may submit deceptive bids to hoard profitable tasks.
* **Deadlocks in Coordination:** Two robots entering a narrow doorway simultaneously can become stuck in an infinite yield loop (Livelock).
* **Communication Latency During Peak Traffic:** Thousands of concurrent CFP messages can saturate network bandwidth.

---

## 9. Conclusion

Task Allocation and Coordination form the twin computational pillars of Multi-Agent Systems. While **Task Allocation** matches agents to objectives using optimization models and market protocols like the **Contract Net Protocol**, **Coordination** orchestrates execution over time and space, preventing deadlocks and guaranteeing safe, unified multi-agent teamwork.

---

## 10. Quick Revision Sheet

* **Task Allocation:** *"Who does what?"* $\implies$ Matching tasks to agents based on capability & cost.
* **Coordination:** *"How & when do they work?"* $\implies$ Managing timing, dependencies, and spatial contention.
* **Contract Net Protocol (CNP):** Manager broadcasts CFP $\to$ Agents bid $\to$ Manager evaluates $\to$ Award contract $\to$ Inform-Done.
* **Mathematical Model:** Binary assignment matrix $x_{ij} \in \{0, 1\}$ subject to task completeness $\sum_i x_{ij} = 1$.
* **Coordination Tools:** Plan merging, priority rules, dynamic replanning, social norms.

### 🧠 One-line memory trick
> **Allocation assigns the contract; Coordination clears the hallway!**

---

## 11. Active Recall & Self-Evaluation (Q&A)

### Q1. What is the difference between task allocation and coordination in MAS?
* **Answer:** Task allocation is the initial assignment problem of determining which agent executes which task based on capabilities, cost, or bids. Coordination is the runtime synchronization process that manages dependencies, timing, communication, and resource contention so agents execute their assigned tasks without collisions or deadlocks.

### Q2. Describe the five main steps of the Contract Net Protocol (CNP).
* **Answer:**
  1. **Task Announcement (CFP):** Manager broadcasts task requirements to eligible contractors.
  2. **Bidding:** Contractors evaluate local availability and submit cost/time bids.
  3. **Bid Evaluation:** Manager compares bids against selection criteria.
  4. **Awarding:** Manager awards contract via `accept-proposal` to the winning bidder and sends `reject-proposal` to others.
  5. **Completion Report:** Winner executes task and reports results via `inform-done`.

### Q3. Write the mathematical objective and constraints of the basic multi-agent assignment problem.
* **Answer:**
  * **Objective:** Minimize total cost: $\min \sum_{i=1}^n \sum_{j=1}^m c_{ij} x_{ij}$
  * **Constraint 1:** Every task assigned to exactly one agent: $\sum_{i=1}^n x_{ij} = 1 \quad \forall j$.
  * **Constraint 2:** Agent capacity limit: $\sum_{j=1}^m x_{ij} \le C_i \quad \forall i$, with $x_{ij} \in \{0, 1\}$.

### Q4. Practical: Why would the lowest-cost bidder in a warehouse not always win a delivery contract?
* **Answer:** Cost alone ignores operational constraints such as battery safety thresholds, payload capacity, maintenance deadlines, or reliability history. For instance, a robot offering the fastest travel time may only have $15\%$ battery remaining; awarding it the task risks mid-route shutdown and corridor blockage.
