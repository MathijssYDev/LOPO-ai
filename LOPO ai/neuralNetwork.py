import numpy as np
from neuron import neuron


class neuralNetwork():
    def __init__(self, layers, biases):

        self.layers = layers
        self.neurons = []
        for i in range(len(layers)):
            if i == 0:
                continue
            self.neurons.append([])
            for x in range(layers[i]):
                self.neurons[i-1].append(neuron(layers[i-1], 6))

    def run(self, trainData, inputImage):
        for i in range(len(self.neurons)):
            for x in range(len(self.neurons[i])):
                self.neurons[i][x].get_weights()

    def set_weights(self, weights):
        self.layersWeights = weights

    def get_weights(self):
        return self.layersWeights


nw = neuralNetwork([pow(32, 2), pow(4, 2), 10], [6, 6])
nw.run(1,1)

# class neuralNetwork():
# def __init__(self, layers, biases):
#     # biases example: [[6,6],6] -> every bias is 6
#     # layers example: [64,[16,16],10] -> 64 input neurons, 2 layers of 16 neurons and 10 output neurons
#     self.layers = layers
#     self.Weights = []
#     for i, v in enumerate(layers):
#         if i == 0:
#             continue
#         self.Weights.append([])
#         for x in range(v):
#             self.Weights[i-1].append(0)
#     self.WeightsStruct = self.Weights.copy()

# def run(self, trainData, inputImage):
#     layersWeightsNew = self.WeightsStruct.copy()
#     layersWeightsNew.insert(0, inputImage)
#     for i in range(len(layersWeightsNew)-1):
#         matrix1 = np.array(layersWeightsNew[i])
#         matrix2 = np.array(self.Weights[i])

#         matrixMultiplied = np.dot(matrix1, matrix2)
#         calc = np.sum(matrixMultiplied)
#         layersWeightsNew[i] = calc
#         print(calc)

# def set_weights(self, weights):
#     self.layersWeights = weights

# def get_weights(self):
#     return self.layersWeights
