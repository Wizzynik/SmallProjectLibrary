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

    def classify(self, start_inputs):
        outputs = self.calc_outputs(start_inputs)
        return index(outputs, max(outputs))

    #Calc Cost for one datapoint
    def cost(self, dataPoint):
        outputs = self.calc_outputs((dataPoint[0], dataPoint[1]))
        outputLayer = self.layers[self.layers.length - 1]
        cost = 0

        for nodeOut in range(outputs.length):
            cost += outputLayer.nodeCost(outputs[nodeOut], dataPoint.expectedOutputs[nodeOut])

        return cost

    #Actual Cost Funktion
    def costOverall(self, data):
        totalCost = 0

        for dataPoint in data:
            totalCost += self.cost(dataPoint)

        return totalCost / data.length

    # Learn function
    def learn (self, trainingData, learnRate):
        h = 0.0001
        originalCost = self.costOverall(trainingData)

        for layer in self.layers:
            for nodeIn in range(layer.numNodesIn):
                for nodeOut in range(layer.numNodesOut):
                    layer.weights[nodeIn][nodeOut] += h
                    deltaCost = self.costOverall(trainingData) - originalCost
                    layer.weights[nodeIn][nodeOut] -= h
                    layer.costGradientW[nodeIn][nodeOut] = deltaCost / h
                    
            for biasIndex in range(layer.biases.length):
                layer.biases[biasIndex] += h
                deltaCost = self.costOverall(trainingData) - originalCost
                layer.biases[biasIndex] -= h
                layer.costGradientB[biasIndex] = deltaCost / h
                    
        self.applyAllGradients(learnRate)