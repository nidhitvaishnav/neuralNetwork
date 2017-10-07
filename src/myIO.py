import pandas as pd

class MyIO:
    """
    This class performs input - output tasks.
    """

#|-----------------------------------------------------------------------------|
# inputCSV
#|-----------------------------------------------------------------------------|
    def inputCSVFromURL(self, filePath):
        """
        given method takes csv file path as an input; reads csv file and
        return data in the form of pandas dataframe
        """
#         inputObj = pd.read_csv(filepath_or_buffer  = filePath, header = None,\
#                                                          delimiter = '\t')
        inputDataFrame = pd.read_csv(filepath_or_buffer = filePath, header = None,\
                                        na_values = "?", skipinitialspace = True)        
#         inputHeader = inputObj.columns.tolist()
        
#         inputDataList = inputDataFrame.tolist()   
        return inputDataFrame
#|------------------------inputCSV -ends---------------------------------------|
#|-----------------------------------------------------------------------------|
# writeCSV
#|-----------------------------------------------------------------------------|
    def writeCSV(self, inputDataFrame, outputFilePath):
        """
        given function uses pandas library as input and write csv file with 
        default delimeter ','
        """
        inputDataFrame.to_csv(outputFilePath, index = False)
#|------------------------writeCSV -ends----------------------------------|    
