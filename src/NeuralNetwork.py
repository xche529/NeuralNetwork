import numpy

class neuralNetwork:
    
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate) :
        self.In = inputnodes
        self.Hid = hiddennodes
        self.Out = outputnodes
        self.Lr = learningrate
        # create weight matrices, wih and who with random normal distribution 
        self.wih = numpy.random.normal(0.0, pow(self.Hid, -0.5), (self.Hid, self.In))
        self.who = numpy.random.normal(0.0, pow(self.Out, -0.5), (self.Out, self.Hid))
        
        
    def train() :
        pass
        
    def query() :
        pass