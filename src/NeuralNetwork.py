import numpy
import scipy.special

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate) :
        self.In = inputnodes
        self.Hid = hiddennodes
        self.Out = outputnodes
        self.Lr = learningrate
        # create weight matrices, wih and who with random normal distribution 
        self.wih = numpy.random.normal(0.0, pow(self.Hid, -0.5), (self.Hid, self.In))
        self.who = numpy.random.normal(0.0, pow(self.Out, -0.5), (self.Out, self.Hid))
        # define activation function 
        self.activation_function = lambda x: scipy.special.expit(x)
        
    def train() :
        pass
        
    def query(self,input_list):
        inputs = numpy.array(input_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        