# Topic 5: A* Search Algorithm
**Module 1 | Very important: 10 marks**

## 1. What is A* Search?

**Definition (exam-ready):** A* (A-Star) is an informed search algorithm that finds a least-cost path from an initial state to a goal state by combining the actual cost incurred so far with the estimated remaining cost.

It combines the ideas of Uniform-Cost Search and Greedy Best-First Search.

### ELI5 explanation

Imagine you're travelling from Mumbai to Pune. You have two pieces of information:
* How much time you've already spent travelling.
* How much time you estimate it will take to reach Pune.

Instead of considering only one of these, A* adds them together and explores the route with the lowest estimated total travel time.

This helps A* balance the cost of the journey so far with the estimated cost of reaching the destination.

## 2. A* Evaluation Function

$$f(n) = g(n) + h(n)$$

* **$g(n)$**: Actual cost from start to current node
* **$h(n)$**: Estimated cost from current node to goal
* **$f(n)$**: Estimated total path cost

For example, suppose a node has an actual path cost of 6 and an estimated remaining cost of 4.
$$f(n) = 6 + 4 = 10$$

A* always selects the frontier node with the lowest $f(n)$.

## 3. How A* Works

1. Insert initial node into priority queue
2. Calculate $f(n) = g(n) + h(n)$
3. Select node with minimum $f(n)$
4. Check whether it is the goal
5. Generate successors and update their costs
6. Repeat until the goal is reached

A* uses a priority queue, commonly called the open list. It also maintains information about explored nodes, often called the closed list.

When a cheaper path to an existing node is discovered, its cost and parent information must be updated. Depending on the heuristic and implementation, a previously explored node may need to be reopened.

## 4. Step-by-Step Worked Example

Consider the following weighted graph. Edge labels represent actual travel costs, and each node has a heuristic value.

### A* Search Graph

![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20350%20240%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20fill%3D%22none%22%20stroke%3D%22currentColor%22%20stroke-width%3D%221.7%22%20opacity%3D%22.6%22%3E%3Cpath%20d%3D%22M35%20112%20L130%2043%20L230%2043%20L315%20112%22%2F%3E%3Cpath%20d%3D%22M35%20112%20L130%20188%20L230%20188%20L315%20112%22%2F%3E%3Cpath%20d%3D%22M130%2043%20L230%20188%22%2F%3E%3C%2Fg%3E%3Ctext%20x%3D%2277%22%20y%3D%2268%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22180%22%20y%3D%2230%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E4%3C%2Ftext%3E%3Ctext%20x%3D%22275%22%20y%3D%2272%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%2277%22%20y%3D%22168%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E5%3C%2Ftext%3E%3Ctext%20x%3D%22180%22%20y%3D%22205%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E1%3C%2Ftext%3E%3Ctext%20x%3D%22275%22%20y%3D%22166%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22173%22%20y%3D%22113%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%20font-weight%3D%22semibold%22%3E1%3C%2Ftext%3E%3Ccircle%20cx%3D%2235%22%20cy%3D%22112%22%20r%3D%2219%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%2235%22%20y%3D%22117%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3ES%3C%2Ftext%3E%3Ctext%20x%3D%2235%22%20y%3D%2287%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=5%3C%2Ftext%3E%3Ccircle%20cx%3D%22130%22%20cy%3D%2243%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22130%22%20y%3D%2248%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EA%3C%2Ftext%3E%3Ctext%20x%3D%22130%22%20y%3D%2218%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=3%3C%2Ftext%3E%3Ccircle%20cx%3D%22130%22%20cy%3D%22188%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22130%22%20y%3D%22193%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EB%3C%2Ftext%3E%3Ctext%20x%3D%22130%22%20y%3D%22163%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=3%3C%2Ftext%3E%3Ccircle%20cx%3D%22230%22%20cy%3D%2243%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22230%22%20y%3D%2248%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EC%3C%2Ftext%3E%3Ctext%20x%3D%22230%22%20y%3D%2218%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=3%3C%2Ftext%3E%3Ccircle%20cx%3D%22230%22%20cy%3D%22188%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22230%22%20y%3D%22193%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3ED%3C%2Ftext%3E%3Ctext%20x%3D%22230%22%20y%3D%22163%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=2%3C%2Ftext%3E%3Ccircle%20cx%3D%22315%22%20cy%3D%22112%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22315%22%20y%3D%22117%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EG%3C%2Ftext%3E%3Ctext%20x%3D%22315%22%20y%3D%2287%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=0%3C%2Ftext%3E%3C%2Fsvg%3E)

*Assume bidirectional edges. The heuristic values do not overestimate the true remaining costs.*

### Step 1: Start at S
The initial node has:
$$g(S) = 0,\quad h(S) = 5$$
$$f(S) = 0 + 5 = 5$$

Expand S and discover A and B.

| Node | g(n) | h(n) | f(n) |
| :--- | :--- | :--- | :--- |
| A | 2 | 3 | 5 |
| B | 5 | 3 | 8 |

A has the lowest estimated total cost, so expand A.

### Step 2: Expand A
From A, we can reach C and D.

For C:
$$g(C) = 2 + 4 = 6$$
$$f(C) = 6 + 3 = 9$$

For D:
$$g(D) = 2 + 1 = 3$$
$$f(D) = 3 + 2 = 5$$

The frontier now contains:

| Node | g(n) | h(n) | f(n) |
| :--- | :--- | :--- | :--- |
| D | 3 | 2 | 5 |
| B | 5 | 3 | 8 |
| C | 6 | 3 | 9 |

Expand D because it has the lowest $f(n)$.

### Step 3: Expand D
D connects to G and B.

For G:
$$g(G) = 3 + 2 = 5$$
$$f(G) = 5 + 0 = 5$$

A path to B through D would cost 4, improving its previous cost of 5. Update B accordingly.

| Node | g(n) | h(n) | f(n) |
| :--- | :--- | :--- | :--- |
| G | 5 | 0 | 5 |
| B | 4 | 3 | 7 |
| C | 6 | 3 | 9 |

Expand G.

### Step 4: Goal reached

> **Optimal path found**
> **S → A → D → G**
> Total path cost: $2 + 1 + 2 = 5$

Notice that A* considered both actual travel cost and estimated remaining cost throughout the search.

## 5. Admissible and Consistent Heuristics

These are two important concepts for understanding A* optimality.

### Admissible heuristic
A heuristic is admissible if it never overestimates the actual minimum remaining cost.
$$h(n) \leq h^*(n)$$
Here, $h^*(n)$ represents the true minimum cost from node $n$ to the goal.

For example, if the actual minimum remaining distance is 10 km, an admissible heuristic could estimate 7 km or 10 km, but not 12 km.

### Consistent heuristic
A heuristic is consistent if, for every transition from node $n$ to successor $n'$:
$$h(n) \leq c(n,n') + h(n')$$
Where $c(n,n')$ is the cost of moving from $n$ to $n'$.

Consistency ensures that the estimated total cost does not decrease along a path.

> **Must remember:** With an admissible heuristic, standard A* tree search is optimal under appropriate search assumptions. Graph-search A* that never reopens closed nodes generally requires a consistent heuristic for its optimality guarantee.

## 6. Common Heuristics

Two frequently used heuristics in grid-based pathfinding are Manhattan distance and Euclidean distance.

### Manhattan vs Euclidean Distance

| Manhattan distance | Euclidean distance |
| :---: | :---: |
| ![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20150%20145%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M15%2010%20V130%20M15%2010%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M45%2010%20V130%20M15%2040%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M75%2010%20V130%20M15%2070%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M105%2010%20V130%20M15%20100%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M135%2010%20V130%20M15%20130%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M15%20130%20H105%20V40%22%20stroke%3D%22%232563EB%22%20stroke-width%3D%224%22%20fill%3D%22none%22%20stroke-linejoin%3D%22round%22%2F%3E%3Ccircle%20cx%3D%2215%22%20cy%3D%22130%22%20r%3D%226%22%20fill%3D%22%232563EB%22%2F%3E%3Ccircle%20cx%3D%22105%22%20cy%3D%2240%22%20r%3D%226%22%20fill%3D%22%2316A34A%22%2F%3E%3C%2Fsvg%3E) | ![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20150%20145%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M15%2010%20V130%20M15%2010%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M45%2010%20V130%20M15%2040%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M75%2010%20V130%20M15%2070%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M105%2010%20V130%20M15%20100%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M135%2010%20V130%20M15%20130%20H135%22%20stroke%3D%22currentColor%22%20opacity%3D%22.15%22%20fill%3D%22none%22%2F%3E%3Cpath%20d%3D%22M15%20130%20L105%2040%22%20stroke%3D%22%239333EA%22%20stroke-width%3D%224%22%20fill%3D%22none%22%2F%3E%3Ccircle%20cx%3D%2215%22%20cy%3D%22130%22%20r%3D%226%22%20fill%3D%22%232563EB%22%2F%3E%3Ccircle%20cx%3D%22105%22%20cy%3D%2240%22%20r%3D%226%22%20fill%3D%22%2316A34A%22%2F%3E%3C%2Fsvg%3E) |
| $|x_2-x_1| + |y_2-y_1|$ | $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Horizontal and vertical movement | Straight-line distance |

For example, consider points (1, 2) and (4, 6).
* **Manhattan distance:** $|4-1| + |6-2| = 7$
* **Euclidean distance:** $\sqrt{3^2 + 4^2} = 5$

Manhattan distance is commonly used when movement is restricted to four directions. Euclidean distance is useful when straight-line movement is possible.

## 7. Properties of A*

| Property | Description |
| :--- | :--- |
| **Type** | Informed search |
| **Evaluation function** | $f(n) = g(n) + h(n)$ |
| **Data structure** | Priority queue |
| **Completeness** | Yes, under standard positive-cost and finite-branching assumptions |
| **Optimality** | Guaranteed with appropriate admissibility or consistency conditions |
| **Time complexity** | Exponential in the worst case |
| **Space complexity** | Exponential in the worst case |

A* can consume substantial memory because it maintains a frontier and information about explored states.

## 8. BFS vs UCS vs Greedy vs A*

| Algorithm | Evaluation criterion | Uses heuristic? | Optimality |
| :--- | :--- | :--- | :--- |
| **BFS** | Shallowest depth | No | Equal-cost edges |
| **UCS** | $g(n)$ | No | Yes, under suitable conditions |
| **Greedy** | $h(n)$ | Yes | Not guaranteed |
| **A\*** | $g(n) + h(n)$ | Yes | With suitable heuristic and search conditions |

> **Exam tip:** The key distinction is that UCS considers past cost, Greedy considers estimated future cost, and A* combines both.

---

## 📝 Quick Revision Sheet
**Topic 5 — Must Remember**

* A* is an informed search algorithm.
* Its evaluation function is $f(n) = g(n) + h(n)$.
* It expands the frontier node with the lowest estimated total cost.
* It uses a priority queue.
* An admissible heuristic never overestimates the true remaining cost.
* A consistent heuristic satisfies the triangle inequality.
* A* can find an optimal solution under suitable conditions, but its memory requirements can be high.

---

## 🧠 Active Learning — Test Yourself

**Q1.** Explain the A* evaluation function and the purpose of each component.
**Q2.** What is the difference between an admissible heuristic and a consistent heuristic?
**Q3.** Why can A* find an optimal path while Greedy Best-First Search cannot guarantee one?
**Q4. Practical:** Consider the following frontier in an A* search:

| Node | g(n) | h(n) |
| :--- | :--- | :--- |
| A | 4 | 6 |
| B | 7 | 2 |
| C | 3 | 5 |
| D | 6 | 5 |

Calculate $f(n)$ for each node and determine which node A* will expand next.

> *Reply with your answers, or say Next to continue to Topic 6: Introduction to Classical Planning.*
