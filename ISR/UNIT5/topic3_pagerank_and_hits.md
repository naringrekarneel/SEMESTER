# PageRank and HITS Algorithms — 10 Marks

## 1. Introduction

**PageRank** and **HITS (Hyperlink-Induced Topic Search)** are link-analysis algorithms designed to rank web pages by evaluating the structure of directed hyperlinks on the World Wide Web. While PageRank computes a query-independent global authority score using random walks, HITS dynamically discovers query-dependent authoritative and directory resources using a mutual reinforcement relationship.

* **Real-World Examples & Use-Cases:**
  * **Google Search Engine:** Original foundational ranking metric for web indexing (PageRank).
  * **Academic Citation Networks:** Evaluating influential research papers and literature surveys (PageRank & HITS).
  * **Social Network Analysis & Recommendation Systems:** Identifying key influencers, hubs, and authoritative content creators on platforms like X and LinkedIn.
* **Major Components & Phases:**
  * **Graph Representation:** Directed graph modeling pages as nodes $V$ and hyperlinks as directed edges $E$.
  * **Base Subgraph Construction (HITS):** Query formulation, root set retrieval, and base set expansion.
  * **Matrix Formulation & Power Iteration:** Stochastic transition matrices, dampening factors, adjacency matrices, and eigenvector convergence.

---

## 2. Architecture & High-Level Overview

```text
[Web / Query Input]
        │
        ├───► [PageRank Pipeline: Query-Independent Global Graph]
        │           │
        │           ▼
        │     Transition Matrix M ──► Damping Factor (1-d)/N ──► Power Iteration (PR = M*PR) ──► Global PR Vector
        │
        └───► [HITS Pipeline: Query-Dependent Subgraph]
                    │
                    ▼
              Root Set (R) ──► Expanded Base Set (S) ──► Co-enforcement (a = A^T h, h = A a) ──► Top Hubs & Authorities
```

### Key Stages:
1. **Graph Extraction:** Extracts directed links where pages act as nodes and hyperlinks serve as directed edges conveying authority endorsements.
2. **Matrix Construction:** Constructs a column-stochastic transition matrix for PageRank and a focused adjacency matrix for HITS.
3. **Iterative Score Propagation:** Transfers link equity through repeated matrix-vector multiplications until convergence criteria ($\epsilon$) are met.
4. **Vector Normalization & Ranking:** Normalizes score vectors to prevent divergence and produces the final ranked list of resources.

---

## 3. Detailed Components & Modules

### 3.1 PageRank Algorithm (Brin & Page)

PageRank models a **Random Surfer** exploring the web graph, defining page importance as the stationary probability of visiting that page.

* **Random Surfer Model:** A user browses hyperlinks at random; with probability $d$ (damping factor, typically $0.85$), they follow an outbound link, and with probability $(1-d)$, they teleport to a random page on the web.
* **Handling Graph Anomalies:** Solves **Spider Traps** (surfer looping indefinitely) and **Dead Ends / Dangling Nodes** (pages with out-degree 0 draining rank) via uniform teleportation:

$$PR(u) = \frac{1-d}{N} + d \sum_{v \in In(u)} \frac{PR(v)}{L(v)}$$

where:
* $N$ = total number of web pages in the graph.
* $In(u)$ = set of pages pointing into page $u$.
* $L(v)$ = number of outbound links (out-degree) from page $v$.
* $d$ = damping factor ($0.85$).

* **Stochastic Transition Matrix:** Formulates the web as a column-stochastic matrix $M$ where $M_{ij} = 1 / L(j)$ if a link exists from $j$ to $i$, otherwise $0$.
* **Power Iteration:** Computes the dominant eigenvector corresponding to eigenvalue $\lambda = 1$ via iterative updates: $R_{k+1} = \mathbf{A} R_k$.

#### Toy Calculation Example:

| Page ($u$) | In-Links ($v$) | Out-Degree $L(v)$ | Initial $PR_0$ | Final Score ($PR$) |
| :--- | :--- | :--- | :--- | :--- |
| **A** | B, C | 2 | 0.33 | **0.39** |
| **B** | C | 1 | 0.33 | **0.21** |
| **C** | A | 1 | 0.33 | **0.40** |

---

### 3.2 HITS Algorithm (Kleinberg)

HITS is a query-dependent link analysis algorithm that decomposes web significance into two dual categories: **Authorities** (informative pages on a topic) and **Hubs** (directories pointing to authorities).

```text
       ┌───────────┐         Points to         ┌───────────────┐
       │   HUBS    │ ────────────────────────► │  AUTHORITIES  │
       │  h(p)     │ ◄──────────────────────── │     a(p)      │
       └───────────┘       Endorsed by         └───────────────┘
```

* **Focused Subgraph Generation:** Retrieves a top-$t$ "Root Set" ($R$) from a text index, then expands it into a "Base Set" ($S$) by including all nodes that $R$ points to and all nodes that point to $R$.
* **Mutual Reinforcement Mechanism:**
  * A page is a good **Authority** if pointed to by good Hubs:
    $$a(p) = \sum_{q \to p} h(q)$$
  * A page is a good **Hub** if it points to good Authorities:
    $$h(p) = \sum_{p \to q} a(q)$$
* **Matrix Formulation:** Given adjacency matrix $A$ of subgraph $S$:
  $$a_{k+1} = A^T h_k = A^T A a_k$$
  $$h_{k+1} = A a_{k+1} = A A^T h_k$$
* **Normalization:** After every iteration, vectors are normalized using the Euclidean norm: $\sum (a_i)^2 = 1$ and $\sum (h_i)^2 = 1$ to prevent unbounded growth.

| Page Type | Definition | Iteration Update Rule | Typical Web Examples |
| :--- | :--- | :--- | :--- |
| **Hub ($h$)** | Directory linking to good authorities | $h = A \cdot a$ | Yahoo Directory, curated link lists, resource portals |
| **Authority ($a$)** | Content-rich site endorsed by hubs | $a = A^T \cdot h$ | Wikipedia articles, primary research portals, official docs |

---

### 3.3 Key Differences: PageRank vs HITS

| Dimension | PageRank | HITS |
| :--- | :--- | :--- |
| **Query Dependency** | **Query-Independent** (Computed offline on entire web graph) | **Query-Dependent** (Computed online on focused subgraph) |
| **Scores Generated** | Single global authority score per URL | Dual scores per URL: Hub score ($h$) and Authority score ($a$) |
| **Computational Cost** | High offline cost; instant retrieval lookup at query time | Low graph size; high query-time runtime latency |
| **Graph Scope** | Entire indexed Web graph ($N$ in billions) | Local base set ($S \approx 1,000 - 5,000$ pages) |
| **Algorithm Class** | Random walk stationary distribution | Mutual reinforcement eigenvector analysis |

#### Advantages:
* **PageRank:** Immune to query-time processing bottlenecks; mathematically guaranteed to converge via the Perron-Frobenius theorem.
* **HITS:** Discovers authoritative niche topics and directories naturally without pre-ranking the entire global graph.

#### Limitations:
* **PageRank:** Susceptible to Link Farms and SEO manipulation; favors older, highly connected sites (new page problem).
* **HITS:** Prone to **Topic Drift** (subgraph dominated by popular unrelated links) and **Mutually Reinforcing Relationships** (two sites artificially inflating scores).

---

## 4. End-to-End Workflow & Execution Steps

```text
Step 1: Graph/Set Initialization
        • PageRank: Indexes global graph into N × N matrix. PR_0 = [1/N, 1/N, ...]^T.
        • HITS: Executes query, retrieves Root Set R, expands to Base Set S; h_0 = [1, ...]^T, a_0 = [1, ...]^T.

Step 2: Iterative Propagation
        • PageRank: Multiplies PR vector by Google matrix G = d*M + ((1-d)/N)*E.
        • HITS: Computes a_{k+1} = A^T * h_k and h_{k+1} = A * a_{k+1}.

Step 3: Normalization & Teleportation Adjustment
        • PageRank: Distributes teleportation probability (1-d)/N to handle dead-ends.
        • HITS: Normalizes vectors to unit length: a_{k+1} / ||a_{k+1}|| and h_{k+1} / ||h_{k+1}||.

Step 4: Convergence Check
        • Verifies ||V_{k+1} - V_k|| < ε. If not converged, returns to Step 2.

Step 5: Output Generation & Result Integration
        • PageRank scores are pre-indexed for rapid runtime lookup.
        • HITS outputs top authorities and hubs directly for the specific query.
```

---

## 5. Conclusion

**PageRank** and **HITS** represent the foundational cornerstones of modern graph-based Information Retrieval, shifting search algorithms from pure lexical matching to structural link endorsement. While PageRank delivers high runtime throughput via offline global computation, HITS offers fine-grained topical partitioning through its dual hub-and-authority paradigm.

### ⭐ Exam keywords
**PageRank → Random Surfer → Damping Factor ($d=0.85$) → Power Iteration → Spider Traps → Teleportation → HITS → Hubs & Authorities → Root Set → Base Set → Mutual Reinforcement → Topic Drift**

### 🧠 One-line memory trick
> **PageRank = Global random walk offline; HITS = Local Hubs pointing to Authorities online.**
