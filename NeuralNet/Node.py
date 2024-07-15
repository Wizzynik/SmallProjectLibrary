class Node:
    # Arguments
    bias = 0
    weights = []
    
    # Constructor
    def __init__(self, bias, weights):
        self.bias = bias
        self.weights = weights
                
    # Methods
    def cal_output(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        return sum + self.bias
        