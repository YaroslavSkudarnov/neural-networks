from Neuron import Neuron

class Layer:
    def __init__(self, input_neurons, output_neurons=1):
        self.__neurons = [Neuron(output_neurons) for _ in range(input_neurons)]

    def __getitem__(self, index):
        return self.__neurons[index]

    def __setitem__(self, index, value):
        self.__neurons[index] = value

    def update(self, index, value):
        self.__neuron[index].update(value)

    def output(self, input_vector):
        return sum(neuron.getOutput() * inp for neuron, inp in zip(self.__neurons, input_vector))

