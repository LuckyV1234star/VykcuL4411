import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms


# Define the neural network model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # Flatten 28x28 image to 784 features
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)  # 10 output classes (digits 0-9)

    def forward(self, x):
        x = torch.flatten(x, 1)  # Flatten input tensor
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 1. Define transformations for the images
transform = transforms.Compose([
    transforms.ToTensor(),  # Convert image to PyTorch tensor
    transforms.Normalize((0.1307,), (0.3081,))  # Normalize MNIST data
])

# 2. Load MNIST dataset
train_dataset = datasets.MNIST('../data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('../data', train=False, transform=transform)

# 3. Create data loaders (for batching)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1000, shuffle=False)


# 4. Initialize the model, loss function, and optimizer
model = Net()
criterion = nn.CrossEntropyLoss() # For multi-class classification
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)


# 5. Train the model
epochs = 2  # Adjust the number of epochs as needed

for epoch in range(epochs):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:  # Print loss every 2000 mini-batches
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')

# 6. Test the model
correct = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')

torch.save(model.state_dict(), './temp')

model = Net()
model.load_state_dict(torch.load('./temp'))
model.eval() # Set the model to evaluation mode

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

image = open('./img/can/boss.jpg').convert('L') # Convert to grayscale
image_tensor = transform(image).unsqueeze(0) # Add a batch dimension

with torch.no_grad():
    output = model(image_tensor)
    _, predicted = torch.max(output, 1)
    print(f"Predicted digit: {predicted.item()}")