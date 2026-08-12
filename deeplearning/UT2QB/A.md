# SGD, Momentum-Based GD and Nesterov Accelerated Gradient — 10 Marks

## 1. Introduction

**Gradient Descent (GD)** is an optimization algorithm used to minimize the loss function of a neural network by updating its weights in the direction of the negative gradient.

Three important variants are:

1. **Stochastic Gradient Descent (SGD)**
2. **Momentum-based Gradient Descent**
3. **Nesterov Accelerated Gradient (NAG)**

The main difference is **how they use the current gradient and previous updates to decide the next step**.

---

# 2. Stochastic Gradient Descent (SGD)

In standard batch Gradient Descent, the gradient is calculated using the entire training dataset.

In **SGD**, the weights are updated using **one training example at a time**.

The update equation is written as display math:

$$
W_{t+1} = W_t - \eta \nabla L(W_t)
$$

where:

* $W_t$ = current weights
* $\eta$ = learning rate
* $\nabla L(W_t)$ = gradient of loss

### Advantages

* Faster updates
* Requires less memory
* Can work well with large datasets
* Noise in updates can sometimes help escape shallow local minima

### Disadvantage

The updates can be **noisy and oscillatory**.

---

# 3. Momentum-Based Gradient Descent

Momentum improves SGD by remembering part of the **previous update direction**.

Instead of using only the current gradient, it maintains a velocity:

$$
v_t = \beta v_{t-1} + \nabla L(W_t)
$$

Then the weights are updated using this velocity:

$$
W_{t+1} = W_t - \eta v_t
$$

where:

* $v_t$ = velocity
* $\beta$ = momentum coefficient, usually close to 1
* $\eta$ = learning rate

### Intuition

Think of a ball rolling downhill.

* The **gradient** tells it which way the slope points now.
* **Momentum** gives the ball some memory of where it was already moving.

So the optimizer builds speed in a consistent direction instead of constantly reacting to every small change in the gradient.

---

# 4. How Momentum Helps Traverse Ravines

A **ravine** is a long, narrow region of the loss surface.

Imagine:

```text
          ↕ oscillation
        /\/\/\/\/\/\/\/\
       /              \
      /                \
     /__________________\
              →
        direction of progress
```

In a ravine:

* The gradient changes sharply in the **steep direction**.
* The useful direction toward the minimum is relatively **flat**.

With ordinary SGD, the optimizer tends to:

* Move rapidly across the steep direction.
* Oscillate from one side of the ravine to the other.
* Make relatively slow progress along the ravine.

Momentum reduces these oscillations.

Conceptually:

$$
\text{Momentum} = \text{current gradient} + \text{memory of previous movement}
$$

If successive gradients point in roughly the same direction, momentum accumulates them and speeds up movement.

If the gradients repeatedly change direction, their effects tend to cancel, reducing the oscillation.

Thus, momentum helps the optimizer **move faster along the ravine while damping unnecessary side-to-side movement**.

---

# 5. Nesterov Accelerated Gradient (NAG)

**NAG** is an improved form of momentum.

The key difference is that NAG calculates the gradient **after looking ahead in the direction of the current momentum**.

First calculate the look-ahead position:

$$
W_t^{\text{lookahead}} = W_t - \eta \beta v_{t-1}
$$

Then calculate the gradient at this look-ahead position:

$$
g_t = \nabla L\bigl(W_t - \eta \beta v_{t-1}\bigr)
$$

The velocity is then updated:

$$
v_t = \beta v_{t-1} + g_t
$$

and the weights are updated:

$$
W_{t+1} = W_t - \eta v_t
$$

### Simple idea

Momentum asks:

> **"Where am I going based on my current position and previous momentum?"**

NAG asks:

> **"If I continue moving in this direction, what will the gradient look like there?"**

So NAG can **anticipate changes in the gradient** and correct its movement earlier.

---

# 6. Comparison

| Feature                | **SGD**          | **Momentum GD**                   | **NAG**                      |
| ---------------------- | ---------------- | --------------------------------- | ---------------------------- |
| Uses current gradient  | Yes              | Yes                               | Yes                          |
| Uses previous velocity | No               | Yes                               | Yes                          |
| Looks ahead            | No               | No                                | **Yes**                      |
| Oscillation            | High             | Reduced                           | Further reduced              |
| Convergence            | Can be slow      | Faster                            | Often faster/more controlled |
| Ravine traversal       | Poorer           | Better                            | Better and more responsive   |
| Memory required        | Low              | Extra velocity                    | Extra velocity               |
| Main advantage         | Simple and cheap | Accelerates consistent directions | Anticipates future gradient  |

---

# 7. Key Difference

The easiest way to remember:

### SGD

$$
\text{Current gradient only}
$$

### Momentum

$$
\text{Current gradient + previous velocity}
$$

### NAG

$$
\text{Look ahead + gradient + previous velocity}
$$

---

# 8. Example of Ravine Behavior

Suppose the optimizer is moving toward a minimum, but the loss surface is very steep horizontally and shallow vertically.

### SGD

```text
↗ ↘ ↗ ↘ ↗ ↘
```

It repeatedly crosses the ravine and wastes steps.

### Momentum

```text
↗ → → → → →
```

The accumulated velocity reduces the side-to-side oscillation and increases movement toward the minimum.

### NAG

```text
→ → → → ✓
```

It looks ahead and adjusts the direction before overshooting as much.

---

## 9. Advantages of Momentum and NAG

### Momentum

* Reduces oscillations.
* Speeds up convergence.
* Helps traverse long, narrow ravines.
* Makes optimization less sensitive to small gradient changes.

### NAG

* Retains the benefits of momentum.
* Uses a look-ahead gradient.
* Can respond earlier to changes in the loss surface.
* Often provides more precise convergence than ordinary momentum.

---

## 10. Conclusion

**SGD** updates weights using the current gradient and is simple but can produce noisy, oscillating updates. **Momentum-based GD** adds memory of previous updates, reducing oscillations and accelerating convergence. **NAG** further improves momentum by looking ahead and often gives more responsive updates near minima.
