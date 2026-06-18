import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
import torchvision.transforms as transforms
from torchvision.models import resnet18  # Just for illustration
from keras.engine.saving import load_model



import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageFolder
from imblearn.over_sampling import SMOTE
from torch.utils.data import Dataset
from torch import nn
from sklearn.preprocessing import StandardScaler

# Define your transformation (resize, normalize, etc.)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load the datasets
train_dataset = ImageFolder(
    root=r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Train',
    transform=transform)
val_dataset = ImageFolder(
    root=r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Validation',
    transform=transform)

# Convert the datasets to DataLoader for batching
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Flatten the images for SMOTE
def flatten_images(loader):
    data, labels = [], []
    for inputs, target in loader:
        data.append(inputs.view(inputs.size(0), -1).numpy())  # Flatten the images
        labels.append(target.numpy())
    data = np.concatenate(data)
    labels = np.concatenate(labels)
    return data, labels

# Flatten training images
X_train, y_train = flatten_images(train_loader)

# Apply SMOTE to balance the dataset
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Check the class distribution after applying SMOTE
print(f"Original class distribution: {np.bincount(y_train)}")
print(f"Resampled class distribution: {np.bincount(y_resampled)}")

# Convert resampled data back to Tensor
X_resampled = torch.tensor(X_resampled, dtype=torch.float32)
y_resampled = torch.tensor(y_resampled, dtype=torch.long)

# Create a new Dataset for the resampled data
class ResampledDataset(Dataset):
    def __init__(self, X, y, transform=None):
        self.X = X
        self.y = y
        self.transform = transform

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        image = self.X[idx].view(3, 224, 224)  # Reshape back to image format
        label = self.y[idx]
        if self.transform:
            image = self.transform(image)
        return image, label

# Create the resampled DataLoader
resampled_dataset = ResampledDataset(X_resampled, y_resampled, transform=transform)
resampled_loader = DataLoader(resampled_dataset, batch_size=32, shuffle=True)










# Define your custom ViT model
class ViT(nn.Module):
    def __init__(self, num_classes):
        super(ViT, self).__init__()
        # Replace this with your ViT model architecture
        self.backbone = resnet18(pretrained=True)
        self.backbone.fc = nn.Linear(512, num_classes)  # Adjust the output dimension for your task

    def forward(self, x):
        return self.backbone(x)


# Define transforms for your dataset
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize image
    transforms.ToTensor(),  # Convert images to PyTorch tensors
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize images
])

# Load your dataset
train_dataset = ImageFolder(
    root=r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Train',
    transform=transform)
val_dataset = ImageFolder(
    root=r'D:\archive (2)\Brain_Stroke_CT-SCAN_image\Validation',
    transform=transform)

# Define data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

val_loader = DataLoader(val_dataset, batch_size=32)

# Define your custom ViT model, loss function, and optimizer
num_classes = len(train_dataset.classes)
model = ViT(num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
# print(f'Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}, Val Loss: {val_epoch_loss:.4f}, Val Acc: {val_accuracy:.4f}, accuracy: {accuracy:.4f}')
hist = {'loss': [], "val_loss": [], "acc": [], "val_acc": []}
num_epochs = 20
for epoch in range(num_epochs):
    h = model.train()

    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
    epoch_loss = running_loss / len(train_dataset)

    # Validation loop
    model.eval()
    val_running_loss = 0.0
    correct_predictions = 0
    total_predictions = 0

    with torch.no_grad():
        for inputs, labels in train_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            val_running_loss += loss.item() * inputs.size(0)
            _, predicted = torch.max(outputs, 1)
            correct_predictions += (predicted == labels).sum().item()
            total_predictions += labels.size(0)
    accuracy = correct_predictions / total_predictions
    val_running_loss = 0.0
    correct_predictions = 0
    total_predictions = 0
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            val_running_loss += loss.item() * inputs.size(0)
            _, predicted = torch.max(outputs, 1)
            correct_predictions += (predicted == labels).sum().item()
            total_predictions += labels.size(0)
    val_epoch_loss = val_running_loss / len(val_dataset)
    val_accuracy = correct_predictions / total_predictions

    hist['loss'].append(epoch_loss)
    hist['val_loss'].append(val_epoch_loss)
    hist['acc'].append(accuracy)
    hist['val_acc'].append(val_accuracy)
    print(
        f'Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}, Val Loss: {val_epoch_loss:.4f}, Val Acc: {val_accuracy:.4f}, accuracy: {accuracy:.4f}')

import matplotlib.pyplot as plt

h = hist
plt.plot(range(1, num_epochs + 1), h['loss'], label='Train Loss')
plt.plot(range(1, num_epochs + 1), h['val_loss'], label='Val Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()


# Plot the validation accuracy
plt.plot(range(1, num_epochs + 1), h['val_acc'], label='Val Accuracy')
plt.plot(range(1, num_epochs + 1), h['acc'], label='Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Validation Accuracy')
plt.legend()
plt.show()


torch.save(model.state_dict(), 'vit_model1.h5')