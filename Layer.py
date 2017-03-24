import Neuron

class Layer:
    def __init__(self, input_neurons):
        self.__neurons = [Neuron(1) for _ in range(input_neurons)]

    def __init__(self, input_neurons, output_neurons):
        self.__neurons = [Neuron(output_neurons) for _ in range(input_neurons)]

    def output(self, input_vector):
        return sum(neuron_output_weight * inp for neuron_output_weight, inp in zip(self.__neurons, input_vector))

