# Topic 4: Greedy Best-First Search (GBFS)
**Module 1 | Important for exams: 7–10 marks**

## 1. What is Greedy Best-First Search?

**Definition (exam-ready):**
Greedy Best-First Search is an informed search algorithm that expands the node estimated to be closest to the goal using a heuristic function.

Unlike Uniform-Cost Search, which considers the cost already incurred, Greedy Best-First Search considers only the estimated remaining cost.

### ELI5 explanation

Imagine you're navigating a city and want to reach a railway station. At every intersection, you choose the road that appears to take you closest to the station.

You don't consider how far you've already travelled. You simply choose whichever option looks closest to your destination.

That's the idea behind Greedy Best-First Search.

However, the road that appears closest might contain traffic, obstacles or a long detour. Therefore, the greedy approach doesn't always produce the shortest path.

## 2. Heuristic Function

A heuristic function estimates the cost of reaching the goal from the current state.

It is represented as:
$$h(n)$$

Where:
* $n$ = Current node
* $h(n)$ = Estimated remaining cost from node $n$ to the goal

The evaluation function for Greedy Best-First Search is:

> **Greedy Best-First Search**
> $$f(n) = h(n)$$
> Always expand the frontier node with the smallest heuristic value.

### Example

Suppose the estimated distances to a destination are:

| Node | Heuristic $h(n)$ |
| :--- | :--- |
| A | 12 |
| B | 7 |
| C | 4 |
| D | 9 |
| Goal | 0 |

If all these nodes are available in the frontier, GBFS selects C because it has the lowest heuristic value.

> **Must remember:** A heuristic is an estimate, not necessarily the actual distance.

## 3. Algorithm

Greedy Best-First Search uses a priority queue to select the node with the lowest heuristic value.

1. Insert initial state into priority queue
2. Select node with minimum $h(n)$
3. Check whether it is the goal
4. If not, generate its successors
5. Calculate heuristic values
6. Insert eligible successors into queue
7. Repeat until the goal is found or the frontier becomes empty.

### Pseudocode

```python
def greedy_best_first_search(start, goal):
    frontier = PriorityQueue()
    frontier.put((h(start), start))

    visited = set()

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            return reconstruct_path(current)

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                frontier.put((h(neighbor), neighbor))

    return None
```

*This is simplified pseudocode; a complete implementation also stores parent information to reconstruct the solution path.*

## 4. Step-by-Step Worked Example

Consider the following graph. The numbers on the edges represent actual travel costs, while the numbers inside parentheses are heuristic estimates.

### Search graph

![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20350%20245%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20fill%3D%22none%22%20stroke%3D%22currentColor%22%20opacity%3D%22.6%22%20stroke-width%3D%221.7%22%3E%3Cpath%20d%3D%22M36%20115%20L125%2045%20L225%2045%20L310%20115%22%2F%3E%3Cpath%20d%3D%22M36%20115%20L125%20190%20L225%20190%20L310%20115%22%2F%3E%3C%2Fg%3E%3Ctext%20x%3D%2275%22%20y%3D%2270%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22175%22%20y%3D%2233%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%22272%22%20y%3D%2273%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E4%3C%2Ftext%3E%3Ctext%20x%3D%2275%22%20y%3D%22169%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E1%3C%2Ftext%3E%3Ctext%20x%3D%22175%22%20y%3D%22207%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22272%22%20y%3D%22170%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ccircle%20cx%3D%2236%22%20cy%3D%22115%22%20r%3D%2219%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%2236%22%20y%3D%22120%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3ES%3C%2Ftext%3E%3Ctext%20x%3D%2236%22%20y%3D%2290%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=7%3C%2Ftext%3E%3Ccircle%20cx%3D%22125%22%20cy%3D%2245%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22125%22%20y%3D%2250%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EA%3C%2Ftext%3E%3Ctext%20x%3D%22125%22%20y%3D%2220%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=3%3C%2Ftext%3E%3Ccircle%20cx%3D%22125%22%20cy%3D%22190%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22125%22%20y%3D%22195%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EB%3C%2Ftext%3E%3Ctext%20x%3D%22125%22%20y%3D%22165%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=5%3C%2Ftext%3E%3Ccircle%20cx%3D%22225%22%20cy%3D%2245%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22225%22%20y%3D%2250%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EC%3C%2Ftext%3E%3Ctext%20x%3D%22225%22%20y%3D%2220%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=2%3C%2Ftext%3E%3Ccircle%20cx%3D%22225%22%20cy%3D%22190%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22225%22%20y%3D%22195%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3ED%3C%2Ftext%3E%3Ctext%20x%3D%22225%22%20y%3D%22165%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=2%3C%2Ftext%3E%3Ccircle%20cx%3D%22310%22%20cy%3D%22115%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22310%22%20y%3D%22120%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EG%3C%2Ftext%3E%3Ctext%20x%3D%22310%22%20y%3D%2290%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3Eh=0%3C%2Ftext%3E%3C%2Fsvg%3E)

The algorithm chooses nodes using $h(n)$, not the actual edge costs.

### Step 1: Start at S
From S, the available successors are A and B.

| Node | Heuristic |
| :--- | :--- |
| A | 3 |
| B | 5 |

GBFS selects A because $h(A) = 3$ is smaller than $h(B) = 5$.

### Step 2: Expand A
A generates C, with $h(C) = 2$.
The frontier now contains:

| Node | Heuristic |
| :--- | :--- |
| B | 5 |
| C | 2 |

GBFS selects C.

### Step 3: Expand C
C generates G, with $h(G) = 0$.
GBFS selects G, and the goal is reached.

> **Goal reached**
> **S → A → C → G**
> Actual path cost: $2 + 3 + 4 = 9$

But consider the alternative route:
$S \rightarrow B \rightarrow D \rightarrow G$
Its actual cost is:
$1 + 2 + 2 = 5$

> **Important observation**
> Greedy Best-First Search returns a path costing 9, even though a path costing 5 exists.
> This demonstrates that GBFS is not guaranteed to find an optimal solution.

## 5. Advantages and Disadvantages

| Advantages | Disadvantages |
| :--- | :--- |
| Often reaches a goal quickly with a useful heuristic | Does not guarantee the optimal path |
| Uses heuristic information to guide exploration | Performance depends heavily on heuristic quality |
| Can avoid exploring many irrelevant states | May follow misleading estimates |
| Simple to implement using a priority queue | Can require substantial memory |

## 6. Properties of Greedy Best-First Search

| Property | Description |
| :--- | :--- |
| **Evaluation function** | $f(n) = h(n)$ |
| **Data structure** | Priority queue |
| **Complete** | With a finite graph and repeated-state checking |
| **Optimal** | No |
| **Time complexity** | $O(b^m)$ worst-case tree search |
| **Space complexity** | $O(b^m)$ worst-case tree search |

Here, $b$ is the branching factor and $m$ is the maximum search depth. Actual performance depends strongly on the heuristic and graph structure.

## 7. Comparison: UCS vs Greedy Best-First Search

| Feature | UCS | Greedy Best-First Search |
| :--- | :--- | :--- |
| **Evaluation function** | $g(n)$ | $h(n)$ |
| **Considers past cost** | Yes | No |
| **Considers estimated future cost** | No | Yes |
| **Uses a heuristic** | No | Yes |
| **Optimality** | Yes, under suitable cost assumptions | Not guaranteed |
| **Main objective** | Find the lowest-cost path | Reach the goal using heuristic guidance |

This comparison leads directly to A* Search, which combines the strengths of both approaches.

---

## 📝 Quick Revision Sheet
**Topic 4 — Must Remember**

* Greedy Best-First Search is an informed search algorithm.
* It selects the frontier node with the lowest heuristic value.
* Its evaluation function is $f(n) = h(n)$.
* It uses a priority queue.
* It ignores the cost already incurred.
* It is not guaranteed to return the shortest or lowest-cost path.
* Its performance depends on the quality of the heuristic.

---

## 🧠 Active Learning — Test Yourself

**Q1.** What is Greedy Best-First Search? Explain the role of its heuristic function.
**Q2.** Why does Greedy Best-First Search not guarantee an optimal solution?
**Q3.** Differentiate between Uniform-Cost Search and Greedy Best-First Search.
**Q4. Practical:** An agent has the following frontier:

| Node | Path cost $g(n)$ | Heuristic $h(n)$ |
| :--- | :--- | :--- |
| A | 3 | 8 |
| B | 7 | 2 |
| C | 2 | 5 |
| D | 5 | 4 |

Which node will Greedy Best-First Search expand next? Which node will UCS expand next? Explain your answer.

> *Reply with your answers, or say Next to continue to Topic 5: A* Search Algorithm.*
