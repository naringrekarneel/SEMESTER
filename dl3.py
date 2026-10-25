import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# 1. Load MNIST Data
transform = transforms.ToTensor()
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# 2. Denoising Autoencoder Architecture
class DenoisingAutoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        # Encoder: 784 -> 64
        self.encoder = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 64),
            nn.ReLU()
        )
        # Decoder: 64 -> 784
        self.decoder = nn.Sequential(
            nn.Linear(64, 28 * 28),
            nn.Sigmoid(),
            nn.Unflatten(1, (1, 28, 28))
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))

model = DenoisingAutoencoder()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 3. Training Loop (Single epoch for exam demonstration)
model.train()
for batch_idx, (images, _) in enumerate(train_loader):
    # Add Gaussian noise and clamp to valid image range [0, 1]
    noise = 0.3 * torch.randn_like(images)
    noisy_images = torch.clamp(images + noise, 0.0, 1.0)
    
    outputs = model(noisy_images)
    loss = criterion(outputs, images)  # Target is the original clean image

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Train only 100 batches so it finishes in seconds during an exam run
    if batch_idx >= 100:
        break

print(f"Training Complete. Batch Loss: {loss.item():.4f}")

# 4. Visualizing Results on MNIST test sample
model.eval()
with torch.no_grad():
    sample_clean = images[:5]
    sample_noisy = torch.clamp(sample_clean + 0.3 * torch.randn_like(sample_clean), 0.0, 1.0)
    reconstructed = model(sample_noisy)

fig, axes = plt.subplots(3, 5, figsize=(10, 6))
for i in range(5):
    # Row 1: Original Clean
    axes[0, i].imshow(sample_clean[i].squeeze(), cmap='gray')
    axes[0, i].axis('off')
    if i == 0: axes[0, i].set_title("Original")

    # Row 2: Noisy Input
    axes[1, i].imshow(sample_noisy[i].squeeze(), cmap='gray')
    axes[1, i].axis('off')
    if i == 0: axes[1, i].set_title("Noisy Input")

    # Row 3: Denoised Output
    axes[2, i].imshow(reconstructed[i].squeeze(), cmap='gray')
    axes[2, i].axis('off')
    if i == 0: axes[2, i].set_title("Denoised")

plt.tight_layout()
plt.show()