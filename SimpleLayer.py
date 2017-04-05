from Neuron import Neuron

class SimpleLayer:
    def __init__(self, input_neurons, output_neurons=1):
        if isinstance(input_neurons, list):
            self.__neurons = input_neurons
        else:
            self.__neurons = [Neuron(output_neurons) for _ in range(input_neurons)]

    def __getitem__(self, index):
        return self.__neurons[index]

    def __setitem__(self, index, value):
        self.__neurons[index] = value

    def __str__(self):
        result = 'Neurons:\n'
        for neuron in self.__neurons:
            result += str(neuron) + '\n'
        return result

    def update(self, index, value):
        self.__neurons[index].update(value)

    def output(self, input_vector):
        return sum(neuron.output() * inp for neuron, inp in zip(self.__neurons, input_vector))

