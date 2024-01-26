import neural_parameters
import json
import numpy


class NumberReader:

    def __init__(self):
        self.weights_file_name = ''
        self.neural_network = neural_parameters.create()

    def read(self, pixels):
        result = self.neural_network.query(pixels)
        return result
    
    
    def read_weights(self, weights_file_name):
        with open(weights_file_name, 'r') as weights_file:
            weight_list = json.load(weights_file)
        self.neural_network.who = numpy.array(weight_list[1]) 
        self.neural_network.wih = numpy.array(weight_list[0]) 

