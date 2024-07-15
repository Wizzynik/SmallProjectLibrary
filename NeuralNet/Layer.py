import math
from random import random

class Layer:
    def __init__(self, nodesIn, nodesOut):
        self.numNodesIn = nodesIn
        self.numNodesOut = nodesOut
        self.weights = [[random() * 2 - 1 for _ in range(nodesOut)] for _ in range(nodesIn)]
        self.biases = [random() * 2 - 1 for _ in range(nodesOut)]
        self.costGradientW = [[0 for _ in range(nodesOut)] for _ in range(nodesIn)]
        self.costGradientB = [0 for _ in range(nodesOut)]

    def activationFunction_sigmoid(self, xValue):
        return 1 / (1 + math.exp(-xValue))

    def activationFunction_hyperbolicTangent(self, xValue):
        return math.tanh(xValue)

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
            activations.append(self.activationFunction_hyperbolicTangent(weightedInput))
        return activations

    def applyGradients(self, learnRate):
        for nodeOut in range(self.numNodesOut):
            self.biases[nodeOut] -= self.costGradientB[nodeOut] * learnRate
            for nodeIn in range(self.numNodesIn):
                self.weights[nodeIn][nodeOut] -= self.costGradientW[nodeIn][nodeOut] * learnRate