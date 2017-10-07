import sys
from myIO import MyIO
from dataPreprocess import DataPreprocess

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
            2. scaling data if required
            3. converting categorical / nominal values into numerical values,
        3. writing data to the csv file and returning refined dataframe
        """
        #reading csv from url in dataframe
        myIO = MyIO()
        inputDataFrame = myIO.inputCSVFromURL(filePath = inputFilePath)

        #debug
        print ('inputDataFrame = {} '.format(inputDataFrame))
        #debug -ends
        dataProcess = DataPreprocess()
        #creating dummy headers and adding them to dataframe
        headerList = dataProcess.provideHeaders(inputDataFrame =inputDataFrame)
        inputDataFrame.columns = headerList

        #removing null values
        nullRemovedDataFrame = dataProcess.removeNullValues(inputDataFrame = \
                                                            inputDataFrame)
        
        #scaling integer and float values
        scaledDataFrame = dataProcess.scaleData(inputDataFrame =\
                                                         nullRemovedDataFrame)
        #converting catgorical values into integer values
        refinedDataFrame = dataProcess.categoricalToNumericalConversion(\
                                            dataFrame = scaledDataFrame)
        #debug
        print ('refinedDataFrame =\n {} '.format(refinedDataFrame))
        #debug -ends
        
        #writing refined csv file
        myIO.writeCSV(inputDataFrame = refinedDataFrame, outputFilePath = \
                                                                 outputFilePath)
        return refinedDataFrame
#|------------------------dataProcessing -ends----------------------------------|    




if __name__ == '__main__':
    '''
    given function can read input and output path from command line arguements,
    (if it is not given than it will take default dataset iris),
    refine the dataset and 
    write it into outputFile path (default: ../dataset/processedTrDataset.csv)
    '''
    if len(sys.argv)>1:
        inputFilePath = sys.argv[1]
        outputFilePath = sys.argv[2]
    else:
        inputFilePath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#         inputFilePath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
#         inputFilePath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
#         inputFilePath = '../dataset/trDataset.csv'
        outputFilePath = '../dataset/processedTrDataset.csv'
    #if len(sys.argv) -ends
    
    #refining data which has read from uci repository
    dataProcessingUI = DataProcessingUI()
    refinedDataFrame = dataProcessingUI.dataProcessing(inputFilePath = inputFilePath,\
                                     outputFilePath = outputFilePath)