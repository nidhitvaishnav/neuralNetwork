import numpy as np
import random
from collections import defaultdict

class NeuralNetwork:        
#|-----------------------------------------------------------------------------|
# __init__
#|-----------------------------------------------------------------------------|
    def __init__(self, nInputs, nHiddenLayers, nNeurons, nOutputs):
        """
        initializing neural network
        Input to the neyralNetwork:
        nInputs : number of neurons at input layer (int)
        nHiddenLayers : number of hidden layers (int)
        nNeuronsAtEachLayer : here we are assuming that each hidden layer has 
        same number of neurons, so we take number of neurons in each layer (int)
        nOutputs : number of neurons at output layer 
        """
        #initializing input parameters
        self.nInputs = nInputs
        self.nHiddenLayers = nHiddenLayers
        self.nNeurons = nNeurons
        self.nOutputs = nOutputs 
    
        #initializing parameters based on given parameters
        layerNames = []
        for i in range(self.nHiddenLayers):
            layerNames.append("hiddenLayer"+str(i))
        #for i ends
        layerNames.append("outputLayer")
        keys=["weight", "output", "delta"]
        self.networkDict={ name:{ key:[] for key in keys}\
                                             for name in layerNames}
        print ('networkDict = {} '.format(self.networkDict))
        
#         self.networkDict = defaultdict(list)
#         self.outputWeightDict = defaultdict(list)
         
        prevLayerNeuronCount = self.nInputs
        for hiddenlayer in range(self.nHiddenLayers):
            for neuron in range(self.nNeurons):
                weightList=[]
                #finding weight for nNeurons + 1 bias
                for inputCounter in range(prevLayerNeuronCount+1):
                    weightx=random.uniform(0,1)
                    weightList.append(weightx)
                #for inputCounter -ends
                self.networkDict["hiddenLayer"+str(hiddenlayer)]['weight'].\
                                                            append(weightList)
            #for neuron -ends
            prevLayerNeuronCount = self.nNeurons
        #for hiddenLayer -ends
                
        for outputCounter in range(self.nOutputs):
            weightList = []
            #finding weight for nNeurons + 1 bias
            for neuron in range(self.nNeurons+1):
                weightx=random.uniform(0,1)
                weightList.append(weightx)
            #for neuron -ends
            self.networkDict["outputLayer"]["weight"].append(weightList)
#             self.outputWeightDict['weight'].append(weightList)             
        #for outputCounter -ends
    
#|------------------------__init__ -ends---------------------------------------|    
#|-----------------------------------------------------------------------------|
# forwardPropagation
#|-----------------------------------------------------------------------------|
    def forwardPropagation(self, inputRow):
        """
        performing forward propagation
        1. for each neurons, finding w*x 
        2. finding sigmoid function
        3. passing this result of sigmoid function to all other neurons as input
        """
        modifiedInputs = []
        for currentLayer in sorted(self.networkDict.keys()):
            inputs = inputRow
            newInputs = []
            #debug
            print ('currentLayer = {} '.format(currentLayer))
            #debug -ends
 
            for myNeuron in self.networkDict[currentLayer]['weight']:
                #debug
                print ('myNeuron = {} '.format(myNeuron))
                #debug -ends
                activationVal = self._activateNeuron(myNeuron, inputs)
                self.networkDict[currentLayer]['output']=\
                                        self._sigmoidActivation(activationVal)
                newInputs.append(self.networkDict[currentLayer]['output'])
            #for myNeuron -ends
            inputs = newInputs
        #for currentLayer -ends
#         #debug
#         print ('self.networkDict = {} '.format(self.networkDict))
#         #debug -ends
        return inputs
#|------------------------forwardPropagation -ends-----------------------------|          
#|-----------------------------------------------------------------------------|
# __activateNeuron
#|-----------------------------------------------------------------------------|
    def _activateNeuron(self, neuronWeight, inputRow):
        """
        performing W*X 
        where W=[w0, w1,..., wn] is a weight vector (w0 is bias)
        X=[x1, x2,...,xn] is an input vector
        output is an activation output of float type 
        """
        #adding bias value 
        activationOutput = neuronWeight[0]
        #adding W*X
        for myIndex in range(len(neuronWeight)-1):
            activationOutput+=neuronWeight[myIndex]*inputRow[myIndex]
        #for myIndex -ends
        #debug
        print ('activationOutput = {} '.format(activationOutput))
        #debug -ends
        return activationOutput

#|------------------------__activateNeuron -ends-------------------------------|    
#|-----------------------------------------------------------------------------|
# _sigmoidActivation
#|-----------------------------------------------------------------------------|
    def _sigmoidActivation(self, activationVal):
        """
        performing sigmoid function 1/(1+e(-x))
        """
        return 1.0 / (1.0 + np.exp(-activationVal)) 
#|------------------------_sigmoidActivation -ends-----------------------------|    
#|-----------------------------------------------------------------------------|
# _transferDerivative
#|-----------------------------------------------------------------------------|
    def _transferDerivative(self, value):
        """
        to find derivative of output(slope) using sigmoid transfer function
        x*(1-x), which returns float value
        """
        return value*(1-value)    
#|------------------------_transferDerivative -ends----------------------------|  
#|-----------------------------------------------------------------------------|
# findBackwardPropagationError
#|-----------------------------------------------------------------------------|
    def findBackwardPropagationError(self, targetValue):
        """
        
        """
        #performing for each layer
        for layerIndex in sorted(range(len(self.networkDict.keys())), reverse=True):
            errorList = []
            #if it is output layer, than compare output with target itself
            #else compare it with next layer values
            if (layerIndex==len(self.networkDict.keys())-1):
                for neuronIndex in range(len(self.networkDict['outputLayer']['weight'])):
#                     #debug
#                     print ('neuron weight= {} '.format(self.networkDict['outputLayer']['weight']))
#                     print ('neuron output= {} '.format(self.networkDict['outputLayer']['output']))
                    print ('index = 2, outputLayer')
                    #debug -ends
                    errorList.append(targetValue[neuronIndex]-\
                                    self.networkDict['outputLayer']['output'])
                #for neuronIndex -ends

            else:
                #debug
                print ('### layerIndex = {}### '.format(layerIndex))
                #debug -ends
                for neuronIndex in range(len(self.networkDict['hiddenLayer'+str(layerIndex)]['weight'])):
                    error=0.0
                    print('+++++++++')
                    if (layerIndex != (len(self.networkDict.keys())-2)):
                        #debug
                        print ('total keys: {}'.format(self.networkDict.keys()))
                        print ('layerIndex = {} '.format(layerIndex))
                        #debug -ends
                        for nextLayerNeuron in self.networkDict['hiddenLayer'+str(layerIndex+1)]['weight']:
                            #debug
                            print ('nextLayerNeuron = {} '.format(nextLayerNeuron))
                            print("{}".format(self.networkDict['hiddenLayer'+str(layerIndex+1)]['delta']))
                            #debug -ends
                            #TODO: check for the multiplication between list and float
                            error+=nextLayerNeuron*float(self.networkDict['hiddenLayer'+str(layerIndex+1)]['delta'])
                            errorList.append(error)
                        #for nextNeuronIndex -ends
                    else:
                        for nextLayerNeuron in self.networkDict['outputLayer']['weight']:
                            #debug
                            print ('delta= {} '.format(self.networkDict['outputLayer']['delta']))
                            #debug -ends
                            error+=nextLayerNeuron*float(self.networkDict['outputLayer']['delta'])
                            errorList.append(error)
                        #for nextNeuronIndex -ends
                    #if layerIndex -ends
                #for neuronIndex -ends                
            #if layerIndex -ends
            #asigning delta based on error value
            if (layerIndex!=len(self.networkDict.keys())-1):
                for neuronIndex in range(len(self.networkDict['hiddenLayer'+str(layerIndex)])):
                    self.networkDict['hiddenLayer'+str(layerIndex)]['delta']\
                            =errorList[neuronIndex]\
                            *self._transferDerivative(self.networkDict[\
                                        'hiddenLayer'+str(layerIndex)]['output'])
                #for neuralIndex -ends
            else:
                for neuronIndex in range(len(self.networkDict['outputLayer'])):
                    self.networkDict['outputLayer']['delta']\
                            =errorList[neuronIndex]*self._transferDerivative(\
                                    self.networkDict['outputLayer']['output'])
                #for neuralIndex -ends
            #if layerIndex -ends
        #for layerIndex -ends
        
#|------------------------findBackwardPropagationError -ends----------------------------------|    