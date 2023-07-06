from NeuralNetwork import neuralNetwork

input = 3
output = 3
hidden = 3
Lr = 0.3
n = neuralNetwork(input, hidden, output, Lr)
result = n.query([1.0, 0.5, -1.5])
print(result)