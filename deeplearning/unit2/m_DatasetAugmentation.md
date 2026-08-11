# Topic 13: Dataset Augmentation

> **Exam Importance:** ⭐⭐⭐⭐☆ — Commonly asked and very important in computer vision

**Dataset Augmentation** is a regularization technique where we create **new training examples by making small, realistic changes to existing data**.

The goal is to make the model **generalize better** and reduce overfitting.

---

# ELI5 Explanation

Imagine you have only one photo of a cat.

Instead of taking 100 new photos, you can create variations:

```text
Original cat
   ↓
Flip it
   ↓
Rotate it
   ↓
Crop it
   ↓
Change brightness
```

Now the model sees the cat in many different situations.

The model learns:

> "I'm supposed to recognize the cat—not memorize this exact picture."

That's **Dataset Augmentation**.

---

# Real-World Example

Suppose you're training a model to recognize handwritten digits.

You have:

```text
7
```

You can create slightly modified versions:

```text
  7       7       7
 /       /       /
```

The number is still **7**, but its appearance changes.

This teaches the model to recognize the underlying pattern rather than one exact representation.

---

# Why Do We Need Dataset Augmentation?

Deep neural networks usually perform better with lots of diverse data.

But collecting data can be expensive.

For example:

```text
1000 original images
        ↓
Augmentation
        ↓
Many training variations
```

This effectively increases the **diversity** of the training data.

---

# Common Augmentation Techniques

## 1. Image Rotation

Rotate the image slightly.

```text
Original → Rotated
```

Example:

```text
🐱 → slightly rotated 🐱
```

Useful when orientation doesn't change the class.

---

## 2. Horizontal Flip

```text
Original → Mirror Image
```

Useful for objects where left/right orientation doesn't matter.

---

## 3. Cropping

Take a smaller region of the image.

```text
Full Image
   ↓
Random Crop
```

Makes the model less dependent on exact object positioning.

---

## 4. Scaling / Zooming

Zoom in or out.

This helps the model recognize objects at different sizes.

---

## 5. Translation

Move the object slightly:

```text
Center

   ↓

Left / Right / Up / Down
```

The model learns that location isn't always important.

---

## 6. Brightness / Contrast Changes

Change lighting conditions.

Example:

```text
☀️ Bright image
       ↓
🌙 Darker image
```

Useful because real-world lighting isn't always consistent.

---

## 7. Adding Noise

Small amounts of noise can be added to training examples.

This forces the model to learn robust patterns.

---

# Text/Data Augmentation

Augmentation isn't only for images.

For text, we can use techniques such as:

* Synonym replacement
* Random word deletion
* Word insertion
* Sentence paraphrasing

Example:

```text
Original:
"The movie was excellent."

Augmented:
"The film was excellent."
```

The meaning remains similar.

---

# Audio Augmentation

For speech/audio models:

* Add background noise.
* Change pitch.
* Change speed.
* Shift the audio slightly.

Example:

```text
Clean speech
     ↓
+ Background noise
     ↓
Noisy speech
```

The model becomes more robust to real-world conditions.

---

# Step-by-Step Example

Suppose we have only **4 images**:

```text
Image 1
Image 2
Image 3
Image 4
```

Apply augmentation:

```text
Image 1 → Flip
Image 1 → Rotate

Image 2 → Crop
Image 2 → Brightness change

Image 3 → Flip
Image 3 → Zoom

Image 4 → Rotate
Image 4 → Translation
```

Now the model sees many variations of the original examples.

---

# Important Point

Dataset augmentation does **not necessarily mean permanently creating thousands of files**.

Augmentation can happen **during training**.

For example:

```text
Original image
      ↓
Random transformation
      ↓
Neural network
```

The next training iteration can generate a different transformation.

This is called **online augmentation**.

---

# Offline vs Online Augmentation

| Type    | Meaning                                   |
| ------- | ----------------------------------------- |
| Offline | Create augmented data beforehand          |
| Online  | Create augmented versions during training |

### Online augmentation

```text
Image
 ↓
Random transformation
 ↓
Model
```

Next epoch:

```text
Same image
 ↓
Different random transformation
 ↓
Model
```

This can produce many variations without storing them all.

---

# Why Does Augmentation Reduce Overfitting?

Without augmentation:

```text
Training data
      ↓
Model memorizes examples
      ↓
Overfitting
```

With augmentation:

```text
Training data
      ↓
Many variations
      ↓
Model learns general patterns
      ↓
Better generalization
```

---

# Important Warning

Augmentation must make **realistic changes**.

Suppose you're classifying:

```text
Cat vs Dog
```

A horizontal flip is usually fine.

But if you apply a transformation that changes the actual class, it's harmful.

For example:

```text
Digit 6
  ↓
Rotate 180°
  ↓
Could look like 9
```

Now you've potentially created an incorrect training label.

So:

> **Augmentation should preserve the correct label.**

This is an important practical point.

---

# Advantages

* Reduces overfitting.
* Improves generalization.
* Makes models more robust.
* Useful when datasets are small.
* Increases data diversity.
* Can improve model accuracy.

---

# Disadvantages

* Excessive augmentation can make data unrealistic.
* Adds computational overhead.
* Poor transformations can introduce incorrect labels.
* Requires domain knowledge.

---

# Exam/Interview Must-Remember

### Dataset Augmentation

> Creating modified versions of existing training examples to increase data diversity and reduce overfitting.

### Common examples:

**Images:**

* Rotation
* Flipping
* Cropping
* Scaling
* Translation
* Brightness/contrast changes
* Noise

**Text:**

* Synonym replacement
* Deletion
* Insertion
* Paraphrasing

**Audio:**

* Noise
* Pitch changes
* Speed changes

---

# Quick Revision

```text
Dataset Augmentation
        ↓
Create realistic variations
        ↓
Increase data diversity
        ↓
Reduce overfitting
        ↓
Improve generalization
```

### One-line memory:

> **"Don't teach the model one picture; teach it the concept."**

---

# Connection

We've covered:

```text
Bias-Variance
     ↓
L1/L2
     ↓
Early Stopping
     ↓
Dataset Augmentation
     ↓
Next: Parameter Sharing & Parameter Tying
```

Now we're moving into techniques that **control how many independent parameters a network learns**.

---

# Active Learning

### Conceptual Questions

1. How does dataset augmentation help reduce overfitting?
2. Give **three examples** of image augmentation.
3. Why should augmentation preserve the original label?

### Practical Question

You're building a **cat-vs-dog image classifier** with only 1,000 training images.

Choose **four suitable augmentation techniques** from the following:

* Rotation
* Horizontal flip
* Random crop
* Brightness change
* Random vertical flip
* Adding moderate noise

Also explain briefly why you chose them.
