from BiasedLayer import BiasedLayer
from Neuron import Neuron

class SimplePerceptron:
    def __init__(self, input_neurons):
        self.__input_layer = BiasedLayer(input_neurons)

    def __train_step_single_vector(self, input_vector, output, multiplier):
        delta = output - self.output(input_vector)
        self.__input_layer = BiasedLayer([neuron.update( multiplier * delta * inp) for neuron, inp in zip(self.__input_layer, input_vector)])

    def __train_step(self, input_vectors, outputs):
        multiplier = self.__start_multiplier
        for input_vector, output in zip(input_vectors, outputs):
            self.__train_step_single_vector(input_vector, output, multiplier)
            multiplier *= self.__fade_multiplier
        
    def train(self, input_vectors, outputs, start_multiplier=0.05, fade_multiplier=1, steps=100):
        self.__start_multiplier = start_multiplier
        self.__fade_multiplier = fade_multiplier

        for i in range(steps):
            self.__train_step(input_vectors, outputs)

    def output(self, input_vector):
        return self.__input_layer.output(input_vector)
       
