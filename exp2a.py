import torch
import torch.nn as nn

# 1. Dummy data: [Size (sq ft / 1000), Bedrooms] -> Price ($100k)
X = torch.tensor([[1.0, 1.0], [1.5, 2.0], [2.0, 3.0], [2.5, 3.0]], dtype=torch.float32)
y = torch.tensor([[1.5], [2.3], [3.1], [3.7]], dtype=torch.float32)

# 2. Model, Loss, and Optimizer
model = nn.Linear(in_features=2, out_features=1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 3. Training Loop
for epoch in range(500):
    predictions = model(X)
    loss = criterion(predictions, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 4. Inference
test_input = torch.tensor([[1.8, 2.0]])
print("Predicted Price:", model(test_input).item())