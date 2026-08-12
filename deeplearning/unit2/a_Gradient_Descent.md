# Topic 1: Gradient Descent (GD)

This is the **foundation** of all optimization algorithms. Every advanced optimizer (Momentum, Adam, RMSProp, etc.) is basically an improvement over Gradient Descent.

---

# ELI5 Explanation 🧒

Imagine you're standing on top of a foggy mountain.

Your goal is to reach the **lowest point (valley).**

Because of the fog, you cannot see the whole mountain.

So what do you do?

You simply check:

> "Which direction is downhill?"

Take one step.

Again check.

Take another step.

Repeat until you reach the bottom.

That's exactly how Gradient Descent works.

- **Mountain** = Loss Function
- **Valley** = Minimum Loss
- **You** = Neural Network
- **Steps** = Updating Weights

---

# Real-World Intuition

Suppose you're learning basketball.

At first, you miss many shots.

Your coach tells you your mistakes.

You slightly adjust your technique.

You try again.

Eventually you become better.

The coach's feedback is like the **gradient**.

Your adjustment is the **Gradient Descent update.**

---

# Why Do We Need Gradient Descent?

Neural networks contain **millions of weights.**

Example:

```text
Weight 1 = 0.42
Weight 2 = -0.85
Weight 3 = 1.21
...
Weight 1,000,000
```

We need a way to automatically improve these weights.

Gradient Descent tells every weight:

> "Move a little in the direction that reduces error."

---

# Important Terms

## 1. Loss Function

Measures how wrong the prediction is.

Examples:

- Mean Squared Error (Regression)
- Cross Entropy (Classification)

**Smaller loss = Better model.**

---

## 2. Gradient

The gradient tells us:

> "Which direction increases the loss the fastest?"

To decrease the loss, we move in the **opposite direction** of the gradient.

---

## 3. Learning Rate (\(\eta\))

The learning rate decides **how big each step should be.**

### Very Small Learning Rate

```text
🐢

Tiny steps

Training becomes very slow.
```

### Very Large Learning Rate

```text
🏃

Jumps everywhere

Never reaches the minimum.
```

### Good Learning Rate

```text
🙂

Steady movement

Reaches the minimum efficiently.
```

---

# Core Formula ⭐⭐⭐⭐⭐

Gradient Descent updates every weight using:

\[
\boxed{
W_{\text{new}}
=
W_{\text{old}}
-
\eta
\frac{\partial L}{\partial W}
}
\]

where

- \(W_{\text{new}}\) = Updated weight
- \(W_{\text{old}}\) = Current weight
- \(\eta\) = Learning rate
- \(L\) = Loss function
- \(\dfrac{\partial L}{\partial W}\) = Gradient (partial derivative of loss with respect to the weight)

### Must Remember

\[
\boxed{
\text{New Weight}
=
\text{Old Weight}
-
\left(
\text{Learning Rate}
\times
\text{Gradient}
\right)
}
\]

---

# Step-by-Step Example

Suppose

- Current Weight = \(8\)
- Gradient = \(3\)
- Learning Rate = \(0.1\)

Using the Gradient Descent formula,

\[
\begin{aligned}
W_{\text{new}}
&=
8
-
(0.1 \times 3)
\\[8pt]
&=
8
-
0.3
\\[8pt]
&=
7.7
\end{aligned}
\]

So,

\[
\boxed{W_{\text{new}} = 7.7}
\]

The weight moves slightly toward reducing the error.

---

# Another Example

Suppose

- Weight = \(5\)
- Gradient = \(-4\)
- Learning Rate = \(0.2\)

Calculation:

\[
\begin{aligned}
W_{\text{new}}
&=
5
-
(0.2 \times -4)
\\[8pt]
&=
5
+
0.8
\\[8pt]
&=
5.8
\end{aligned}
\]

Therefore,

\[
\boxed{W_{\text{new}} = 5.8}
\]

Notice:

A **negative gradient** causes the weight to increase.

The update always moves in the direction that reduces the loss.

---

# Visual Idea

```text
Loss

^
|
|      ● Start
|      \
|       \
|        \
|         \
|          \
|           ●
|            \
|             ●
|              \
|_______________●________________> Weight

               Minimum Loss
```

Each dot represents one Gradient Descent update.

---

# Gradient Descent Algorithm

1. Initialize weights randomly.
2. Pass the training data through the network (Forward Pass).
3. Calculate the loss.
4. Compute gradients using Backpropagation.
5. Update the weights using the Gradient Descent formula.
6. Repeat until the loss stops decreasing or a stopping criterion is met.

### Flow

```text
Initialize Weights
        ↓
Forward Pass
        ↓
Calculate Loss
        ↓
Backpropagation
        ↓
Compute Gradients
        ↓
Update Weights
        ↓
Repeat
```

---

# Advantages

- Simple to understand.
- Easy to implement.
- Foundation of all modern optimization algorithms.
- Works well for many machine learning problems.

---

# Disadvantages

- Can be slow on large datasets.
- May get stuck in local minima or saddle points.
- Sensitive to the learning rate.
- Full Batch Gradient Descent requires processing the entire dataset before every update.

---

# Exam/Interview Must-Remember Points

| Question | Answer |
|----------|--------|
| Purpose of Gradient Descent? | Minimize the loss function. |
| What does the gradient indicate? | Direction of the steepest increase in loss. |
| Why do we subtract the gradient? | To move toward lower loss. |
| What is the learning rate? | Controls the step size of each update. |
| Formula | \(\displaystyle \boxed{W_{\text{new}} = W_{\text{old}} - \eta \frac{\partial L}{\partial W}}\) |

---

# Quick Revision Sheet

- Gradient Descent minimizes the loss function.
- Weights are updated iteratively.
- Uses gradients computed by Backpropagation.
- Learning rate controls the update size.
- Too small learning rate → Slow convergence.
- Too large learning rate → Overshooting or divergence.
- Foundation of optimizers like Momentum, RMSProp, and Adam.

---

# Active Learning

## Conceptual Questions

1. Why do we move in the **opposite** direction of the gradient instead of following it?

2. What happens if the learning rate is extremely large?

3. In one sentence, what is the purpose of Gradient Descent?

---

## Practical Question

A neural network has:

- Weight = \(12\)
- Gradient = \(5\)
- Learning Rate = \(0.2\)

Using the Gradient Descent update rule,

\[
\begin{aligned}
W_{\text{new}}
&=
12
-
(0.2 \times 5)
\\[8pt]
&=
12
-
1
\\[8pt]
&=
11
\end{aligned}
\]

Final Answer:

\[
\boxed{W_{\text{new}} = 11}
\]

Reply with your answers, and I'll check them before moving on to **Topic 2: Stochastic Gradient Descent (SGD) & Mini-batch Gradient Descent**.
