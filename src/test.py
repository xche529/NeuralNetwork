from neuralNetwork import neuralNetwork
import numpy
import json
import neural_parameters as np

#this is a script where you can test the neural network

weigth_file_name = input("Enter the name of the file containing the weights: ")
weigth_file_name += ".json"
with open(weigth_file_name, 'r') as file:
    weight_list = json.load(file)
    wih = weight_list[0]
    who = weight_list[1]

i = np.i()
o = np.o()  
h = np.h()
Lr = np.Lr()

n = neuralNetwork(i, h, o, Lr)
n.who = numpy.array(who)
n.wih = numpy.array(wih)

test_file_name = input("Enter the name of the file containing the test data: ")
test_file_name += ".csv"
test_file = open(test_file_name, 'r')
test_list = test_file.readlines()
test_file.close()

scorecard = []
#testing process
for image in test_list:
    all_values = image.split(',')
    correct_label = int(all_values[0])
    scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = n.query(scaled_input)
    label = numpy.argmax(outputs)
    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)
    pass

#display the result
print(scorecard)
result = sum(scorecard) / len(scorecard)
print("performance = ", result)