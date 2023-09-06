import numpy as np

class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # TODO (Implement FCNNs architecture here)
        self.layer_size = layer_sizes

        self.weight1 = np.random.normal(size=(layer_sizes[1],layer_sizes[0]))
        self.weight2 = np.random.normal(size=(layer_sizes[2],layer_sizes[1]))
        self.weight3 = np.random.normal(size=(layer_sizes[3],layer_sizes[2]))
        self.weight4 = np.random.normal(size=(layer_sizes[4],layer_sizes[3]))

        self.bias1 = np.ones((layer_sizes[1], 1))
        self.bias2 = np.ones((layer_sizes[2], 1))
        self.bias3 = np.ones((layer_sizes[3], 1))
        self.bias4 = np.ones((layer_sizes[4], 1))


    def activation(self, x):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        # TODO (Implement activation function here)
        sigmoid = 1 / (1 + np.exp(-x))
        return sigmoid

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # TODO (Implement forward function here)
        sig1 = self.activation(self.weight1 @ x + self.bias1)
        sig2 = self.activation(self.weight2 @ sig1 + self.bias2)
        sig3 = self.activation(self.weight3 @ sig2 + self.bias3)
        sig4 = self.activation(self.weight4 @ sig3 + self.bias4)
        return sig4