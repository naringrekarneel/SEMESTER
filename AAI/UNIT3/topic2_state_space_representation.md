# Topic 2: State-Space Representation
**Module 1 | Important for exams: 7–10 marks**

## 1. What is State-Space Representation?

**Definition (exam-ready):**
State-space representation is a technique in Artificial Intelligence used to represent a problem as a collection of possible states, actions and transitions. It allows an intelligent agent to search systematically from an initial state to a desired goal state.

### ELI5 explanation

Imagine you're playing chess. Every arrangement of pieces on the chessboard represents a different state.

When you move a piece, the board changes from one state to another. Your goal might be to reach a state where your opponent is checkmated.

The collection of all possible legal board configurations and the moves connecting them forms a state space.

Each chessboard configuration represents a state. Legal moves cause transitions between states.

In Agentic AI, state-space representation helps an agent understand its current situation, identify possible actions and plan how to reach its goal.

## 2. Components of State-Space Representation

A state-space problem consists of five major components.

| Component | Description | Example |
| :--- | :--- | :--- |
| **Initial state** | Starting configuration | Robot at position A |
| **State space** | All reachable configurations | All reachable positions |
| **Actions** | Operations available to the agent | Move left, right, up or down |
| **Transition model** | Defines the resulting state after an action | Moving from A to B |
| **Goal state** | Desired final configuration | Robot reaches destination G |

A path cost function can additionally measure the expense of moving between states.

### Mathematical representation

A search problem can be represented as:
$$P = (S, A, T, s_0, G, C)$$

Where:
* $S$: Set of possible states
* $A$: Set of available actions
* $T$: State-transition function
* $s_0$: Initial state
* $G$: Set of goal states
* $C$: Action-cost function

The transition function is:
$$s' = T(s_t, a_t)$$

This means that performing action $a_t$ in state $s_t$ produces the next state $s'$.

## 3. State-Space Graph

A state-space graph is a graphical representation of a problem in which nodes represent states and edges represent transitions between states.

Consider a robot moving between six locations.

![](data:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20340%20245%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3Cmarker%20id%3D%22arrow%22%20viewBox%3D%220%200%2010%2010%22%20refX%3D%229%22%20refY%3D%225%22%20markerWidth%3D%226%22%20markerHeight%3D%226%22%20orient%3D%22auto-start-reverse%22%3E%3Cpath%20d%3D%22M0%200%20L10%205%20L0%2010%20Z%22%20fill%3D%22%2364748b%22%2F%3E%3C%2Fmarker%3E%3C%2Fdefs%3E%3Cg%20fill%3D%22none%22%20stroke%3D%22%2364748b%22%20stroke-width%3D%221.7%22%20marker-end%3D%22url\(%23arrow\)%22%3E%3Cpath%20d%3D%22M50%20120%20L125%2052%22%2F%3E%3Cpath%20d%3D%22M50%20120%20L125%20190%22%2F%3E%3Cpath%20d%3D%22M145%2043%20L220%2043%22%2F%3E%3Cpath%20d%3D%22M145%20190%20L220%20190%22%2F%3E%3Cpath%20d%3D%22M240%2050%20L290%20110%22%2F%3E%3Cpath%20d%3D%22M240%20183%20L290%20130%22%2F%3E%3Cpath%20d%3D%22M140%2060%20L225%20175%22%2F%3E%3C%2Fg%3E%3Ccircle%20cx%3D%2242%22%20cy%3D%22120%22%20r%3D%2219%22%20fill%3D%22%232563eb%22%2F%3E%3Ctext%20x%3D%2242%22%20y%3D%22125%22%20fill%3D%22white%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20text-anchor%3D%22middle%22%3ES%3C%2Ftext%3E%3Ccircle%20cx%3D%22135%22%20cy%3D%2243%22%20r%3D%2219%22%20fill%3D%22%2364748b%22%2F%3E%3Ctext%20x%3D%22135%22%20y%3D%2248%22%20fill%3D%22white%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20text-anchor%3D%22middle%22%3EA%3C%2Ftext%3E%3Ccircle%20cx%3D%22135%22%20cy%3D%22190%22%20r%3D%2219%22%20fill%3D%22%2364748b%22%2F%3E%3Ctext%20x%3D%22135%22%20y%3D%22195%22%20fill%3D%22white%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20text-anchor%3D%22middle%22%3EB%3C%2Ftext%3E%3Ccircle%20cx%3D%22230%22%20cy%3D%2243%22%20r%3D%2219%22%20fill%3D%22%2364748b%22%2F%3E%3Ctext%20x%3D%22230%22%20y%3D%2248%22%20fill%3D%22white%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20text-anchor%3D%22middle%22%3EC%3C%2Ftext%3E%3Ccircle%20cx%3D%22230%22%20cy%3D%22190%22%20r%3D%2219%22%20fill%3D%22%2364748b%22%2F%3E%3Ctext%20x%3D%22230%22%20y%3D%22195%22%20fill%3D%22white%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20text-anchor%3D%22middle%22%3ED%3C%2Ftext%3E%3Ccircle%20cx%3D%22300%22%20cy%3D%22120%22%20r%3D%2219%22%20fill%3D%22%2316a34a%22%2F%3E%3Ctext%20x%3D%22300%22%20y%3D%22125%22%20fill%3D%22white%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20text-anchor%3D%22middle%22%3EG%3C%2Ftext%3E%3Ctext%20x%3D%2242%22%20y%3D%22155%22%20font-size%3D%2211%22%20fill%3D%22%232563eb%22%20text-anchor%3D%22middle%22%3EInitial%3C%2Ftext%3E%3Ctext%20x%3D%22300%22%20y%3D%22155%22%20font-size%3D%2211%22%20fill%3D%22%2316a34a%22%20text-anchor%3D%22middle%22%3EGoal%3C%2Ftext%3E%3C%2Fsvg%3E)

*Directed edges show the allowed movements between states.*

For example, the agent could follow the path `S → A → C → G` or `S → B → D → G`.

The search algorithm determines which path to explore and eventually returns a solution.

## 4. State Space vs Search Tree

This is a commonly asked distinction.

| State-space graph | Search tree |
| :--- | :--- |
| Represents states and their transitions | Represents the exploration of possible action sequences |
| A state typically appears as one node | The same state may appear multiple times |
| Can contain cycles | Each node has a unique parent, except the root |
| Describes the problem | Describes the search process |

For example, if a robot moves from A to B and then returns to A, the state-space graph contains only one node for A. A search tree may contain two separate nodes representing the two visits to A.

> **Must remember:** A search tree can be much larger than the state-space graph because it may represent repeated visits to the same state.

## 5. Worked Example: The 8-Puzzle Problem

The 8-puzzle is a classic AI problem consisting of eight numbered tiles and one empty space on a 3×3 board.

The objective is to reach a specified goal arrangement by sliding tiles into the empty space.

**Initial state**
```text
1 2 3
4 0 6
7 5 8
```

**Goal state**
```text
1 2 3
4 5 6
7 8 0
```

### Step 1: Identify the states
Each unique arrangement of the tiles represents a state. We represent the empty position using `0`.

### Step 2: Identify possible actions
The empty space can move up, down, left or right, provided the move stays within the board.

### Step 3: Generate successor states
From the initial state, the empty space is in the centre, so all four actions are possible.

**Four possible successor states**

Move up:
```text
1 0 3
4 2 6
7 5 8
```

Move down:
```text
1 2 3
4 5 6
7 0 8
```

Move left:
```text
1 2 3
0 4 6
7 5 8
```

Move right:
```text
1 2 3
4 6 0
7 5 8
```

### Step 4: Find a solution
In this example, only two moves are required.

**Solution path**

Initial state:
```text
1 2 3
4 0 6
7 5 8
```

Move down:
```text
1 2 3
4 5 6
7 0 8
```

Move right — Goal reached:
```text
1 2 3
4 5 6
7 8 0
```

Total path cost = 2, assuming every move costs 1.

## 6. State-Space Complexity

The size of a state space determines how difficult a problem can be.

For an 8-puzzle, there are nine positions, including the empty space.
The total number of possible arrangements is:
$$9! = 362,880$$

However, only half of these arrangements are reachable from any particular starting arrangement:
$$\frac{9!}{2} = 181,440$$

This illustrates why efficient search algorithms are important. Larger problems can have enormous state spaces, making exhaustive exploration impractical.

This rapid increase in the number of possible states is known as **state-space explosion**.

## 7. Real-world applications

* **Robotics**: Each robot position and orientation represents a state.
* **Game AI**: Each board configuration represents a state.
* **Route planning**: Locations represent states, and roads represent transitions.
* **Agentic AI**: A task's current progress, available tools and intermediate results can form part of an agent's state.

---

## 📝 Quick Revision

**Topic 2 — Must Remember**

* State-space representation models a problem using states, actions and transitions.
* The initial state is the starting configuration; the goal state is the desired configuration.
* A state-space graph represents possible states and their relationships.
* A search tree represents the exploration of action sequences.
* State-space explosion occurs when the number of possible configurations becomes extremely large.
* The 8-puzzle has 181,440 states reachable from a given starting arrangement.

---

## 🧠 Active Learning — Test Yourself

**Q1.** Define state-space representation and explain its main components.
**Q2.** What is the difference between a state-space graph and a search tree?
**Q3.** What is state-space explosion, and why is it a challenge in AI?
**Q4. Practical:** Consider the following 8-puzzle configuration:

```text
1 2 3
4 5 6
0 7 8
```

The goal is:

```text
1 2 3
4 5 6
7 8 0
```

Find the sequence of moves required to reach the goal and calculate the path cost, assuming each move costs 1.

> *Reply with your answers, or say Next to continue to Topic 3: Uninformed Search (BFS, DFS and UCS).*
