import numpy as np

# 1. Dataset (XOR logic gate)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# 2. Activation and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 3. Initialize weights and biases
np.random.seed(42)
W1 = np.random.uniform(size=(2, 4))
b1 = np.zeros((1, 4))
W2 = np.random.uniform(size=(4, 1))
b2 = np.zeros((1, 1))

lr = 0.1

# 4. Training loop
for epoch in range(10000):
    # Forward Pass
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2)

    # Backpropagation
    error = y - output
    d_output = error * sigmoid_derivative(output)
    
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(a1)

    # Weight updates
    W2 += a1.T.dot(d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += X.T.dot(d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

# 5. Testing
print("Predictions after training:")
print(np.round(output))