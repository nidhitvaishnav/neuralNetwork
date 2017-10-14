import numpy as np
import random
import copy

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
        #for outputCounter -ends
    
#|------------------------__init__ -ends---------------------------------------|    
#|-----------------------------------------------------------------------------|
# forwardPropagation
#|-----------------------------------------------------------------------------|
    def forwardPropagation(self, inputRow, iterationCount, rowCount):
        """
        performing forward propagation
        1. for each neurons, finding w*x 
        2. finding sigmoid function
        3. passing this result of sigmoid function to all other neurons as input
        """
        inputs = copy.deepcopy(inputRow)
        for currentLayer in sorted(self.networkDict.keys()):
            newInputs = []
            for neuronIndex, myNeuron in enumerate(self.networkDict[currentLayer]['weight']):
                activationVal = self._activateNeuron(myNeuron, inputs)
                sigmoidActVal = self._sigmoidActivation(activationVal)
                if (iterationCount==0 and rowCount==0):
                    self.networkDict[currentLayer]['output'].append(sigmoidActVal)
                else:
                    self.networkDict[currentLayer]['output'][neuronIndex]=\
                                                                sigmoidActVal
                #if -ends
                newInputs.append(sigmoidActVal)
            #for myNeuron -ends
            inputs = copy.deepcopy(newInputs)
        #for currentLayer -ends
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
        activationOutput = neuronWeight[-1]
        #adding W*X
        for myIndex in range(len(neuronWeight)-1):
            activationOutput+=neuronWeight[myIndex]*inputRow[myIndex]
        #for myIndex -ends
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
    def findBackwardPropagationError(self, targetValue, iterationCount, rowCount):
        """
        given function performs back propagation and finds/updates delta
        1. 
        """
        #performing for each layer
        for layerIndex in sorted(range(len(self.networkDict.keys())), reverse=True):
            errorList = []
            #if it is output layer, than compare output with target itself
            #else compare it with next layer values
            if (layerIndex==len(self.networkDict.keys())-1):
                for neuronIndex, neuronOutput in \
                            enumerate(self.networkDict['outputLayer']['output']):
                    errorList.append(targetValue[neuronIndex]-neuronOutput)
                #for neuronIndex -ends
            else:
                for neuronIndex in range(len(\
                        self.networkDict['hiddenLayer'+str(layerIndex)]['weight'])):
                    error=0.0
                    if (layerIndex != (len(self.networkDict.keys())-2)):
                        for nextLayerNeuronWeight in self.networkDict['hiddenLayer'\
                                                +str(layerIndex+1)]['weight']:
                            error+=float(nextLayerNeuronWeight[neuronIndex])\
                                    *float(self.networkDict['hiddenLayer'\
                                    +str(layerIndex+1)]['delta'][neuronIndex])
                            errorList.append(error)
                        #for nextNeuronIndex -ends
                    else:
                        for nextLayerNeuronWeight in \
                                    self.networkDict['outputLayer']['weight']:
                            error+=float(nextLayerNeuronWeight[neuronIndex])*\
                                    float(self.networkDict['outputLayer']['delta'][neuronIndex])
                            errorList.append(error)
                        #for nextNeuronIndex -ends
                    #if layerIndex -ends
                #for neuronIndex -ends                
            #if layerIndex -ends
            #asigning delta based on error value
            if (layerIndex!=len(self.networkDict.keys())-1):
                for neuronIndex in range(len(self.networkDict['hiddenLayer'+\
                                                    str(layerIndex)]['output'])):
                    if (iterationCount==0 and rowCount==0):
                        self.networkDict['hiddenLayer'+str(layerIndex)]['delta'].\
                                                    append(errorList[neuronIndex]\
                            *self._transferDerivative(self.networkDict[\
                                        'hiddenLayer'+str(layerIndex)]['output'\
                                                                ][neuronIndex]))
                    else:
                        self.networkDict['hiddenLayer'+str(layerIndex)]['delta']\
                                            [neuronIndex] =errorList[neuronIndex]\
                            *self._transferDerivative(self.networkDict[\
                            'hiddenLayer'+str(layerIndex)]['output'][neuronIndex])
                #for neuralIndex -ends
            else:
                for neuronIndex, neuronOutput in enumerate(self.networkDict[\
                                                    'outputLayer']['output']):
                    if (iterationCount==0 and rowCount==0):
                        self.networkDict['outputLayer']['delta'].append(\
                                    errorList[neuronIndex]*self._transferDerivative(\
                                    neuronOutput))
                    else:
                        self.networkDict['outputLayer']['delta'][neuronIndex] \
                            = errorList[neuronIndex]*self._transferDerivative(neuronOutput)
                #for neuralIndex -ends
            #if layerIndex -ends
        #for layerIndex -ends
        
#|------------------------findBackwardPropagationError -ends-------------------|    
#|-----------------------------------------------------------------------------|
# weightUpdate
#|-----------------------------------------------------------------------------|
    def weightUpdate(self, inputRow, learningRate):
        """
        This is to train network.
        newWeights = weight + learningRate * error * input
        """
        #for all layers, if they are not hidden layer, taking inputs from 
        #the output of the previous layer;
        #finding updated weights based on 
        #newWeight = LearningRate*neuronDelta*Inputs
        for layerIndex, layer in enumerate(sorted(self.networkDict.keys())):
            inputs = inputRow[:-1]
            if layer!='hiddenLayer0':
                inputs = [neuronOutput for neuronOutput in\
                     self.networkDict["hiddenLayer"+str(layerIndex-1)]['output']]
                #for neuronOutput -ends
            #if layer -ends
            for neuronIndex, neuronDelta in enumerate(self.networkDict[layer]['delta']):
                for atr in range(len(inputs)):
                    self.networkDict[layer]['weight'][neuronIndex][atr]+=\
                                            learningRate*neuronDelta*inputs[atr]
                #for atr -ends
                self.networkDict[layer]['weight'][neuronIndex][-1]+=\
                                                    learningRate*neuronDelta
            #for neuronIndex, euronDelta -ends
        #for layer -ends
#|------------------------weightUpdate -ends-----------------------------------|    
#|-----------------------------------------------------------------------------|
# trainNetwork
#|-----------------------------------------------------------------------------|
    def trainNetwork(self, trainingDataArr, nIteration, numOfUniqueClasses, learningRate=0.9):
        """
        given function creates a neural network after initialization
        """
        #for nIterations, we are training network on entire dataset
        for currentIteration in range(nIteration):
            trainingError=0
            for rowIndex, currentRow in enumerate(trainingDataArr):
                #performing forward propagation
                outputs = self.forwardPropagation(inputRow = currentRow,\
                                                iterationCount =currentIteration,\
                                                rowCount = rowIndex)
                #converting target (real output) in one hot output 
                targetOutput = [0 for i in range(numOfUniqueClasses)]
                targetOutput[int(currentRow[-1])] = 1
                #finding mean square error
                trainingError+=sum([(targetOutput[i]-outputs[i])**2/len(\
                                targetOutput) for i in range(len(targetOutput))])
                #performing back propagation
                self.findBackwardPropagationError(targetValue = targetOutput,\
                                                iterationCount =currentIteration,\
                                                rowCount = rowIndex)
                #updating weights
                self.weightUpdate(inputRow = currentRow, learningRate = learningRate)
            #for currentRow -ends
        #for currentIteration -ends
        return trainingError        
#|------------------------trainNetwork -ends-----------------------------------|
#|-----------------------------------------------------------------------------|
# predictDataset
#|-----------------------------------------------------------------------------|
    def predictDataset(self, testingDataSet):
        """
        given function predicts output of test dataset and returns output 
        data array
        """
        outputList = []
        predictErrorCount = 0
        #for all dataset, finding predicted outputs, which are in form of 
        #one hot output, and then converting them into actual outputs
        for rowIndex, currentRow in enumerate(testingDataSet):
            oneHotOutputs = self.forwardPropagation(inputRow = currentRow,\
                                         iterationCount =0, rowCount = rowIndex)
            rowOutput = oneHotOutputs.index(max(oneHotOutputs))
            outputList.append(rowOutput)
            #accuracy count
            if rowOutput != currentRow[-1]:
                predictErrorCount+=1    
            #if rowOutput -ends
        #for rowIndex, currentRow -ends
        outputArr = np.array(outputList)
        return outputArr        
#|------------------------predictDataset -ends---------------------------------| 
#|-----------------------------------------------------------------------------|
# meanSquareError
#|-----------------------------------------------------------------------------|
    def meanSquareError(self, targetArr, predictedOutputArr):
        """
        given function finds mean square error
        E(w) = 1/2*sigma(t-o)^2
        """
        return np.square(targetArr - predictedOutputArr).mean()   
#|------------------------meanSquareError -ends--------------------------------|   
#|-----------------------------------------------------------------------------|
# printNeuralNetworkWeights
#|-----------------------------------------------------------------------------|
    def printNeuralNetworkWeights(self, headerList):
        """
        print weights of neural network
        """
        #printing input layer
        print ('layer{} : {}'.format(0, "Input Layer"))
        for index in range(0, len(headerList)):
            print ('\t Neuron{} weights : {}'.format(index, 0))
        #for index -ends
        print ('\n')
        #printing hidden and output layers
        for layerIndex, layer in enumerate(sorted(self.networkDict.keys())):
            print ('layer{} : {}'.format(layerIndex+1, layer))
            for neuronIndex, neuronWeight in enumerate(self.networkDict[layer]['weight']):
                print ('\t Neuron{} weights : {}'.format(neuronIndex, neuronWeight))
            #for neuronIndex -ends
            print ('\n')
        #for layerIndex -ends
    
#|------------------------printNeuralNetworkWeights -ends----------------------|    
 
