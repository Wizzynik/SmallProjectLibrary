# imports
from operator import index
from Layer import Layer

# Main management class for neural network
class Skynet:
    layers = []
    
    def __init__(self, inputLayers):
        for i in range(len(inputLayers) - 1):
            self.layers.append(Layer(inputLayers[i], inputLayers[i+1]))
            
# Calculate the output of the network given an Array of inputs
def calc_outputs(self, inputs):
    for layer in self.layers:
        inputs = layer.calc_output(inputs)
    return inputs

def start(start_inputs):
    outputs = calc_outputs(start_inputs)
    return index(outputs, max(outputs))