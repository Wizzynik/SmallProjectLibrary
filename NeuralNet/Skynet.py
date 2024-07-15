from Layer import Layer

# Main management class for neural network
class Skynet:
    def __init__(self, layerSizes):
        self.layers = []
        for i in range(len(layerSizes) - 1):
            self.layers.append(Layer(layerSizes[i], layerSizes[i+1]))
            
    # Calculate the output of the network given an Array of inputs
    def calc_outputs(self, inputs):
        for layer in self.layers:
            inputs = layer.calc_output(inputs)
        return inputs

    def classify(self, start_inputs):
        outputs = self.calc_outputs(start_inputs)
        return outputs.index(max(outputs))

    # Calc Cost for one datapoint
    def cost(self, dataPoint):
        outputs = self.calc_outputs((dataPoint[0], dataPoint[1]))
        expectedOutputs = [1, 0] if dataPoint[1] < (dataPoint[0] ** 2) / 2000 else [0, 1]
        return sum((o - e) ** 2 for o, e in zip(outputs, expectedOutputs))

    # Actual Cost Function
    def costOverall(self, data):
        return sum(self.cost(dataPoint) for dataPoint in data) / len(data)

    # Learn function
    def learn(self, trainingData, learnRate):
        h = 0.0001
        originalCost = self.costOverall(trainingData)

        for layer in self.layers:
            for nodeIn in range(layer.numNodesIn):
                for nodeOut in range(layer.numNodesOut):
                    layer.weights[nodeIn][nodeOut] += h
                    deltaCost = self.costOverall(trainingData) - originalCost
                    layer.weights[nodeIn][nodeOut] -= h
                    layer.costGradientW[nodeIn][nodeOut] = deltaCost / h
                    
            for biasIndex in range(len(layer.biases)):
                layer.biases[biasIndex] += h
                deltaCost = self.costOverall(trainingData) - originalCost
                layer.biases[biasIndex] -= h
                layer.costGradientB[biasIndex] = deltaCost / h
                    
        for layer in self.layers:
            layer.applyGradients(learnRate)