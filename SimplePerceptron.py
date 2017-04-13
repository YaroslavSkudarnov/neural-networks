from BiasedLayer import BiasedLayer
from Neuron import Neuron
import logging, random

class SimplePerceptron:
    def __init__(self, input_neurons):
        self.__input_layer = BiasedLayer(input_neurons)

    def __train_step_single_vector(self, input_vector, output, multiplier):
        delta = output - self.output(input_vector)
        logging.info(input_vector)
        logging.info('Output before: {}'.format(self.output(input_vector)))
        self.__input_layer = BiasedLayer([neuron.update(self.__multiplier * delta * inp) for neuron, inp in zip(self.__input_layer, input_vector + [1.0])])
        logging.info(', '.join(str(x) for x in self.__input_layer._SimpleLayer__neurons))
        logging.info('Output after: {}'.format(self.output(input_vector)))

    def __train_step(self, input_vectors, outputs):
        inputs_and_outputs = list(zip(input_vectors, outputs))
        random.shuffle(inputs_and_outputs)
        logging.info(inputs_and_outputs)

        for input_vector, output in inputs_and_outputs:
            self.__train_step_single_vector(input_vector, output, self.__multiplier)
        
    def train(self, input_vectors, outputs, start_multiplier=0.5, fade_multiplier=0.95, steps=100, reuse_multiplier=False):
        if not reuse_multiplier:
            self.__multiplier = start_multiplier
        for i in range(steps):
            self.__train_step(input_vectors, outputs)
            self.__multiplier *= fade_multiplier

    def output(self, input_vector):
        return self.__input_layer.output(input_vector)
       
