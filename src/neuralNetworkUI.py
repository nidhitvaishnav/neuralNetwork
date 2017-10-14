import sys
from myIO import MyIO
from myUtility import MyUtility
from neuralNetwork import NeuralNetwork


class NeuralNetworkUI:
    
#|-----------------------------------------------------------------------------|
# createNeuralNetwork
#|-----------------------------------------------------------------------------|
    def createNeuralNetwork(self, inputFilePath, trainingPercent, maxItr,
                                                    nHiddenLayers, nNeurons):
        """
        given function creates neural network, 
        and displays its waight at each level and accuracy of the network
        0. read dataset
        1. split dataset into training and testing datasets
        2. initialize network
            a. take weights randomly for hidden and output layers
        3. forward propogation
            a. neuron activation: sigma(wi*xi)
            b. neuron transfer : sigmoid function 1/(1+e(-x))
        4. back propogation
            a. transfer derivative
            b. error back propogation
        5. train network
            a. update weights
        6. predict
        7. find mean square errors
        """
        #0. read dataset
        myIO = MyIO()
        inputDataFrame = myIO.inputProcessedCSV(filePath = inputFilePath)
        headerList = inputDataFrame.columns.values
        
        #1. split dataset into training and testing dataset\
        myUtility = MyUtility()
        trainingDataFrame, testingDataFrame = myUtility.splitDataset(\
                                            inputDataFrame = inputDataFrame,\
                                            trainingPercent = trainingPercent)
        
        #2. initializeNeuralNetwork
        uniqueClasses = inputDataFrame['class'].unique()
        numOfUniqueClasses = uniqueClasses.size
        
        trainingDataArr = trainingDataFrame.values
        testingDataArr = testingDataFrame.values
        
        trainingAtrArr, trainingClassArr, trainingAtrHeader = \
                                    myUtility.segregateAttributesAndClass(\
                                                inputArr = trainingDataArr,\
                                                inputHeader = headerList)
        testingAtrArr, testingClassArr, testingAtrHeader =\
                                 myUtility.segregateAttributesAndClass(\
                                                    inputArr = testingDataArr,\
                                                    inputHeader = headerList)

        
        nRows, nCols = trainingDataArr.shape
        
        neuralNetwork = NeuralNetwork( nInputs = nCols-1,\
                                       nHiddenLayers = nHiddenLayers, \
                                       nNeurons = nNeurons, \
                                       nOutputs = numOfUniqueClasses)
        

        #4. back propogation
#         neuralNetwork.findBackwardPropagationError(targetValue = [1,0,0])
        trainingError = neuralNetwork.trainNetwork(\
                                            trainingDataArr = trainingDataArr,\
                                            nIteration = maxItr,\
                                            numOfUniqueClasses=numOfUniqueClasses, \
                                            learningRate=0.5)
        trainingPredictedOPArr = neuralNetwork.predictDataset(\
                                            testingDataSet = trainingDataArr)
        testingPredictedOPArr = neuralNetwork.predictDataset(\
                                            testingDataSet = testingDataArr)
        
        trainingError =  neuralNetwork.meanSquareError(\
                                    targetArr = trainingClassArr,\
                                    predictedOutputArr = trainingPredictedOPArr)
        testingError = neuralNetwork.meanSquareError(\
                                    targetArr = testingClassArr,\
                                     predictedOutputArr = testingPredictedOPArr)
        
        #debug
        print ("\nAfter training neural network:\n")
        neuralNetwork.printNeuralNetworkWeights(headerList = trainingAtrHeader)
        print ('\ntrainingError = {}'.format(trainingError))
        print ('testingError = {} '.format(testingError))
        #debug -ends
#|------------------------createNeuralNetwork -ends----------------------------|    






if __name__ == '__main__':
    if len(sys.argv)>1:
        inputFilePath = str(sys.argv[1])
        trainingPercent = float(sys.argv[2])
        maxItr = int(sys.argv[3])
        nHiddenLayers = int(sys.argv[4])
        nNeurons = int(sys.argv[5])
    else:
        inputFilePath = '../dataset/processedTrDataset.csv'
        trainingPercent = 80
        maxItr = 10
        nHiddenLayers = 2
        nNeurons = 2
    #if len(sys.argv) -ends
    
    neuralNetworkUI = NeuralNetworkUI()    
    neuralNetworkUI.createNeuralNetwork(inputFilePath = inputFilePath,\
                                        trainingPercent = trainingPercent,\
                                        maxItr = maxItr,\
                                        nHiddenLayers = nHiddenLayers,\
                                        nNeurons = nNeurons)    