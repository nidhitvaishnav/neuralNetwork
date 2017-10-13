from neuralNetwork import NeuralNetwork


# test forward propagation

row = [1, 0, None]
neuralNetwork = NeuralNetwork(nInputs=1,nHiddenLayers=1,nNeurons=1,nOutputs=2)
neuralNetwork.networkDict = {'hiddenLayer0':{'output': [],\
        'weight': [[0.13436424411240122, 0.8474337369372327, 0.763774618976614]],\
        'delta': []},
        'outputLayer':{'output': [],\
        'weight': [[0.2550690257394217, 0.49543508709194095],\
                   [0.4494910647887381, 0.651592972722763]],\
        'delta': []}}


output = neuralNetwork.forwardPropagation(row)
print(output)