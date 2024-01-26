import neural_parameters
import json
import numpy


class NumberReader:

    def __init__(self, weights_file_name):
        self.neural_network = neural_parameters.create()
        self.read_weights(weights_file_name)
        self.neural_network.who = numpy.array(self.who)
        self.neural_network.wih = numpy.array(self.wih)

    def read(self, image):
        pass
    
    
    def read_weights(self, weights_file_name):
        weight_list = json.load(weights_file_name)
        self.wih = weight_list[0]
        self.who = weight_list[1]

