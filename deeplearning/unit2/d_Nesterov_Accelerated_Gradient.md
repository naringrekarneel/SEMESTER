# Topic 4: Nesterov Accelerated Gradient (NAG)

> **Exam Importance:** ⭐⭐⭐⭐☆ (Frequently Asked)

Nesterov Accelerated Gradient (NAG) is an **improved version of Momentum**. Instead of blindly following the previous momentum, it **looks ahead** before deciding the next step.

---

# ELI5 Explanation

Imagine you're driving a car.

### Momentum 🚗

You keep driving based on your current speed.

If there's a sharp turn ahead, you'll notice it only after reaching it.

---

### NAG 🚘

Before accelerating, you **look ahead** at the road.

If you see a turn, you adjust your steering early.

Result:

* Smoother driving
* Less overshooting
* Faster arrival

That's exactly how NAG works.

---

# Real-World Intuition

Imagine running toward a staircase.

### Momentum

You run at full speed and realize you're at the stairs only when you reach them.

---

### NAG

You notice the stairs **a few steps before** reaching them and slow down in advance.

This avoids overshooting and makes movement more efficient.

---

# Why Was NAG Introduced?

Momentum has one limitation.

It says:

> "I was moving in this direction, so I'll keep going."

But what if the minimum is very close?

Momentum may overshoot it.

NAG fixes this by checking **where momentum is about to take us** before calculating the gradient.

---

# Core Idea

### Momentum

```text
Current Position
      ↓
Compute Gradient
      ↓
Move
```

---

### NAG

```text
Current Position
      ↓
Move a little using momentum (look ahead)
      ↓
Compute Gradient at the new position
      ↓
Correct the movement
```

The key difference is **where the gradient is calculated**.

* Momentum → Current position
* NAG → Look-ahead position

---

# Formula

### Step 1: Look Ahead

[
W_{look} = W + \beta v
]

---

### Step 2: Compute Gradient at Look-Ahead Point

[
g = \nabla J(W_{look})
]

---

### Step 3: Update Velocity

[
v = \beta v - \eta g
]

---

### Step 4: Update Weight

[
W = W + v
]

---

## Must Remember

**Momentum** uses the gradient at the **current position**.

**NAG** uses the gradient at the **future (look-ahead) position**.

---

# Step-by-Step Example

Suppose:

* Weight = 10
* Previous velocity = -0.5
* Learning rate = 0.1
* Momentum = 0.9
* Gradient at look-ahead point = 2

### Step 1

Look-ahead position:

[
W_{look} = 10 + 0.9(-0.5)
= 10 - 0.45
= 9.55
]

---

### Step 2

Gradient at 9.55:

[
g = 2
]

---

### Step 3

Velocity:

[
v = 0.9(-0.5) - 0.1(2)
= -0.45 - 0.2
= -0.65
]

---

### Step 4

Update weight:

[
W = 10 - 0.65 = 9.35
]

---

# Visual Comparison

### Momentum

```text
Start

●
 \
  \
   \
    \
     Goal
```

It keeps moving based on previous direction.

---

### NAG

```text
Start

●
 \
  \
   👀 Look Ahead
     \
      Goal
```

Checks the future position before updating.

---

# Advantages

* Faster convergence than Momentum.
* Reduces overshooting.
* More accurate updates.
* Performs well on deep neural networks.
* Uses future information for smarter movement.

---

# Disadvantages

* Slightly more computation than Momentum.
* Still requires tuning learning rate and momentum coefficient.

---

# Momentum vs NAG

| Feature                               | Momentum | NAG               |
| ------------------------------------- | -------- | ----------------- |
| Uses previous velocity                | ✅        | ✅                 |
| Looks ahead before computing gradient | ❌        | ✅                 |
| Overshooting                          | More     | Less              |
| Accuracy                              | Good     | Better            |
| Convergence                           | Fast     | Faster & smoother |

---

# Exam/Interview Must-Remember Points

* NAG is an enhancement of Momentum.
* Computes the gradient at the **look-ahead position**.
* Reduces overshooting near the minimum.
* Usually converges faster and more accurately than Momentum.
* The main idea is **"look before you leap."**

---

# Quick Revision

* NAG = Momentum + Look Ahead.
* Gradient is computed at the future position.
* Less oscillation and overshooting.
* Better convergence than Momentum.
* Frequently asked difference: **Momentum vs NAG**.

---

# Connection So Far

```text
Gradient Descent
        ↓
SGD / Mini-Batch GD
        ↓
Momentum
        ↓
Nesterov Accelerated Gradient (NAG)
        ↓
Next: Adaptive Learning Rates (AdaGrad)
```

Notice the progression:

* **GD** learns using gradients.
* **Momentum** adds memory.
* **NAG** adds memory + foresight.

---

# Active Learning

### Conceptual Questions

1. What is the main difference between Momentum and NAG?
2. Why does NAG reduce overshooting?
3. At which position does NAG calculate the gradient?

### Practical Question

Given:

* Weight = **15**
* Previous velocity = **−0.4**
* Momentum coefficient = **0.9**
* Learning rate = **0.1**
* Gradient at the look-ahead position = **3**

Calculate:

1. The look-ahead position.
2. The new velocity.
3. The updated weight.

Reply with your answers, and we'll move to **Topic 5: AdaGrad**.
