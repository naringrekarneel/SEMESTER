# Topic 1: Problem Solving by Search
**Module 1 Important for exams**

## 1. What is problem solving by search?

**Definition (exam-ready):**
Problem solving by search is a technique in Artificial Intelligence in which an intelligent agent explores possible states and actions to find a sequence of steps that transforms an initial state into a desired goal state.

In simple words, an AI agent considers possible actions, explores their outcomes, and finds a path toward its goal.

## 2. ELI5 explanation

Imagine you are inside a maze. You know your starting position and where the exit is, but you don't know the correct route.

You can move left, right, forward or backward. At every intersection, you must decide which direction to explore.

An AI search agent solves a similar problem by representing the maze as states and the possible movements as actions.

A search agent explores possible paths from the starting position to the goal.

The agent's objective may be to find any valid path, the shortest path, or the path with the lowest cost.

## 3. Components of a search problem

A search problem generally consists of six important components.

| Component | Explanation | Maze example |
| :--- | :--- | :--- |
| **Initial state** | Where the agent starts | Maze entrance |
| **State space** | All possible states | All reachable positions |
| **Actions** | Available operations | Up, down, left, right |
| **Transition model** | Result of an action | Moving to another cell |
| **Goal test** | Checks whether the goal is reached | Reaching the exit |
| **Path cost** | Cost of the chosen actions | Number of steps |

> **Must remember:**
> A search problem specifies the initial state, actions, transition model, goal test, and path cost. The state space consists of all states reachable through valid actions.

## 4. How does problem solving by search work?

The search process follows these steps:
1. Define the problem
2. Identify the initial state
3. Generate possible actions
4. Explore successor states
5. Apply the goal test
6. Return the solution path

During exploration, the agent maintains a **frontier**, containing states waiting to be explored. It may also maintain an **explored set** to avoid repeatedly visiting the same states. 
The search algorithm determines which state from the frontier is explored next.

## 5. Types of search algorithms

Search algorithms are broadly divided into two categories.

### Uninformed Search
Uses no additional information about how close a state is to the goal.
* Breadth-First Search
* Depth-First Search
* Uniform-Cost Search

### Informed Search
Uses heuristic estimates to guide exploration toward the goal.
* Greedy Best-First Search
* A* Search

*We'll study these algorithms individually in upcoming topics.*

## 6. Step-by-step worked example

Consider an AI agent trying to travel from city A to city F.
*(Example search graph: Numbers on the edges represent travel costs. A is the start and F is the goal.)*

Suppose the agent wants to find the lowest-cost path.

**Step 1: Define the problem**
* Initial state = A
* Goal state = F
* Available actions = Movements along the graph's edges.

**Step 2: Generate possible paths**
Some possible paths are:
* A → B → D → F
* A → C → E → F
* A → B → E → F

**Step 3: Calculate path costs**

| Path | Calculation | Total |
| :--- | :--- | :--- |
| A → B → D → F | 2 + 3 + 5 | 10 |
| A → C → E → F | 4 + 2 + 2 | 8 |
| A → B → E → F | 2 + 1 + 2 + 2 | 7 |

**Step 4: Select the lowest-cost path**

> **Optimal solution:**
> A → B → E → F
> Total path cost = 7

This illustrates the objective of optimal search. In practice, a search algorithm systematically explores states rather than manually listing every possible path.

## 7. Important properties of search algorithms

These four properties are frequently asked in exams and interviews.

| Property | Meaning |
| :--- | :--- |
| **Completeness** | Will it find a solution if one exists? |
| **Optimality** | Will it find the lowest-cost solution? |
| **Time complexity** | How much computation is required? |
| **Space complexity** | How much memory is required? |

An algorithm can be complete without being optimal. For example, it may find a valid route without finding the cheapest route.

## 8. Real-world applications

Problem solving by search is used in GPS route planning, robotic navigation, game-playing AI, puzzle solving, and automated planning.

In Agentic AI, search helps an agent evaluate alternative actions before committing to a plan. For example, an autonomous coding agent might explore different ways to fix a failing test.

---

## 📝 Quick Revision Sheet
**Topic 1 — Must Remember**

* Search finds a sequence of actions from an initial state to a goal state.
* A search problem defines states, actions, transitions, goal conditions, and path costs.
* Uninformed search does not use heuristic estimates.
* Informed search uses heuristics to guide exploration.
* Four evaluation criteria: completeness, optimality, time complexity, and space complexity.
* A solution is a valid path; an optimal solution has the minimum path cost.

---

## 🧠 Active Learning — Test Yourself
*Answer these four questions before we move to Topic 2.*

**Q1 · Conceptual**
What is problem solving by search in Artificial Intelligence? Explain using a real-world example.

**Q2 · Conceptual**
What is the difference between uninformed and informed search? Give two examples of each.

**Q3 · Conceptual**
Explain the difference between completeness and optimality.

**Q4 · Practical**
Find the lowest-cost path from S to G.
*(Calculate the total cost and explain your chosen path.)*
