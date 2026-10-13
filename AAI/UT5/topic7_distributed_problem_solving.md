# Topic 7: Distributed Problem Solving (DPS) — 10 Marks

## 1. ELI5 — What is Distributed Problem Solving?

Imagine your university is planning a massive convocation ceremony for 10,000 graduates:
* A single person trying to seat every student, design stage lighting, organize food catering, manage security, and coordinate dignitary speeches would face **cognitive overload and computational collapse**.
* Instead, the problem is **divided into manageable subproblems**:
  * **Team 1** creates the seating chart for graduates.
  * **Team 2** designs stage lighting and audio.
  * **Team 3** arranges catering schedules.
  * **Team 4** coordinates security access checkpoints.

Each team solves its local problem in parallel. However, **solving the parts in isolation is not enough**: Team 1 cannot place seats over the electrical cables laid by Team 2, and Team 4 must approve VIP access routes. The teams must exchange constraints and combine their local plans into a unified, conflict-free master schedule.

In Artificial Intelligence, this paradigm is known as **Distributed Problem Solving (DPS)**.

```text
                           COMPLEX GLOBAL PROBLEM
                                      │
                         Decomposition Phase (Divide)
                                      ▼
     ┌────────────────────────────────┼────────────────────────────────┐
     ▼                                ▼                                ▼
[Subproblem 1]                 [Subproblem 2]                 [Subproblem 3]
Agent A Solves                 Agent B Solves                 Agent C Solves
     │                                │                                │
     └────────────────────────────────┼────────────────────────────────┘
                                      ▼
                      Coordination & Synthesis (Combine)
                                      ▼
                           UNIFIED GLOBAL SOLUTION
```

### Exam Definition:
> **Distributed Problem Solving (DPS)** is a subfield of Distributed Artificial Intelligence (DAI) where a network of loosely coupled, cooperative autonomous agents share computational responsibility to solve a complex global problem by **decomposing it into subproblems, solving them concurrently, and synthesizing local solutions into an integrated global result**.

---

## 2. The 4-Stage Lifecycle of DPS

Every formal DPS architecture executes four sequential, iterative phases:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. PROBLEM DECOMPOSITION : Partition global problem into sub-goals    │
├────────────────────────────────────────────────────────────────────────┤
│ 2. SUBPROBLEM ALLOCATION : Distribute subproblems to capable agents    │
├────────────────────────────────────────────────────────────────────────┤
│ 3. LOCAL PROBLEM SOLVING : Agents compute partial solutions in parallel│
├────────────────────────────────────────────────────────────────────────┤
│ 4. SOLUTION SYNTHESIS    : Combine and reconcile local results         │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Problem Decomposition:** Breaking down a high-dimensional problem into smaller, semi-independent subproblems (using functional, spatial, or temporal partitioning).
2. **Subproblem Allocation:** Assigning partitioned sub-tasks to individual agents equipped with appropriate domain tools and domain expertise.
3. **Local Problem Solving:** Agents independently search local state spaces using internal search algorithms (e.g., $A^*$, heuristic planning, constraint solvers).
4. **Solution Synthesis & Integration:** The most difficult phase. Agents exchange partial solutions, verify interface boundaries, resolve cross-agent constraint conflicts, and assemble the final coherent global solution.

---

## 3. Architectural Models of DPS

```text
                             DPS ARCHITECTURES
                                     │
     ┌───────────────────────────────┼───────────────────────────────┐
     ▼                               ▼                               ▼
[Hierarchical DPS]          [Blackboard Systems]         [Cooperative Peer-to-Peer]
Master decomposes;          Shared global workspace;     Decentralized negotiation;
Workers execute & report    Opportunistic updates        Direct inter-agent messaging
```

### A. Hierarchical DPS
* A designated supervisor node decomposes the overarching problem, delegates subproblems down a tree hierarchy, and merges outputs as they filter back up.
* **Best Used For:** Industrial manufacturing pipelines, military command chains.

### B. Blackboard Architecture (E.g., Hearsay-II)
* Agents (termed *Knowledge Sources*) do not communicate point-to-point. Instead, they interact through a **shared centralized memory structure (the Blackboard)**.
* When an agent observes partial data on the blackboard that matches its expertise, it triggers an action, computes an update, and writes its hypothesis back to the blackboard for others to build upon.

### C. Fully Decentralized Peer-to-Peer DPS
* Agents communicate asynchronously over message channels. No agent has a global system view; the global solution emerges through iterative consensus protocols.

---

## 4. Mathematical Modeling: Distributed Constraint Satisfaction (DisCSP)

Many DPS problems are formalized mathematically as a **Distributed Constraint Satisfaction Problem (DisCSP)** or **Distributed Constraint Optimization Problem (DCOP)**.

### Mathematical Formulation:
A DisCSP is defined as a 4-tuple: $\langle \mathcal{A}, \mathcal{X}, \mathcal{D}, \mathcal{C} \rangle$
* $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$: A set of $n$ autonomous agents.
* $\mathcal{X} = \{x_1, x_2, \dots, x_m\}$: A set of variables, where each variable $x_j$ belongs to an agent $A_i$.
* $\mathcal{D} = \{D_1, D_2, \dots, D_m\}$: The discrete domains of possible values for each variable.
* $\mathcal{C} = \{C_1, C_2, \dots, C_k\}$: A set of constraints restricting valid combinations of variable assignments.
  * **Intra-Agent Constraints:** Constraints involving only variables owned by a single agent.
  * **Inter-Agent Constraints:** Constraints involving variables owned by different agents (requiring inter-agent communication).

### Objective:
Find a global variable assignment $X^* \in \mathcal{D}_1 \times \dots \times \mathcal{D}_m$ such that **all constraints $C \in \mathcal{C}$ are satisfied**:

$$\text{Find } x \quad \text{such that} \quad C_k(x) = \text{True} \quad \forall k$$

* **Core Distributed Algorithms:**
  * **Asynchronous Backtracking (ABT):** Agents assign values asynchronously and exchange messages (`OK?` and `NOGOOD`) to resolve inter-agent constraint violations.
  * **Asynchronous Weak-Commitment Search (AWC):** Dynamically alters agent priority orders to escape local search deadlocks.

---

## 5. DPS vs. Task Allocation vs. Multi-Agent Systems (MAS)

Students frequently confuse these three related concepts in examinations:

| Dimension | Distributed Problem Solving (DPS) | Task Allocation | General Multi-Agent Systems (MAS) |
| :--- | :--- | :--- | :--- |
| **Scope** | Complete end-to-end problem decomposition and synthesis | Pure mapping of tasks to specific agents | Broad umbrella discipline covering all multi-agent interaction |
| **Agent Relationship** | **Strictly Cooperative** (Designed for a shared mission) | Can be cooperative or competitive (auctions) | Can be cooperative, competitive, or self-interested |
| **Primary Output** | An **integrated solution** (e.g., flight plan, timetable) | An **assignment matrix** ($x_{ij} \in \{0, 1\}$) | Emergent system behaviors / game outcomes |
| **Core Hurdle** | Synthesis & cross-subproblem constraint violations | Optimal utility matching & load balancing | Alignment, trust, communication protocols |

> **Key Rule of Thumb:** Task Allocation is often just **Stage 2** within the broader Distributed Problem Solving lifecycle!

---

## 6. Concrete Worked Example: City-Wide Urban Route Planning

**Problem:** Find an optimal route from Airport ($A$) to City Center ($Z$) across three autonomous regional traffic sectors ($R_1, R_2, R_3$).

```text
  SECTOR 1 (Agent A)                SECTOR 2 (Agent B)                SECTOR 3 (Agent C)
┌───────────────────────┐         ┌───────────────────────┐         ┌───────────────────────┐
│ Airport (A)           │         │ Highway Crossing (H)  │         │ Gateway (G)           │
│   │                   │         │   │                   │         │   │                   │
│   ▼ (8 mins)          │         │   ▼ (12 mins)         │         │   ▼ (5 mins)          │
│ Checkpoint X ─────────┼────────►│ Checkpoint Y ─────────┼────────►│ City Center (Z)       │
└───────────────────────┘         └───────────────────────┘         └───────────────────────┘
```

### Execution Pipeline:
1. **Decomposition:** The metropolitan transit grid is partitioned spatially into three geographic sectors ($R_1, R_2, R_3$), assigned to Agents $A, B, C$.
2. **Local Optimization:**
   * Agent $A$ finds the fastest path inside Sector 1: $A \to X$ ($8\text{ mins}$).
   * Agent $B$ finds the fastest path inside Sector 2: $H \to Y$ ($12\text{ mins}$).
   * Agent $C$ finds the fastest path inside Sector 3: $G \to Z$ ($5\text{ mins}$).
3. **The Boundary Disconnection Trap (Synthesis Failure):**
   * Agent $A$'s exit is Checkpoint $X$, but Agent $B$'s fastest entry point is Highway Crossing $H$!
   * $X$ does not connect directly to $H$. If the agents simply glued their independently optimal local paths together, the route would be physically discontinuous.
4. **Coordination & Synthesis Phase:**
   * Agent $A$ and Agent $B$ exchange boundary interface nodes.
   * Agent $B$ re-evaluates its local routing starting from entry node $X$. It finds a slightly slower path $X \to Y$ ($14\text{ mins}$).
   * The integrated route is now globally continuous:
     $$\text{Total Time} = T(A \to X) + T(X \to Y) + T(Y \to Z) = 8 + 14 + 5 = 27\text{ mins}$$
   * **Crucial Takeaway:** A collection of locally optimal solutions does not guarantee a globally optimal (or even feasible) solution without coordination at boundaries!

---

## 7. Advantages and Limitations of DPS

### Advantages:
* **High Computational Parallelism:** Decomposing NP-hard problems allows distributed machines to search state spaces concurrently.
* **Fault Tolerance & Reliability:** If Agent 3 crashes, Agents 1 and 2 can continue solving their subproblems while a replica node boots up.
* **Natural Mapping to Distributed Physical Problems:** Matches inherently distributed systems like power grids, factory floors, and supply chains.

### Limitations:
* **The Integration / Synthesis Bottleneck:** Merging conflicting partial plans often requires expensive iterative backtracking.
* **Communication Latency:** High network bandwidth consumption when agents repeatedly negotiate boundary constraints.
* **Sub-Optimality (Myopic Bias):** Agents optimizing strictly for local objectives may miss globally superior solutions.

---

## 8. Summary & Exam-Ready Structure

When answering a 10-mark question on Distributed Problem Solving:
1. **Define DPS:** Use the core phrase: *Decompose $\to$ Solve Locally $\to$ Coordinate $\to$ Synthesize*.
2. **Detail the 4 Stages:** Explain Problem Decomposition, Allocation, Local Solving, and Synthesis.
3. **Explain DisCSP:** Write down the 4-tuple $\langle \mathcal{A}, \mathcal{X}, \mathcal{D}, \mathcal{C} \rangle$ and distinguish between intra-agent and inter-agent constraints.
4. **Provide the Difference Table:** Contrast DPS vs. Task Allocation vs. MAS.
5. **Give the Worked Example:** Walk through the urban route planning case study and highlight the boundary disconnection trap.
6. **List Pros, Cons, and Applications.**

---

## 9. Quick Revision Sheet

* **DPS:** Cooperatively solving a single large problem via division of labor and solution synthesis.
* **4-Step Pipeline:** Decompose $\to$ Allocate $\to$ Solve $\to$ Synthesize.
* **DisCSP:** Variables and constraints distributed across multiple agents; solved via Asynchronous Backtracking (ABT).
* **The Boundary Problem:** Locally optimal sub-solutions can be globally incompatible without coordination.
* **Blackboard Architecture:** A shared global data structure through which independent expert agents communicate opportunistically.

### 🧠 One-line memory trick
> **Decompose the challenge, solve the pieces in parallel, and reconcile the seams to build the whole!**

---

## 10. Active Recall & Self-Evaluation (Q&A)

### Q1. What is Distributed Problem Solving (DPS)?
* **Answer:** Distributed Problem Solving is an approach within Distributed AI where multiple cooperative autonomous agents collaboratively solve a complex problem by dividing it into smaller subproblems, solving them concurrently, and synthesizing the partial solutions into an integrated global result.

### Q2. Differentiate DPS from Task Allocation.
* **Answer:**
  * **Task Allocation** is the specific assignment process of deciding *which agent executes which task* based on cost, bids, or capabilities.
  * **DPS** is the broader, complete end-to-end problem-solving lifecycle that includes problem decomposition, task allocation, local algorithmic solving, constraint management, and final solution synthesis.

### Q3. Why must agents coordinate when combining their local solutions?
* **Answer:** Because subproblems in real-world systems are rarely completely independent. Subproblems share boundary interfaces, physical resources, and timing constraints. If agents do not coordinate during synthesis, locally optimal solutions will clash, creating deadlocks, incompatible connections, or unfeasible global solutions.

### Q4. Practical: Three agents independently plan different sections of a delivery route. Their individual sections are efficient, but two sections do not connect. What went wrong, and how should the agents fix it?
* **Answer:**
  * **What went wrong:** The agents suffered from **myopic local optimization without boundary constraint synchronization**. They optimized their internal paths in isolation, ignoring the inter-agent constraints governing the shared interface checkpoints between regions.
  * **How to fix it:** The agents must execute a **Distributed Constraint Satisfaction Protocol (such as ABT)**. The first agent transmits its chosen exit checkpoint to the second agent. The second agent treats that checkpoint as a mandatory entry constraint and replans its internal path from that specific node, guaranteeing a continuous, globally valid trajectory.
