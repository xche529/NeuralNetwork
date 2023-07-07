from neuralNetwork import neuralNetwork
import numpy
import matplotlib.pyplot as plt


#this is the main script where you can build and train the neural network and test it
input = 784
output = 10
hidden = 100
Lr = 0.4
data_file = open("train_data.csv", 'r')
data_list = data_file.readlines()
data_file.close()
#all_values = data_list[0].split(',')
#image_array = numpy.asfarray(all_values[1:]).reshape((28,28))

#plt.imshow(image_array, cmap='Greys', interpolation='None')
#interpolation='None'
#plt.show()
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


#this is the testing process below  
image = data_list[1]
all_values = image.split(',')
scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

result = n.query(scaled_input)
for i in range(len(result)):
    if result[i] == numpy.amax(result):
        index = i
        break
print(str(index) + "is the result")
print("it should be " + str(all_values[0]))
print(result)