import numpy as np


class DataPreprocess:

#|-----------------------------------------------------------------------------|
# provideHeaders
#|-----------------------------------------------------------------------------|
    def provideHeaders(self, inputDataFrame):
        """
        given function takes raw input data and provides dummy headers
        """
        #finding size of inputDatalist
        nRows, nCols = inputDataFrame.shape
        #initiating header list
        headerList = []
        
        #assigning dummy headers; 1 to second last column
        for num in range(1, nCols):
            headerName = 'header_'+str(num)
            headerList.append(headerName)
        #for i -ends
        
        #last column will be class column, so providing its header as 'class'
        headerList.append('class')
        
        return headerList
#|------------------------provideHeaders -ends----------------------------------| 
#|-----------------------------------------------------------------------------|
# removeNullValues
#|-----------------------------------------------------------------------------|
    def removeNullValues(self, inputDataFrame):
        """
        given function removes data which has null values
        input: dataframe of pandas
        output: dataframe
        """
        #removing null rows
        nullRemovedDataFrame = inputDataFrame.dropna()

        return nullRemovedDataFrame
#|------------------------removeNullValues -ends-------------------------------|   
#|-----------------------------------------------------------------------------|
# scaleData
#|-----------------------------------------------------------------------------|
    def scaleData(self, inputDataFrame):
        """
        for scaling, given dataframe checks for the integer, long and float 
        data, find their mean, and divide the value by standard deviation
        """
        #finding shape of dataframe
        nRows, nCols = inputDataFrame.shape

        #for all columns if column is not of object type, scale data
        for currentCol in range(0, nCols-1):
            if (inputDataFrame.dtypes[currentCol] != object):
                #finding header name
                headerName = inputDataFrame.columns[currentCol]
                #if data type is not float & object (integer) than converting
                #it into float type, so that it doesn't give 0 for 0.xyz after
                #scaling
                if(inputDataFrame[headerName].dtypes!=float):
                    inputDataFrame[headerName]=inputDataFrame[headerName].astype("float64")
                #if -ends
                #finding mean and standard deviation
                colMean = np.mean(inputDataFrame[headerName])
                colStdDev = np.std(inputDataFrame[headerName])
#                 #debug
#                 print ('{}:- colMean = {} colStdDev = {}'.format(headerName,\
#                                                             colMean, colStdDev))
#                 #debug -ends
                
                #for all available rows(which has not been removed) scale data
                #and replace cell value with new value
                for rowIndex, rowData in inputDataFrame.iterrows():
                    oldValue = inputDataFrame.ix[rowIndex, headerName]
                    #rounding values till 4 digit
                    newValue = round(float(oldValue - colMean)/float(colStdDev),4)
                    inputDataFrame.set_value(rowIndex, headerName, newValue)
                #for currentRow -ends
            #if !=object -ends
        #for currentCol -ends
        return inputDataFrame
    
#|------------------------scaleData -ends----------------------------------|    

#|-----------------------------------------------------------------------------|
# categoricalToNumericalConversion
#|-----------------------------------------------------------------------------|
    def categoricalToNumericalConversion(self, dataFrame):
        """
        given function converts categorical/nominal data into numerical data:
        input: dataframe of pandas with categorical values
        output: dataframe of pandas
        """
        
        #creating a data frame which contains the object type values
        objDataFrame = dataFrame.select_dtypes(include=['object']).copy()
         
        nRows, nCols = objDataFrame.shape
        #for all column converting object type in categoty type and assigning
        #appropriate code
        for myIndex in range(0,nCols):
            headerName = objDataFrame.columns[myIndex]
            objDataFrame[headerName] = objDataFrame[headerName].astype("category")
            objDataFrame[headerName] = objDataFrame[headerName].cat.codes
            #writing objectDataFrame column to its respective dataFrame column
            dataFrame[headerName] = objDataFrame[headerName]            
        #for myIndex -ends

        return dataFrame
#|------------------------categoricalToNumericalConversion -ends---------------|    