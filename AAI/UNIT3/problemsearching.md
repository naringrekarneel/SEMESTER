# Agentic AI — Complete Learning Roadmap

We'll cover your syllabus in a logical sequence, starting with how AI agents solve problems and progressing toward how they plan, learn, make decisions and execute complex tasks.

Our focus will be on exam-ready explanations, algorithms, worked examples and practical applications.

# 1. Learning Roadmap

# Module 1: Problem Solving and Search

Starting here

|
No.

|

Topic

|
| --- | --- |
|

1

|

Problem Solving by Search

|
|

2

|

State-Space Representation

|
|

3

|

Uninformed Search: BFS, DFS, UCS

|
|

4

|

Heuristic Search: Greedy Best-First Search

|
|

5

|

A* Search Algorithm

|

# Module 2: Classical Planning

|
No.

|

Topic

|
| --- | --- |
|

6

|

Introduction to Classical Planning

|
|

7

|

Forward and Backward Planning

|
|

8

|

STRIPS and Planning Algorithms

|

# Module 3: Reinforcement Learning

|
No.

|

Topic

|
| --- | --- |
|

9

|

Reinforcement Learning for Agents

|
|

10

|

Markov Decision Process (MDP)

|
|

11

|

Value Functions and Bellman Equations

|
|

12

|

Policy-Based Decision Making

|
|

13

|

Q-Learning and Policy Optimization

|

# Module 4: Agentic AI Task Execution

|
No.

|

Topic

|
| --- | --- |
|

14

|

Multi-Step Task Decomposition

|
|

15

|

Planning and Executing Multi-Step Tasks

|
|

16

|

Connecting Search, Planning and RL in Agentic AI

|

We'll have a quick revision sheet and mini quiz after every few topics.

# Topic 1: Problem Solving by Search

Module 1

Important for exams

## 1. What is problem solving by search?

Definition (exam-ready):

Problem solving by search is a technique in Artificial Intelligence in which an intelligent agent explores possible states and actions to find a sequence of steps that transforms an initial state into a desired goal state.

In simple words, an AI agent considers possible actions, explores their outcomes and finds a path toward its goal.

## 2. ELI5 explanation

Imagine you are inside a maze. You know your starting position and where the exit is, but you don't know the correct route.

You can move left, right, forward or backward. At every intersection, you must decide which direction to explore.

An AI search agent solves a similar problem by representing the maze as states and the possible movements as actions.

A search agent explores possible paths from the starting position to the goal.

The agent's objective may be to find any valid path, the shortest path or the path with the lowest cost.

## 3. Components of a search problem

A search problem generally consists of six important components.

|
Component

|

Explanation

|

Maze example

|
| --- | --- | --- |
|

Initial state

|

Where the agent starts

|

Maze entrance

|
|

State space

|

All possible states

|

All reachable positions

|
|

Actions

|

Available operations

|

Up, down, left, right

|
|

Transition model

|

Result of an action

|

Moving to another cell

|
|

Goal test

|

Checks whether the goal is reached

|

Reaching the exit

|
|

Path cost

|

Cost of the chosen actions

|

Number of steps

|

Must remember

A search problem specifies the initial state, actions, transition model, goal test and path cost. The state space consists of all states reachable through valid actions.

## 4. How does problem solving by search work?

The search process follows these steps:

Define the problem

Identify the initial state

Generate possible actions

Explore successor states

Apply the goal test

Return the solution path

During exploration, the agent maintains a frontier, containing states waiting to be explored. It may also maintain an explored set to avoid repeatedly visiting the same states.

The search algorithm determines which state from the frontier is explored next.

## 5. Types of search algorithms

Search algorithms are broadly divided into two categories.

## Search Algorithms

Uninformed Search

Uses no additional information about how close a state is to the goal.

* Breadth-First Search

* Depth-First Search

* Uniform-Cost Search

Informed Search

Uses heuristic estimates to guide exploration toward the goal.

* Greedy Best-First Search

* A* Search

We'll study these algorithms individually in upcoming topics.

## 6. Step-by-step worked example

Consider an AI agent trying to travel from city A to city F.

Example search graph

![](data\:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20340%20235%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20stroke%3D%22currentColor%22%20stroke-width%3D%221.6%22%20fill%3D%22none%22%20opacity%3D%220.65%22%3E%3Cpath%20d%3D%22M42%20118%20L128%2048%20L218%2048%20L300%20118%22%2F%3E%3Cpath%20d%3D%22M42%20118%20L128%20190%20L218%20190%20L300%20118%22%2F%3E%3Cpath%20d%3D%22M128%2048%20L218%20190%22%2F%3E%3C%2Fg%3E%3Ctext%20x%3D%2285%22%20y%3D%2277%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22173%22%20y%3D%2238%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%22263%22%20y%3D%2276%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E5%3C%2Ftext%3E%3Ctext%20x%3D%2285%22%20y%3D%22164%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E4%3C%2Ftext%3E%3Ctext%20x%3D%22173%22%20y%3D%22202%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22263%22%20y%3D%22166%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22166%22%20y%3D%22115%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E1%3C%2Ftext%3E%3Ccircle%20cx%3D%2242%22%20cy%3D%22118%22%20r%3D%2218%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%2242%22%20y%3D%22123%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EA%3C%2Ftext%3E%3Ccircle%20cx%3D%22128%22%20cy%3D%2248%22%20r%3D%2218%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22128%22%20y%3D%2253%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EB%3C%2Ftext%3E%3Ccircle%20cx%3D%22128%22%20cy%3D%22190%22%20r%3D%2218%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22128%22%20y%3D%22195%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EC%3C%2Ftext%3E%3Ccircle%20cx%3D%22218%22%20cy%3D%2248%22%20r%3D%2218%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22218%22%20y%3D%2253%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3ED%3C%2Ftext%3E%3Ccircle%20cx%3D%22218%22%20cy%3D%22190%22%20r%3D%2218%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22218%22%20y%3D%22195%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EE%3C%2Ftext%3E%3Ccircle%20cx%3D%22300%22%20cy%3D%22118%22%20r%3D%2218%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22300%22%20y%3D%22123%22%20font-size%3D%2214%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EF%3C%2Ftext%3E%3C%2Fsvg%3E)Numbers on the edges represent travel costs. A is the start and F is the goal.

Suppose the agent wants to find the lowest-cost path.

Step 1: Define the problem

Initial state = A, goal state = F. Available actions are movements along the graph's edges.

Step 2: Generate possible paths

Some possible paths are:

* A → B → D → F

* A → C → E → F

* A → B → E → F

Step 3: Calculate path costs

|
Path

|

Calculation

|

Total

|
| --- | --- | --- |
|

A → B → D → F

|

2 + 3 + 5

|

10

|
|

A → C → E → F

|

4 + 2 + 2

|

8

|
|

A → B → E → F

|

2 + 1 + 2 + 2

|

7

|

Step 4: Select the lowest-cost path

Optimal solution

# A → B → E → F

Total path cost = 7

This illustrates the objective of optimal search. In practice, a search algorithm systematically explores states rather than manually listing every possible path.

## 7. Important properties of search algorithms

These four properties are frequently asked in exams and interviews.

|
Property

|

Meaning

|
| --- | --- |
|

Completeness

|

Will it find a solution if one exists?

|
|

Optimality

|

Will it find the lowest-cost solution?

|
|

Time complexity

|

How much computation is required?

|
|

Space complexity

|

How much memory is required?

|

An algorithm can be complete without being optimal. For example, it may find a valid route without finding the cheapest route.

## 8. Real-world applications

Problem solving by search is used in GPS route planning, robotic navigation, game-playing AI, puzzle solving and automated planning.

In Agentic AI, search helps an agent evaluate alternative actions before committing to a plan. For example, an autonomous coding agent might explore different ways to fix a failing test.

## Quick revision sheet

## Topic 1 — Must Remember

* Search finds a sequence of actions from an initial state to a goal state.

* A search problem defines states, actions, transitions, goal conditions and path costs.

* Uninformed search does not use heuristic estimates.

* Informed search uses heuristics to guide exploration.

* Four evaluation criteria: completeness, optimality, time complexity and space complexity.

* A solution is a valid path; an optimal solution has the minimum path cost.

# Active Learning — Test Yourself

Answer these four questions before we move to Topic 2.

Q1 · Conceptual

What is problem solving by search in Artificial Intelligence? Explain using a real-world example.

Q2 · Conceptual

What is the difference between uninformed and informed search? Give two examples of each.

Q3 · Conceptual

Explain the difference between completeness and optimality.

Q4 · Practical

Find the lowest-cost path from S to G.

![](data\:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(255%2C%20255%2C%20255\)%22%20viewBox%3D%220%200%20320%20205%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cg%20stroke%3D%22currentColor%22%20stroke-width%3D%221.7%22%20fill%3D%22none%22%20opacity%3D%220.7%22%3E%3Cpath%20d%3D%22M32%20104%20L118%2038%20L215%2038%20L288%20104%22%2F%3E%3Cpath%20d%3D%22M32%20104%20L118%20169%20L215%20169%20L288%20104%22%2F%3E%3Cpath%20d%3D%22M118%2038%20L215%20169%22%2F%3E%3C%2Fg%3E%3Ctext%20x%3D%2275%22%20y%3D%2262%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%22165%22%20y%3D%2229%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E4%3C%2Ftext%3E%3Ctext%20x%3D%22257%22%20y%3D%2264%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%2275%22%20y%3D%22151%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22166%22%20y%3D%22184%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E3%3C%2Ftext%3E%3Ctext%20x%3D%22257%22%20y%3D%22151%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ctext%20x%3D%22162%22%20y%3D%22105%22%20font-size%3D%2212%22%20fill%3D%22currentColor%22%20text-anchor%3D%22middle%22%3E2%3C%2Ftext%3E%3Ccircle%20cx%3D%2232%22%20cy%3D%22104%22%20r%3D%2217%22%20fill%3D%22%232563EB%22%2F%3E%3Ctext%20x%3D%2232%22%20y%3D%22109%22%20font-size%3D%2213%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3ES%3C%2Ftext%3E%3Ccircle%20cx%3D%22118%22%20cy%3D%2238%22%20r%3D%2217%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22118%22%20y%3D%2243%22%20font-size%3D%2213%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EA%3C%2Ftext%3E%3Ccircle%20cx%3D%22118%22%20cy%3D%22169%22%20r%3D%2217%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22118%22%20y%3D%22174%22%20font-size%3D%2213%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EB%3C%2Ftext%3E%3Ccircle%20cx%3D%22215%22%20cy%3D%2238%22%20r%3D%2217%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22215%22%20y%3D%2243%22%20font-size%3D%2213%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EC%3C%2Ftext%3E%3Ccircle%20cx%3D%22215%22%20cy%3D%22169%22%20r%3D%2217%22%20fill%3D%22%2364748B%22%2F%3E%3Ctext%20x%3D%22215%22%20y%3D%22174%22%20font-size%3D%2213%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3ED%3C%2Ftext%3E%3Ccircle%20cx%3D%22288%22%20cy%3D%22104%22%20r%3D%2217%22%20fill%3D%22%2316A34A%22%2F%3E%3Ctext%20x%3D%22288%22%20y%3D%22109%22%20font-size%3D%2213%22%20font-weight%3D%22bold%22%20fill%3D%22%23FFFFFF%22%20text-anchor%3D%22middle%22%3EG%3C%2Ftext%3E%3C%2Fsvg%3E)

Calculate the total cost and explain your chosen path.

Reply with your answers to Q1–Q4. I'll check them, explain any mistakes and then we'll move on to Topic 2: State-Space Representation.
