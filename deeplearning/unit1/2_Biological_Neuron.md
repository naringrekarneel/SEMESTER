# Topic 2: Biological Neuron

Before understanding Artificial Neural Networks, we must first understand the **Biological Neuron**, because it inspired the design of neural networks used in Deep Learning.

---

# ELI5 (Explain Like I'm 5)

Imagine your brain is a huge city with billions of people sending messages to each other.

Each person is called a **neuron**.

When one person receives enough important messages, they pass the message to another person.

This is exactly how neurons in our brain work.

Example:

You touch a hot pan.

1. Your skin senses heat.
2. Neurons send signals to your brain.
3. Your brain processes the information.
4. Your brain sends another signal.
5. Your hand immediately moves away.

This entire process happens in a fraction of a second.

---

# What is a Biological Neuron?

A **biological neuron** is the basic structural and functional unit of the nervous system. It receives information, processes it, and sends it to other neurons through electrical and chemical signals.

The human brain contains approximately **86 billion neurons**, all connected in a vast communication network.

---

# Structure of a Biological Neuron

A biological neuron has four main parts:

| Part                      | Function                                          |
| ------------------------- | ------------------------------------------------- |
| Dendrites                 | Receive signals from other neurons                |
| Cell Body (Soma)          | Processes the received signals                    |
| Axon                      | Carries the output signal away from the cell body |
| Axon Terminals (Synapses) | Pass the signal to the next neuron                |

Flow of information:

```text
Dendrites
     ↓
 Cell Body (Soma)
     ↓
    Axon
     ↓
Axon Terminals
     ↓
Next Neuron
```

---

# Real-World Analogy

Think of a courier service.

* **Dendrites** → Delivery staff collecting parcels.
* **Cell Body** → Sorting center where parcels are checked.
* **Axon** → Delivery truck carrying parcels.
* **Axon Terminals** → Delivery person handing the parcel to the next customer.

Information moves from one neuron to another just like parcels move through a courier network.

---

# How Does a Neuron Work?

Suppose you accidentally touch a hot object.

### Step 1

Your skin detects heat.

### Step 2

Sensory neurons receive the signal through dendrites.

### Step 3

The cell body decides whether the signal is strong enough.

### Step 4

If the signal crosses a certain threshold, it travels through the axon.

### Step 5

The signal reaches another neuron or a muscle.

### Step 6

Your muscles contract, and you quickly pull your hand away.

---

# Important Concept: Threshold

A neuron does **not** fire for every tiny signal.

It combines all incoming signals.

* If the total signal is **below the threshold**, nothing happens.
* If the total signal is **greater than or equal to the threshold**, the neuron fires.

Example:

Threshold = 10

Signals received:

* Signal A = 3
* Signal B = 2
* Signal C = 4

Total = 9

Since 9 < 10, the neuron does **not** fire.

Now another signal arrives:

* Signal D = 3

Total = 12

Since 12 ≥ 10, the neuron fires.

This idea later becomes the foundation of the **Artificial Neuron**.

---

# Connection to Artificial Intelligence

Scientists wanted computers to learn the way humans learn.

So they copied the basic working of biological neurons.

Comparison:

| Biological Neuron | Artificial Neuron   |
| ----------------- | ------------------- |
| Dendrites         | Input features      |
| Synapse           | Weights             |
| Cell Body         | Summation function  |
| Threshold         | Activation function |
| Axon              | Output              |

This comparison forms the basis of Artificial Neural Networks (ANNs).

---

# Why is the Biological Neuron Important?

Understanding biological neurons helps explain why neural networks use:

* Inputs
* Weights
* Summation
* Activation functions
* Outputs

Every artificial neuron is inspired by this natural model.

---

# Worked Example

Imagine a student deciding whether to study.

Inputs:

* Exam tomorrow = Yes
* Homework pending = Yes
* Feeling tired = Yes

The brain combines all these signals.

If the motivation becomes strong enough (crosses the threshold), the student starts studying.

Otherwise, they continue watching videos.

This is similar to how a neuron decides whether to fire.

---

# Exam Definition (2–3 Marks)

**Biological Neuron:**
A biological neuron is the basic functional unit of the nervous system that receives information through dendrites, processes it in the cell body, and transmits signals through the axon to other neurons or muscles.

---

# Frequently Asked Exam/Interview Questions

1. What is a biological neuron?
2. Draw and label the structure of a biological neuron.
3. Explain the function of dendrites, soma, axon, and synapse.
4. How does a biological neuron inspire artificial neural networks?
5. What is meant by the threshold of a neuron?

---

# Must-Remember Points

* Neurons are the basic units of the nervous system.
* The brain contains about **86 billion neurons**.
* Dendrites receive signals.
* Soma processes signals.
* Axon carries signals.
* Synapses connect neurons.
* A neuron fires only when the received signal crosses a threshold.
* Artificial neurons are modeled after biological neurons.

---

# Quick Revision Bullets

* Biological neuron = basic unit of the brain.
* Four parts: Dendrites, Soma, Axon, Synapse.
* Dendrites receive information.
* Soma processes information.
* Axon sends information.
* Neuron fires only after crossing a threshold.
* Artificial neurons are inspired by biological neurons.

---

# Active Learning

### Conceptual Questions

1. What are the four main parts of a biological neuron?
2. What is the function of the axon?
3. Why is the threshold concept important in a biological neuron?

### Practical Question

Suppose a neuron has a threshold value of **15** and receives signals **4, 5, and 3**. Will the neuron fire? If another signal of **4** arrives, what happens? Explain your answer.
