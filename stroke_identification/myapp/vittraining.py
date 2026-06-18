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

# Now you can use the `resampled_loader` for training your model
