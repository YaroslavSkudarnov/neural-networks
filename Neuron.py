class Neuron:
    def __init__(self, outputs_num=1):
        self.__outputs = [0.0] * outputs_num

    def __str__(self):
        return 'Outputs: {}'.format(self.__outputs)

    def output(self, index=0):
        return self.__outputs[index]

    def update(self, value, index=0):
        self.__outputs[index] += value
    
