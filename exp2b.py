import torch
import torch.nn as nn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load tabular dataset
iris = load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names  # ['setosa', 'versicolor', 'virginica']

# Split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.long)

# 2. Simple Neural Network (4 inputs -> 16 hidden -> 3 classes)
model = nn.Sequential(
    nn.Linear(4, 16),
    nn.ReLU(),
    nn.Linear(16, 3)
)

# 3. Loss & Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 4. Training Loop
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

# 5. Testing & Terminal Output
model.eval()
with torch.no_grad():
    test_outputs = model(X_test)
    predictions = torch.argmax(test_outputs, dim=1)

print("\n--- SAMPLE PREDICTIONS IN TERMINAL ---")
print(f"{'Actual':<15} | {'Predicted':<15} | {'Match?'}")
print("-" * 42)
for actual, pred in zip(y_test[:8], predictions[:8]):
    act_name = target_names[actual.item()]
    pred_name = target_names[pred.item()]
    status = "✓ Correct" if actual == pred else "✗ Wrong"
    print(f"{act_name:<15} | {pred_name:<15} | {status}")

# Calculate overall test accuracy
accuracy = (predictions == y_test).float().mean().item() * 100
print("-" * 42)
print(f"Overall Test Accuracy: {accuracy:.2f}%\n")