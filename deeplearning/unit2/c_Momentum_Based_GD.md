# Topic 3: Momentum-Based Gradient Descent

> **Exam Importance:** ⭐⭐⭐⭐☆ (Frequently Asked)

Momentum is the **first major improvement** over Gradient Descent. It helps the optimizer move **faster**, **more smoothly**, and reduces the zig-zag movement seen in SGD.

---

# ELI5 Explanation

Imagine you're pushing a heavy shopping cart.

### Without Momentum

You push...

It moves a little.

You stop.

Push again.

Stop.

It keeps slowing down.

---

### With Momentum

You keep pushing continuously.

The cart gains **speed** and becomes easier to move.

Even if the road has small bumps, it keeps moving forward.

That's exactly what **Momentum** does in Gradient Descent.

It remembers the **previous direction** and keeps moving in that direction.

---

# Real-World Intuition

Imagine riding a bicycle downhill.

Without momentum:

* You pedal every second.
* The bike slows down quickly.

With momentum:

* Once the bike gains speed,
* it keeps moving even if you stop pedaling for a while.

Momentum in optimization works the same way—it carries forward part of the previous update.

---

# Why Do We Need Momentum?

Recall SGD:

```text
Step 1 → Right
Step 2 → Left
Step 3 → Right
Step 4 → Left
```

The optimizer keeps **zig-zagging**, which slows convergence.

Visual idea:

```text
Without Momentum

Goal

      ●
     /
    /
   /
  /
 ●
  \
   \
    \
     ●
```

With Momentum:

```text
Goal

      ●
      |
      |
      |
      |
      ●
```

Momentum smooths the path toward the minimum.

---

# Core Idea

Instead of using **only the current gradient**, Momentum also considers the **previous update**.

It asks:

> "What direction was I already moving? I'll continue in that direction."

This speeds up learning, especially in long valleys of the loss surface.

---

# Key Formulas

### Step 1: Update the velocity

[
v_t = \beta v_{t-1} - \eta \nabla J(W)
]

Where:

* (v_t) = current velocity (momentum)
* (v_{t-1}) = previous velocity
* (\beta) = momentum coefficient (usually **0.9**)
* (\eta) = learning rate
* (\nabla J(W)) = gradient

---

### Step 2: Update the weights

[
W = W + v_t
]

---

## Must Remember

Momentum adds **memory** to Gradient Descent.

Normal GD remembers **nothing**.

Momentum remembers the **previous direction**.

---

# Step-by-Step Worked Example

Suppose:

* Weight = 10
* Gradient = 4
* Learning rate = 0.1
* Momentum = 0.9
* Previous velocity = 0

### Step 1

Calculate velocity:

[
v = 0.9 \times 0 - 0.1 \times 4 = -0.4
]

### Step 2

Update weight:

[
W = 10 + (-0.4) = 9.6
]

---

### Next Iteration

Suppose:

* Gradient = 3
* Previous velocity = -0.4

Velocity:

[
v = 0.9(-0.4) - 0.1(3)
= -0.36 - 0.3
= -0.66
]

Weight:

[
W = 9.6 - 0.66 = 8.94
]

Notice that the optimizer takes a **larger step** because of accumulated momentum.

---

# Visual Comparison

### Gradient Descent

```text
●
 \
  \
   \
    ●
     \
      ●
```

Small, slow steps.

---

### Momentum

```text
●
 \
  \
   \
    \
     \
      ●
```

Longer, smoother movement.

---

# Advantages

* Faster convergence.
* Reduces zig-zag motion.
* Works well in narrow valleys.
* Helps escape small local minima.
* Easy to implement.

---

# Disadvantages

* Requires choosing the momentum coefficient ((\beta)).
* Too much momentum may overshoot the minimum.

---

# Gradient Descent vs Momentum

| Feature                | Gradient Descent | Momentum                |
| ---------------------- | ---------------- | ----------------------- |
| Uses previous updates? | ❌ No             | ✅ Yes                   |
| Speed                  | Slower           | Faster                  |
| Zig-zag movement       | More             | Less                    |
| Convergence            | Slow             | Faster                  |
| Memory                 | None             | Keeps previous velocity |

---

# Exam/Interview Must-Remember Points

* Momentum is an improvement over Gradient Descent.
* It stores the **previous update** as velocity.
* Typical momentum coefficient: **0.9**.
* It reduces oscillations and speeds up convergence.
* Almost every modern optimizer is based on this idea.

---

# Quick Revision

* Momentum = Gradient Descent + Memory.
* Uses **velocity** to remember previous movement.
* Reduces zig-zag behavior.
* Faster than plain Gradient Descent.
* Common momentum value: **0.9**.

---

# Connection with Previous Topics

```
Gradient Descent
        ↓
SGD (faster updates)
        ↓
Momentum (faster + smoother updates)
        ↓
Next: Nesterov Accelerated Gradient (looks ahead before updating)
```

---

# Active Learning

### Conceptual Questions

1. What problem in SGD does Momentum solve?
2. Why is Momentum generally faster than standard Gradient Descent?
3. What does the **velocity** term represent?

### Practical Question

Given:

* Weight = **20**
* Gradient = **5**
* Learning rate = **0.1**
* Momentum coefficient = **0.9**
* Previous velocity = **−0.3**

Calculate:

1. The new velocity.
2. The updated weight.

Reply with your answers, and we'll continue to **Topic 4: Nesterov Accelerated Gradient (NAG)**.
