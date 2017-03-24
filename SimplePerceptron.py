import Layer
import Neuron

class SimplePerceptron:
    def __init__(self, input_neurons, start_multiplier=1, fade_multiplier=0.95, steps=100):
        self.__input_layer = Layer(input_neurons + 1)
        self.__start_multiplier = start_multiplier
        self.__fade_multiplier = fade_multiplier
        self.__steps = steps

    def __train_step_single_vec_tor(self, input_vector, output, multiplier):
        delta = output - self.output(input_vector)
        self.__input_layer = [neuron.update(0, multiplier * delta * inp) for neuron, inp in zip(self.__input_layer, input_vector)])]

    def __train_step(self, input_vectors, outputs):
        multiplier = self.__start_multiplier
        for input_vector, output in input_vectors, outputs:
            self.__train_step_single_vec(input_vector, output, multiplier)
            multiplier *= self.__fade_multiplier
        
    def train(self, input_vectors, outputs):
        for _ in range(self.__steps):
            self.__train_step(input_vecs, outputs)

    def output(self, input_vector):
        return sum(x * y for neuron, inp in zip(self.__input_layer, input_vector))
       
