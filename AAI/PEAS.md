# Topic 5: PEAS Description and Task Environments

This topic is **very exam-friendly** because PEAS gives you a systematic way to describe an intelligent agent.

Think of PEAS as the agent's **job description**.

> **P = Performance Measure**
> **E = Environment**
> **A = Actuators**
> **S = Sensors**

---

# 1. What is PEAS?

## ELI5

Suppose we want to build a **self-driving car**.

Before building it, we need to answer four questions:

1. **How do we know the car is doing a good job?** → Performance Measure
2. **Where is the car operating?** → Environment
3. **What can the car do?** → Actuators
4. **What can the car sense?** → Sensors

That's PEAS.

---

# 2. Formal Definition

**PEAS** is a framework used to specify the **task environment of an intelligent agent** by defining its:

* **Performance Measure**
* **Environment**
* **Actuators**
* **Sensors**

It helps designers clearly define what an agent should achieve, where it operates, how it acts, and how it perceives the environment.

---

# 3. P — Performance Measure

This answers:

> **"How do we measure whether the agent is successful?"**

Examples:

For a self-driving car:

* Safety
* Minimum travel time
* Passenger comfort
* Low fuel consumption
* Following traffic rules

---

## Important

Performance measure is **not the same as the goal**.

For example:

**Goal:** Reach college.

**Performance measures:**

* Reach safely
* Reach quickly
* Spend less money
* Avoid accidents

The goal says **what should be achieved**.

The performance measure says **how well it was achieved**.

---

# 4. E — Environment

This is the world in which the agent operates.

For a self-driving car:

* Roads
* Traffic
* Pedestrians
* Weather
* Traffic lights
* Other vehicles

---

# 5. A — Actuators

Actuators are the mechanisms through which the agent **takes action**.

For a self-driving car:

* Steering
* Accelerator
* Brake
* Horn
* Indicators

Simple memory trick:

> **Actuator = Action**

---

# 6. S — Sensors

Sensors allow the agent to **perceive the environment**.

For a self-driving car:

* Cameras
* Radar
* LiDAR
* GPS
* Ultrasonic sensors

Simple memory trick:

> **Sensor = Sense**

---

# Complete PEAS Example: Self-Driving Car

| PEAS                    | Example                                 |
| ----------------------- | --------------------------------------- |
| **Performance Measure** | Safety, speed, comfort, fuel efficiency |
| **Environment**         | Roads, traffic, pedestrians, weather    |
| **Actuators**           | Steering, brakes, accelerator, horn     |
| **Sensors**             | Camera, GPS, radar, LiDAR               |

This is one of the most common examples in exams.

---

# Example 2: Vacuum Cleaner Agent

Let's build another one.

### Performance Measure

* Maximum cleanliness
* Minimum time
* Minimum energy consumption

### Environment

* Rooms
* Floors
* Furniture
* Dirt
* Walls

### Actuators

* Wheels
* Suction motor
* Brushes

### Sensors

* Dirt sensor
* Camera
* Distance sensor
* Bumper sensor

---

# Example 3: Medical Diagnosis Agent

### Performance Measure

* Diagnostic accuracy
* Patient safety
* Fast diagnosis
* Appropriate treatment recommendation

### Environment

* Hospital
* Patient
* Medical records
* Laboratory results

### Actuators

* Display diagnosis
* Generate report
* Recommend tests
* Alert doctor

### Sensors

* Patient symptoms
* Medical history
* Test results
* Vital signs

---

# Example 4: Chess Agent

### Performance Measure

* Win the game
* Maximize score
* Minimize mistakes

### Environment

* Chessboard
* Opponent
* Current game state

### Actuators

* Make chess move

### Sensors

* Board state
* Opponent's moves

---

# 7. What is a Task Environment?

A **task environment** is the complete problem setting in which an intelligent agent operates.

It includes:

* What the agent must achieve
* The world it operates in
* What it can perceive
* What actions it can perform

PEAS helps us define this environment clearly.

---

# 8. Properties of Task Environments

This is another **high-priority exam area**.

Task environments can be classified using several properties.

---

## A. Fully Observable vs Partially Observable

### Fully Observable

The agent can access all information needed about the current environment.

Example:

**Chess**

The complete board is visible.

```text
Agent sees → Entire board
```

---

### Partially Observable

The agent cannot see everything.

Example:

**Self-driving car**

It cannot know everything happening behind every building or vehicle.

```text
Agent sees → Only part of environment
```

### Memory trick

> **Fully observable = Complete information**

> **Partially observable = Missing information**

---

# B. Deterministic vs Stochastic

### Deterministic

An action always produces a predictable result.

Example:

Chess:

> Move a piece → Piece moves to the selected square.

---

### Stochastic

There is uncertainty in the outcome.

Example:

Self-driving car:

> Apply brakes → Exact stopping distance can vary.

Weather, road conditions, human behavior, etc. introduce uncertainty.

### Memory trick

> **Deterministic = predictable**

> **Stochastic = uncertainty**

---

# C. Episodic vs Sequential

### Episodic

Each decision is mostly independent of previous decisions.

Example:

Image classification.

```text
Image 1 → classify
Image 2 → classify
Image 3 → classify
```

Previous classifications don't significantly affect the next one.

---

### Sequential

Current actions affect future states.

Example:

Chess.

One move changes the future possibilities.

### Memory trick

> **Episodic = independent decisions**

> **Sequential = decisions are connected**

---

# D. Static vs Dynamic

### Static

Environment doesn't change while the agent is deciding.

Example:

Crossword puzzle.

---

### Dynamic

Environment changes while the agent is operating.

Example:

Self-driving car.

Traffic keeps moving.

### Memory trick

> **Static = stays**

> **Dynamic = changes**

---

# E. Discrete vs Continuous

### Discrete

Limited/countable states or actions.

Example:

Chess.

There are distinct moves and board positions.

---

### Continuous

Values can vary continuously.

Example:

Self-driving car.

* Speed
* Steering angle
* Position

can change continuously.

---

# F. Single-Agent vs Multi-Agent

### Single-Agent

Only one agent is making decisions.

Example:

Sudoku-solving system.

---

### Multi-Agent

Multiple agents interact.

Example:

Chess:

* Agent 1 = You
* Agent 2 = Opponent

Other examples:

* Autonomous vehicles
* Multi-agent games
* Trading systems

---

# Task Environment Classification Table

| Property            | Type 1           | Type 2               |
| ------------------- | ---------------- | -------------------- |
| Observability       | Fully Observable | Partially Observable |
| Outcome             | Deterministic    | Stochastic           |
| Decision dependency | Episodic         | Sequential           |
| Change over time    | Static           | Dynamic              |
| State/action space  | Discrete         | Continuous           |
| Number of agents    | Single-Agent     | Multi-Agent          |

This table is worth memorizing.

---

# Worked Example: Self-Driving Car

Let's classify its environment.

### Observability

**Partially observable**

Why?

The car cannot observe everything around it.

---

### Deterministic/Stochastic

**Stochastic**

Why?

Other drivers and environmental conditions are unpredictable.

---

### Episodic/Sequential

**Sequential**

Why?

Every steering/braking decision affects future states.

---

### Static/Dynamic

**Dynamic**

Why?

Traffic and pedestrians are continuously moving.

---

### Discrete/Continuous

Mostly **continuous**

Why?

Speed, steering, acceleration, and position vary continuously.

---

### Single/Multi-Agent

**Multi-Agent**

Why?

Other drivers and autonomous systems also make decisions.

---

# Full Example

A typical self-driving car environment can therefore be described as:

> **Partially observable, stochastic, sequential, dynamic, continuous, and multi-agent.**

That exact sentence can earn easy marks in an exam when supported with explanations.

---

# PEAS vs Task Environment

Don't mix them up.

| PEAS                       | Task Environment                       |
| -------------------------- | -------------------------------------- |
| Describes the agent's task | Describes characteristics of the world |
| Performance                | Observability                          |
| Environment                | Determinism                            |
| Actuators                  | Episodic/Sequential                    |
| Sensors                    | Static/Dynamic                         |
|                            | Discrete/Continuous                    |
|                            | Single/Multi-agent                     |

So:

> **PEAS tells us what the agent needs to do and interact with.**

> **Task-environment properties tell us what kind of world the agent operates in.**

---

# Exam-Friendly Example

### Question:

**Give the PEAS description for a self-driving car.**

### Answer:

**P — Performance Measure:** Safety, minimum travel time, passenger comfort, fuel efficiency, traffic-rule compliance.

**E — Environment:** Roads, vehicles, pedestrians, traffic lights, weather, road conditions.

**A — Actuators:** Steering, accelerator, brakes, horn, indicators.

**S — Sensors:** Cameras, GPS, radar, LiDAR, ultrasonic sensors.

Then mention its task environment:

> Partially observable, stochastic, sequential, dynamic, continuous, and multi-agent.

That's a very solid answer.

---

# Must-Remember

### PEAS

**P → Performance Measure → How well?**

**E → Environment → Where?**

**A → Actuators → What can it do?**

**S → Sensors → What can it perceive?**

### Task Environment

Remember:

> **Observable → Deterministic → Episodic → Static → Discrete → Agents**

The pairs are:

* Full ↔ Partial
* Deterministic ↔ Stochastic
* Episodic ↔ Sequential
* Static ↔ Dynamic
* Discrete ↔ Continuous
* Single ↔ Multi-agent

---

# Quick Revision Sheet

```text
PEAS
P → Performance
E → Environment
A → Actuators
S → Sensors

Task Environment
→ Observable?
→ Predictable?
→ Independent or sequential?
→ Static or dynamic?
→ Discrete or continuous?
→ Single or multi-agent?
```

---

# Active Learning

### Conceptual Questions

**1.** What is PEAS, and why is it used when designing an intelligent agent?

**2.** Differentiate between **fully observable** and **partially observable** environments.

**3.** Differentiate between **deterministic** and **stochastic** environments with one example each.

### Practical Question

Create the **PEAS description** for an **AI chess-playing agent**, including:

* Performance Measure
* Environment
* Actuators
* Sensors

Then classify the chess task environment as:

**observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, and single-agent/multi-agent.**

Reply with your answer, or type **next** for **Topic 6: Architecture of Intelligent Agents**.
