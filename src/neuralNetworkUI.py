import sys
from myIO import MyIO
from myUtility import MyUtility


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
            b. neuron transfer : sigmoid function
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
        myUtility.splitDataset(inputDataFrame = inputDataFrame,\
                                            trainingPercent = trainingPercent)
        
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
        nHiddenLayers = 1
        nNeurons = 3
    #if len(sys.argv) -ends
    
    neuralNetworkUI = NeuralNetworkUI()    
    neuralNetworkUI.createNeuralNetwork(inputFilePath = inputFilePath,\
                                        trainingPercent = trainingPercent,\
                                        maxItr = maxItr,\
                                        nHiddenLayers = nHiddenLayers,\
                                        nNeurons = nNeurons)    