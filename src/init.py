from neuralNetwork import neuralNetwork
import numpy
import matplotlib.pyplot as plt
import json

#this is the main script where you can build and train the neural network and test it
input = 784
output = 10
hidden = 100
Lr = 0.4
n = neuralNetwork(input, hidden, output, Lr)
name = input("Enter the name of the file you want to save the neural Network to: ")
