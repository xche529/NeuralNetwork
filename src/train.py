from neuralNetwork import neuralNetwork
import numpy
import matplotlib.pyplot as plt
#this is the script where you can train the neural network 
input = 784
output = 10
hidden = 100
Lr = 0.4
data_file = open("train_data.csv", 'r')
data_list = data_file.readlines()
data_file.close()

num_train = int(input("Enter the number of test run you want: "))
file = input("Enter the name of the file you want to save the neural network to: ")

n = neuralNetwork(input, hidden, output, Lr)

#training process
for image in data_list:
    all_values = image.split(',')
    scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = numpy.zeros(output) + 0.01

    targets[int(all_values[0])] = 0.99
    print(targets)
    n.train(scaled_input, targets)
pass