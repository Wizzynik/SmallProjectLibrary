import math


class Layer:
    # Num nodes in last layer
    numNodesIn = None
    # Num nodes in this layer
    numNodesOut = None
    # List of Lists of weights for each node
    weights = [[]]
    # List of biases for each node
    biases = [] 
    
        # Constructor
    def __init__(self, nodesIn, nodesOut):
        self.numNodesIn = nodesIn
        self.numNodesOut = nodesOut
        
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
        for i in range(self.numNodesOut):
            weightedInput = self.biases[i]
            for j in range(self.numNodesIn):
                weightedInput += inputs[j] * self.weights[i][j]
            # Add the weighted input to the list of outputs
            activations.append(self.activationFunction(weightedInput))  
                  
        return activations
    