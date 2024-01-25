from old_version.neuralNetwork import neuralNetwork
import numpy
import json
import old_version.neural_parameters as np

#this is a script where you can reverse the neural network to get the image from the output
weigth_file_name = input("Enter the name of the file containing the weights: ")
weigth_file_name += ".json"
with open(weigth_file_name, 'r') as file:
    weight_list = json.load(file)
    wih = weight_list[0]
    who = weight_list[1]

n = np.create()
n.who = numpy.array(who)
n.wih = numpy.array(wih)


number = input("Enter the number you want to reverse: ")
targets = numpy.zeros(o) + 0.01
targets[int(number)] = 0.99

image = n.reverse(targets)

image = numpy.array(image)
numpy.imshow(image.reshape(28,28), cmap='Greys', interpolation='None')