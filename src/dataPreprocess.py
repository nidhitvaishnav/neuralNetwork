import numpy as np
import copy


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
#         return inputDataFrame
#|------------------------removeNullValues -ends-------------------------------|   
   
# 
#|-----------------------------------------------------------------------------|
# categoricalToNumericalConversion
#|-----------------------------------------------------------------------------|
    def categoricalToNumericalConversion(self, rawDataFrame):
        """
        given function converts categorical/nominal data into numerical data:
        input: dataframe of pandas with categorical values
        output: dataframe of pandas
        """
        #debug
        print ('rawDataFrame.dtype() = {} '.format(rawDataFrame.dtypes))
        #debug -ends
        #creating a data frame which contains the object type values
        objDataFrame = rawDataFrame.select_dtypes(include=['object']).copy()
        print (objDataFrame.head(10))
        
        nRows, nCols = objDataFrame.shape
        for myIndex in range(0,nCols):
            currentAtrDataFrame = objDataFrame.ix[:,myIndex]
            #debug
            print ('++++++++++++++++++++++++++')
            print ('object type')
            print ('++++++++++++++++++++++++++')

            print ('currentAtrDataFrame: \n{} '.format(currentAtrDataFrame))
            #debug -ends
            currentAtrDataFrame = currentAtrDataFrame.astype("category")

            currentAtrDataFrame = currentAtrDataFrame.cat.codes
            #debug
            print ('---------------------------------')
            print ('category type')
            print ('---------------------------------')
            print ('currentAtrDataFrame: \n{} '.format(currentAtrDataFrame))

            #debug -ends
        
        


     
#|------------------------categoricalToNumericalConversion -ends---------------|    