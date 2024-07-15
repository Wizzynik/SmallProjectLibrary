import math
from random import random


class Layer:
    # Num nodes in last layer
    numNodesIn = None
    # Num nodes in this layer
    numNodesOut = None
    
    costGradientW = [[]]
    costGradientB = []
    # List of Lists of weights for each node
    weights = [[]]
    # List of biases for each node
    biases = [] 
    
    # Constructor
    def __init__(self, nodesIn, nodesOut):
        self.numNodesIn = nodesIn
        self.numNodesOut = nodesOut
            
    def initializeRandomWeights(self):
        # generate random number
        for nodeIn in range(self.numNodesIn):
            for nodeOut in range(self.numNodesOut):
                randomValue = random() * 2 - 1
                self.weights[nodeIn][nodeOut] = randomValue / math.sqrt(self.numNodesIn) 
        
    def activationFunction_sigmoid(self, xValue):
        return 1 / (1 + math.exp(-xValue))
    
    def activationFunction_hyperbolicTangent(self, xValue):
        e2w = math.exp(2*xValue)
        return (e2w - 1) / (e2w + 1)
    
    def activationFunction_SiLU(self, xValue):
        return xValue / (1 + math.exp(-xValue))
    
    def activationFunction_ReLU(self, xValue):
        return max(0, xValue)
        
    def calc_output(self, inputs):
        activations = []
        for nodeOut in range(self.numNodesOut):
            weightedInput = self.biases[nodeOut]
            for nodeIn in range(self.numNodesIn):
                weightedInput += inputs[nodeIn] * self.weights[nodeIn][nodeOut]
            # Add the weighted input to the list of outputs
            activations.append(self.activationFunction(weightedInput))  
                  
        return activations
    
    def nodeCost(outputActivation, expectedOutput):
        error = outputActivation - expectedOutput
        return error * error
    
    def applyGradients(self, learnRate):
        for nodeOut in range(self.numNodesOut):
            self.biases[nodeOut] -= self.costGradientB[nodeOut] * learnRate
            for nodeIn in range(self.numNodesIn):
                self.weights[nodeIn][nodeOut] = self.costGradientW[nodeIn][nodeOut] * learnRate
                