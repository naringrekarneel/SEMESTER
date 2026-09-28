# Topic 3: Uninformed Search Algorithms (BFS, DFS and UCS)
**Module 1 | Important for exams: 10 marks**

## 1. What is Uninformed Search?

**Definition:** Uninformed search, also called blind search, is an AI problem-solving technique that explores a state space without using heuristic information about how close a state is to the goal.

### ELI5 explanation

Imagine searching for your friend's house in an unfamiliar city without GPS.

You know where you are and how to recognize the house, but you don't know which road leads there.

You could explore all nearby roads first, follow one road as far as possible, or prioritize roads that have cost you the least travel time so far.

These three approaches correspond to BFS, DFS and UCS.

| Algorithm | Main strategy | Data structure |
| :--- | :--- | :--- |
| **BFS** | Explore level by level | Queue (FIFO) |
| **DFS** | Explore one branch deeply | Stack (LIFO) |
| **UCS** | Explore the lowest-cost path first | Priority queue |

## 2. Breadth-First Search (BFS)

BFS explores all nodes at the current depth before moving to the next depth.

It is useful when we want to find the shortest path in terms of the number of edges in an unweighted graph.

### BFS exploration

![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20340%20242%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20stroke%3D%22currentColor%22%20opacity%3D%22.4%22%20stroke-width%3D%221.6%22%20fill%3D%22none%22%3E%3Cpath%20d%3D%22M170%2027%20L87%20100%20M170%2027%20L253%20100%20M87%20100%20L40%20192%20M87%20100%20L132%20192%20M253%20100%20L208%20192%20M253%20100%20L300%20192%22%2F%3E%3C%2Fg%3E%3Ccircle%20cx%3D%22170%22%20cy%3D%2227%22%20r%3D%2219%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%22170%22%20y%3D%2232%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EA%3C%2Ftext%3E%3Ctext%20x%3D%22194%22%20y%3D%2211%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E1%3C%2Ftext%3E%3Ccircle%20cx%3D%2287%22%20cy%3D%22100%22%20r%3D%2219%22%20fill%3D%22%230891B2%22%2F%3E%3Ctext%20x%3D%2287%22%20y%3D%22105%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EB%3C%2Ftext%3E%3Ctext%20x%3D%22111%22%20y%3D%2284%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E2%3C%2Ftext%3E%3Ccircle%20cx%3D%22253%22%20cy%3D%22100%22%20r%3D%2219%22%20fill%3D%22%230891B2%22%2F%3E%3Ctext%20x%3D%22253%22%20y%3D%22105%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EC%3C%2Ftext%3E%3Ctext%20x%3D%22277%22%20y%3D%2284%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E3%3C%2Ftext%3E%3Ccircle%20cx%3D%2240%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%2240%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3ED%3C%2Ftext%3E%3Ctext%20x%3D%2264%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E4%3C%2Ftext%3E%3Ccircle%20cx%3D%22132%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22132%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EE%3C%2Ftext%3E%3Ctext%20x%3D%22156%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E5%3C%2Ftext%3E%3Ccircle%20cx%3D%22208%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22208%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EF%3C%2Ftext%3E%3Ctext%20x%3D%22232%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E6%3C%2Ftext%3E%3Ccircle%20cx%3D%22300%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22300%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EG%3C%2Ftext%3E%3Ctext%20x%3D%22324%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E7%3C%2Ftext%3E%3Ctext%20x%3D%2210%22%20y%3D%2228%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3ELevel%200%3C%2Ftext%3E%3Ctext%20x%3D%2210%22%20y%3D%22101%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3ELevel%201%3C%2Ftext%3E%3Ctext%20x%3D%2210%22%20y%3D%22229%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3ELevel%202%3C%2Ftext%3E%3C%2Fsvg%3E)

*The small numbers indicate BFS visitation order, assuming left-to-right exploration.*

### BFS algorithm

1. Insert the initial state into a queue.
2. Remove the front node from the queue.
3. Check whether it is the goal.
4. If not, add its unvisited successors to the back of the queue.
5. Repeat until the goal is found or the queue becomes empty.

### Worked example

Using the graph above, suppose A is the starting node and F is the goal.

| Step | Node explored | Queue after exploration |
| :--- | :--- | :--- |
| 1 | A | B, C |
| 2 | B | C, D, E |
| 3 | C | D, E, F, G |
| 4 | D | E, F, G |
| 5 | E | F, G |
| 6 | F | Goal found |

The resulting solution path is:
> **A → C → F**
> Path length = 2 edges

### BFS properties

| Property | Result |
| :--- | :--- |
| **Complete** | Yes, with finite branching |
| **Optimal** | Yes, when every edge has equal cost |
| **Time complexity** | $O(b^d)$ |
| **Space complexity** | $O(b^d)$ |

Here, $b$ is the branching factor and $d$ is the depth of the shallowest goal. These are standard worst-case tree-search bounds.

**Main disadvantage:** BFS can consume a large amount of memory because it stores nodes across entire levels.

## 3. Depth-First Search (DFS)

DFS explores one branch as deeply as possible before backtracking to explore other branches.

### ELI5 explanation

Imagine exploring a maze by following one corridor until you reach a dead end. You then return to the previous intersection and try another corridor.

That's exactly how DFS works.

### DFS exploration

![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20340%20242%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20stroke%3D%22currentColor%22%20opacity%3D%22.4%22%20stroke-width%3D%221.6%22%20fill%3D%22none%22%3E%3Cpath%20d%3D%22M170%2027%20L87%20100%20M170%2027%20L253%20100%20M87%20100%20L40%20192%20M87%20100%20L132%20192%20M253%20100%20L208%20192%20M253%20100%20L300%20192%22%2F%3E%3C%2Fg%3E%3Cpath%20d%3D%22M170%2027%20L87%20100%20L40%20192%20M87%20100%20L132%20192%20M170%2027%20L253%20100%20L208%20192%20M253%20100%20L300%20192%22%20stroke%3D%22%237C3AED%22%20stroke-width%3D%223%22%20fill%3D%22none%22%20stroke-dasharray%3D%225%203%22%2F%3E%3Ccircle%20cx%3D%22170%22%20cy%3D%2227%22%20r%3D%2219%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%22170%22%20y%3D%2232%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EA%3C%2Ftext%3E%3Ctext%20x%3D%22194%22%20y%3D%2211%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E1%3C%2Ftext%3E%3Ccircle%20cx%3D%2287%22%20cy%3D%22100%22%20r%3D%2219%22%20fill%3D%22%237C3AED%22%2F%3E%3Ctext%20x%3D%2287%22%20y%3D%22105%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EB%3C%2Ftext%3E%3Ctext%20x%3D%22111%22%20y%3D%2284%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E2%3C%2Ftext%3E%3Ccircle%20cx%3D%22253%22%20cy%3D%22100%22%20r%3D%2219%22%20fill%3D%22%237C3AED%22%2F%3E%3Ctext%20x%3D%22253%22%20y%3D%22105%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EC%3C%2Ftext%3E%3Ctext%20x%3D%22277%22%20y%3D%2284%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E5%3C%2Ftext%3E%3Ccircle%20cx%3D%2240%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%237C3AED%22%2F%3E%3Ctext%20x%3D%2240%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3ED%3C%2Ftext%3E%3Ctext%20x%3D%2264%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E3%3C%2Ftext%3E%3Ccircle%20cx%3D%22132%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%237C3AED%22%2F%3E%3Ctext%20x%3D%22132%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EE%3C%2Ftext%3E%3Ctext%20x%3D%22156%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E4%3C%2Ftext%3E%3Ccircle%20cx%3D%22208%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%237C3AED%22%2F%3E%3Ctext%20x%3D%22208%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EF%3C%2Ftext%3E%3Ctext%20x%3D%22232%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E6%3C%2Ftext%3E%3Ccircle%20cx%3D%22300%22%20cy%3D%22192%22%20r%3D%2219%22%20fill%3D%22%237C3AED%22%2F%3E%3Ctext%20x%3D%22300%22%20y%3D%22197%22%20font-size%3D%2214%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%3EG%3C%2Ftext%3E%3Ctext%20x%3D%22324%22%20y%3D%22176%22%20font-size%3D%2211%22%20fill%3D%22currentColor%22%3E7%3C%2Ftext%3E%3C%2Fsvg%3E)

*DFS goes deep into the left branch before backtracking to explore the right branch.*

### DFS algorithm

1. Push the initial state onto a stack.
2. Pop the top state.
3. Check whether it is the goal.
4. If not, push its unvisited successors onto the stack.
5. Continue until the goal is found or the stack is empty.

*Recursive DFS uses the program's call stack instead of an explicit stack.*

### Worked example

Suppose A is the initial state and F is the goal.

Following left-to-right exploration:

**DFS visitation order:**
A, B, D, E, C, F

D and E are dead ends. DFS backtracks to A, explores C and finds F.

Although the visitation order includes D and E, the final solution path is:
> **A → C → F**

### DFS properties

| Property | Result |
| :--- | :--- |
| **Complete** | Not guaranteed in infinite-depth spaces |
| **Optimal** | No |
| **Time complexity** | $O(b^m)$ |
| **Space complexity** | $O(bm)$ |

Here, $m$ is the maximum search depth. These bounds apply to standard tree-search DFS.

**Main advantage:** DFS generally uses much less memory than BFS.

**Main disadvantage:** It may spend a long time exploring a deep branch while a shallow solution exists elsewhere.

## 4. Uniform-Cost Search (UCS)

Uniform-Cost Search expands the node with the lowest cumulative path cost from the initial state.

Unlike BFS, UCS considers the cost of each action rather than simply counting the number of steps.

### Key formula

$$g(n) = \sum_{i=1}^{k} c_i$$

Where $g(n)$ is the cumulative cost from the initial state to node $n$, and $c_i$ is the cost of each action along that path.

UCS uses a priority queue ordered by $g(n)$.

### Worked example

Consider the following weighted graph.

![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20340%20220%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20stroke%3D%22currentColor%22%20stroke-width%3D%221.7%22%20opacity%3D%22.65%22%20fill%3D%22none%22%3E%3Cpath%20d%3D%22M35%20105%20L135%2035%20L245%2035%20L305%20105%22%2F%3E%3Cpath%20d%3D%22M35%20105%20L135%20180%20L245%20180%20L305%20105%22%2F%3E%3Cpath%20d%3D%22M135%2035%20L245%20180%22%2F%3E%3C%2Fg%3E%3Ctext%20x%3D%2278%22%20y%3D%2260%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22190%22%20y%3D%2225%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E4%3C%2Ftext%3E%3Ctext%20x%3D%22278%22%20y%3D%2263%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%2278%22%20y%3D%22160%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E5%3C%2Ftext%3E%3Ctext%20x%3D%22190%22%20y%3D%22195%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E1%3C%2Ftext%3E%3Ctext%20x%3D%22278%22%20y%3D%22161%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22177%22%20y%3D%22109%22%20font-size%3D%2213%22%20text-anchor%3D%22middle%22%20fill%3D%22currentColor%22%20font-weight%3D%22semibold%22%3E1%3C%2Ftext%3E%3Ccircle%20cx%3D%2235%22%20cy%3D%22105%22%20r%3D%2219%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%2235%22%20y%3D%22110%22%20font-size%3D%2214%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%3ES%3C%2Ftext%3E%3Ccircle%20cx%3D%22135%22%20cy%3D%2235%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22135%22%20y%3D%2240%22%20font-size%3D%2214%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%3EA%3C%2Ftext%3E%3Ccircle%20cx%3D%22135%22%20cy%3D%22180%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22135%22%20y%3D%22185%22%20font-size%3D%2214%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%3EB%3C%2Ftext%3E%3Ccircle%20cx%3D%22245%22%20cy%3D%2235%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22245%22%20y%3D%2240%22%20font-size%3D%2214%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%3EC%3C%2Ftext%3E%3Ccircle%20cx%3D%22245%22%20cy%3D%22180%22%20r%3D%2219%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22245%22%20y%3D%22185%22%20font-size%3D%2214%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%3ED%3C%2Ftext%3E%3Ccircle%20cx%3D%22305%22%20cy%3D%22105%22%20r%3D%2219%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22305%22%20y%3D%22110%22%20font-size%3D%2214%22%20text-anchor%3D%22middle%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%3EG%3C%2Ftext%3E%3C%2Fsvg%3E)

*Edge labels indicate travel costs. For this example, treat edges as traversable in both directions.*

The goal is to find the lowest-cost route from S to G.

### Step-by-step UCS execution

The frontier below lists nodes with their best known cumulative costs.

| Step | Expanded node | Frontier after expansion |
| :--- | :--- | :--- |
| 1 | S (0) | A(2), B(5) |
| 2 | A (2) | D(3), B(5), C(6) |
| 3 | D (3) | B(4), G(5), C(6) |
| 4 | B (4) | G(5), C(6) |
| 5 | G (5) | Goal reached |

The path through A and D has the lowest cost:
$$S \rightarrow A \rightarrow D \rightarrow G$$
$$2 + 1 + 2 = 5$$

> **Optimal solution**
> **S → A → D → G**
> Minimum total cost = 5

### UCS properties

| Property | Result |
| :--- | :--- |
| **Complete** | Yes, if every step cost is at least some positive $\epsilon$ |
| **Optimal** | Yes, for nonnegative edge costs under standard conditions |
| **Time complexity** | Exponential in the worst case |
| **Space complexity** | Exponential in the worst case |

A common time and space bound, when every step cost is at least $\epsilon > 0$, is:
$$O\left(b^{1 + \lfloor C^*/\epsilon \rfloor}\right)$$
