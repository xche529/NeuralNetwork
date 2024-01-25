from old_version.neuralNetwork import neuralNetwork
import numpy
import matplotlib.pyplot as plt
import json
import old_version.neural_parameters as np

#this is script where you can create the weights for the neural network and save it to a file
n = np.create()
file_name = input("Enter the name of the file you want to save the neural Network to: ")
file_name = file_name + '.json'
wih = n.wih.tolist()
who = n.who.tolist()
weight = [wih, who]
with open(file_name, 'w') as file:
    json.dump(weight, file)
print("Done!")
