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

        inputDataFrame = pd.read_csv(filepath_or_buffer = filePath, header = None,\
                                        na_values = "?", skipinitialspace = True)        
   
        return inputDataFrame
#|------------------------inputCSV -ends---------------------------------------|
#|-----------------------------------------------------------------------------|
# inputProcessedCSV
#|-----------------------------------------------------------------------------|
    def inputProcessedCSV(self, filePath):
        """
        given function reads csv file and returns data in the form of pandas 
        data frame
        """
        inputDataframe  = pd.read_csv(filepath_or_buffer = filePath)
        return inputDataframe
    
#|------------------------inputProcessedCSV -ends----------------------------------|    
#|-----------------------------------------------------------------------------|
# writeCSV
#|-----------------------------------------------------------------------------|
    def writeCSV(self, inputDataFrame, outputFilePath):
        """
        given function uses pandas library as input and write csv file with 
        default delimeter ','
        """
        inputDataFrame.to_csv(outputFilePath, index = False)
#|------------------------writeCSV -ends---------------------------------------|    
