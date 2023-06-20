import numpy as np
from random import random
class neuron():
    def __init__(self, amountOfWeights, bias):
        self.weights = []
        for i in range(amountOfWeights):
            self.weights.append(random())
        print(self.weights)
        self.bias = bias

    def run(self, inp):
        matrix1 = np.array(inp[i])
        matrix2 = np.array(self.weights[i])
        matrixMultiplied = np.dot(matrix1, matrix2)
        calc = self.sigmoid(np.sum(matrixMultiplied)+self.bias)
        return calc

    def set_weights(self, weights):
        self.weights = weights

    def get_weights(self):
        return self.weights
    def sigmoid(self,v):
        return 1/(1+np.exp(-v))
