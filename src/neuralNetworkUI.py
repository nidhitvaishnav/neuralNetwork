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
        """
        #0. read dataset
        myIO = MyIO()
        inputDataFrame = myIO.inputProcessedCSV(filePath = inputFilePath)
        headerList = inputDataFrame.columns.values
        #debug
        print ('inputDataFrame =\n {} '.format(inputDataFrame))
        print ('headerList =\n {}'.format(headerList))
        #debug -ends 
        
        #1. split dataset into training and testing dataset\
        myUtility = MyUtility()
        trainingDataFrame, testingDataFrame = myUtility.splitDataset(\
                                            inputDataFrame = inputDataFrame,\
                                            trainingPercent = trainingPercent)
        
        #2. initializeNeuralNetwork
        uniqueClasses = inputDataFrame['class'].unique()
        numOfUniqueClasses = uniqueClasses.size
        
        #debug
        print ('numOfUniqueClasses = {} '.format(numOfUniqueClasses))
        #debug -ends
        
        trainingDataArr = trainingDataFrame.values
        testingDataArr = testingDataFrame.values
        
#         trainingAtrArr, trainingClassArr, trainingAtrHeader = myUtility.segregateAttributesAndClass(inputArr = trainingDataArr, inputHeader = headerList)
#         testingAtrArr, testingClassArr, testingAtrHeader = myUtility.segregateAttributesAndClass(inputArr = testingDataArr, inputHeader = headerList)
#         
#         #debug
#         print ('trainingAtrArr = {} '.format(trainingAtrArr.shape))
#         print("trainingClassArr = {}".format(trainingClassArr.shape))
#         print ('testingAtrArr = {} '.format(testingAtrArr.shape))
#         print("testingClassArr = {}".format(testingClassArr.shape))
#         #debug -ends
        
        nRows, nCols = trainingDataArr.shape
        
        neuralNetwork = NeuralNetwork( nInputs = nCols-1,\
                                       nHiddenLayers = nHiddenLayers, \
                                       nNeurons = nNeurons, \
                                       nOutputs = numOfUniqueClasses)
        
#         #debug
#         print ('networkDict =\n {} '.format(neuralNetwork.networkDict))
# #         print ('outputWeightDict =\n {} '.format(neuralNetwork.outputWeightDict))
#         #debug -ends
#         
#         #3. forword propogation
#         outputs = neuralNetwork.forwardPropagation(inputRow = trainingDataArr[0])
#         #debug
#         print ('=========================================================')
#         print ('outputs = {} '.format(outputs))
#         print ('=========================================================')
#         #debug -ends

        #4. back propogation
#         neuralNetwork.findBackwardPropagationError(targetValue = [1,0,0])
        neuralNetwork.trainNetwork(trainingDataArr = trainingDataArr, nIteration = 1000, numOfUniqueClasses=3, learningRate=0.9)
        predictedOutputList, predictionError = neuralNetwork.predictDataset(testingDataSet = testingDataArr)
        #debug
        print ('predictionError = {} '.format(predictionError))
        #debug -ends
#|------------------------createNeuralNetwork -ends----------------------------|    

















if __name__ == '__main__':
    if len(sys.argv)>1:
        inputFilePath = sys.argv[1]
        trainingPercent = sys.argv[2]
        maxItr = sys.argv[3]
        nHiddenLayers = sys.argv[4]
        nNeurons = sys.argv[5]
    else:
        inputFilePath = '../dataset/processedTrDataset.csv'
        trainingPercent = 80
        maxItr = 200
        nHiddenLayers = 2
        nNeurons = 2
    #if len(sys.argv) -ends
    
    neuralNetworkUI = NeuralNetworkUI()    
    neuralNetworkUI.createNeuralNetwork(inputFilePath = inputFilePath,\
                                        trainingPercent = trainingPercent,\
                                        maxItr = maxItr,\
                                        nHiddenLayers = nHiddenLayers,\
                                        nNeurons = nNeurons)    