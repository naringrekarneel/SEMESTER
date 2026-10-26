import torch
import torch.nn as nn
X = torch.tensor([[1.0, 1.0], [1.5, 2.0], [2.0, 3.0], [2.5, 3.0]])
y = torch.tensor([[1.5], [2.3], [3.1], [3.7]])

model = nn.Linear(2, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(500):
    pred = model(X)
    loss = criterion(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(model(torch.tensor([[1.8, 2.0]])).item())
