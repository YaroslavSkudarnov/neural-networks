from SimpleLayer import SimpleLayer

class BiasedLayer(SimpleLayer):
    def __init__(self, input_neurons, output_neurons=1):
        if isinstance(input_neurons, list):
            super().__init__(input_neurons)
        else:
            super().__init__(input_neurons + 1, output_neurons)
        

    def output(self, input_vector):
        return super().output(input_vector + [1.0])
