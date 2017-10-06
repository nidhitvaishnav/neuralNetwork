import pandas as pd
from pandas.core.dtypes.missing import na_value_for_dtype


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

