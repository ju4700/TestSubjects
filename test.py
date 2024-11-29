import torch
import torch.nn as nn
import torch.optim as optim


class MatrixInverseModel(nn.Module):
    def __init__(self, input_size):
        super(MatrixInverseModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 256)
        self.fc3 = nn.Linear(256, input_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def generate_data(n, matrix_size):
    matrices = []
    inverses = []
    for _ in range(n):
        matrix = torch.rand(matrix_size, matrix_size)
        if torch.det(matrix) != 0:  # Check if invertible
            inverse = torch.inverse(matrix)
            matrices.append(matrix.flatten())
            inverses.append(inverse.flatten())
    return torch.stack(matrices), torch.stack(inverses)


# Training loop
def train(model, data, targets, epochs=1000, learning_rate=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        if epoch % 100 == 0:
            print(f'Epoch {epoch}/{epochs}, Loss: {loss.item()}')


# Initialize the model
matrix_size = 3
model = MatrixInverseModel(matrix_size * matrix_size)

data, targets = generate_data(500, matrix_size)

train(model, data, targets)

test_matrix = torch.rand(matrix_size, matrix_size)
if torch.det(test_matrix) != 0:
    test_matrix_flat = test_matrix.flatten().unsqueeze(0)
    predicted_inverse_flat = model(test_matrix_flat)
    predicted_inverse = predicted_inverse_flat.reshape(matrix_size, matrix_size)
    print("Predicted Inverse:\n", predicted_inverse)
    print("Actual Inverse:\n", torch.inverse(test_matrix))
else:
    print("Generated matrix is not invertible")
