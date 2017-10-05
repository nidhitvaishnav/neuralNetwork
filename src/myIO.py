import pandas as pd


class MyIO:
    """
    This class performs input - output tasks.
    """

#|-----------------------------------------------------------------------------|
# inputCSV
#|-----------------------------------------------------------------------------|
    def inputCSV(self, filePath):
        """
        given method takes csv file path as an input; reads csv file and
        return data in the form of numpy array
        """
#         inputObj = pd.read_csv(filepath_or_buffer  = filePath, header = None,\
#                                                          delimiter = '\t')
        inputObj = pd.read_csv(filepath_or_buffer  = filePath, header = None)
        inputArr = inputObj.values
        
#         inputHeader = inputObj.columns.tolist()
        
        inputDataList = inputArr.tolist()   
        return inputDataList
#|------------------------inputCSV -ends---------------------------------------|

