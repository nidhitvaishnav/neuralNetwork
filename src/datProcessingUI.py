import sys
from myIO import MyIO
from dataPreprocess import DataPreprocess
import numpy as np

class DataProcessingUI:
    
#|-----------------------------------------------------------------------------|
# dataProcessing
#|-----------------------------------------------------------------------------|
    def dataProcessing(self, inputFilePath, outputFilePath):
        """
        1. given function reads csv file,
           Note: data from https://archive.ics.uci.edu/ml/datasets does not 
                 provide headers, so we are providing our own headers
        2. pre-process it by 
            1. removing null values,
            2. converting categorical / nominal values into numerical values,
            3. scaling data if required
        """
        
        myIO = MyIO()
        inputDataFrame = myIO.inputCSV(filePath = inputFilePath)

        #debug
        print ('inputDataFrame = {} '.format(inputDataFrame))
        #debug -ends
        dataProcess = DataPreprocess()
        headerList = dataProcess.provideHeaders(inputDataFrame =inputDataFrame)
        #debug
        print ('headerList = {} '.format(headerList))
        #debug -ends
        inputDataFrame.columns = headerList
        #debug
        print ('---------------------')
        print ('inputArr = \n{} '.format(inputDataFrame.head(10)))
        print ('---------------------')
        #debug -ends
        nullRemovedDataFrame = dataProcess.removeNullValues(inputDataFrame = \
                                                            inputDataFrame)
        #debug
        print ('nullRemovedDataFrame.head(10) = {} '.format(nullRemovedDataFrame.head(10)))
        #debug -ends
        refinedDataFrame = dataProcess.categoricalToNumericalConversion(\
                                            rawDataFrame = nullRemovedDataFrame)
        
#|------------------------dataProcessing -ends----------------------------------|    
















if __name__ == '__main__':
    if len(sys.argv)>1:
        inputFilePath = sys.argv[1]
        outputFilePath = sys.argv[2]
    else:
#         inputFilePath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
#         inputFilePath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        inputFilePath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
        outputFilePath = '../dataset/processedTrDataset.csv'
    #if len(sys.argv) -ends
    
    dataProcessingUI = DataProcessingUI()
    dataProcessingUI.dataProcessing(inputFilePath = inputFilePath,\
                                     outputFilePath = outputFilePath)