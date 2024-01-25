from old_version.neuralNetwork import neuralNetwork
#this is a file to store all the parameters for the neural network
i = 784
o = 10
h = 100 
Lr = 0.2
n = neuralNetwork(i, h, o, Lr)
def i() :
    return i

def o() :
    return o

def h() : 
    return h

def Lr() :
    return Lr

def create():
    return n