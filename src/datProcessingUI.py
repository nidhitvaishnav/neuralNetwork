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
            3. cleansing the data set of any wrong values
            2. converting categorical / nominal values into numerical values,
            3. scaling data if required
        """
        
        myIO = MyIO()
        inputDataList = myIO.inputCSV(filePath = inputFilePath)
        #debug
        print ('inputDataList:\n')
        for data in inputDataList:
            print ("{}".format(data))
        #debug -ends
#         inputArr = np.array(inputDataList)
#         #debug
#         print ('inputArr = {} '.format(inputArr))
#         #debug -ends
        
        dataProcess = DataPreprocess()
        listWithoutNull = dataProcess.removeNullValues(inputDataList = \
                                                                inputDataList)
        
#|------------------------dataProcessing -ends----------------------------------|    





















if __name__ == '__main__':
    if len(sys.argv)>1:
        inputFilePath = sys.argv[1]
        outputFilePath = sys.argv[2]
    else:
        inputFilePath = '../dataset/trDataset.csv'
        outputFilePath = '../dataset/processedTrDataset.csv'
    #if len(sys.argv) -ends
    
    dataProcessingUI = DataProcessingUI()
    dataProcessingUI.dataProcessing(inputFilePath = inputFilePath,\
                                     outputFilePath = outputFilePath)