import random
import numpy as np

class MyUtility:
    
#|-----------------------------------------------------------------------------|
# splitDataset
#|-----------------------------------------------------------------------------|
    def splitDataset(self, inputDataFrame, trainingPercent):
        """
        splitting dataset randomly  into training and testing datasets 
        based on trainingPercent
        """
        trainingDataFrame =inputDataFrame.sample(\
                                        frac=float(trainingPercent)/float(100),\
                                        random_state = 1)

        testingDataFrame = inputDataFrame.loc[~inputDataFrame.index.isin(\
                                                    trainingDataFrame.index)]
        return trainingDataFrame,testingDataFrame
#|------------------------splitDataset -ends-----------------------------------|
#|-----------------------------------------------------------------------------|
# createNestedDict
#|-----------------------------------------------------------------------------|
    def createNestedDict(self, myDict, value, *path):
        """
        it can create nested dictionary
        """
        for level in path[:-1]:
            myDict = myDict.setdefault(level, {})
        #for level -ends
        dict[path[-1]]=value
        return myDict
#|------------------------createNestedDict -ends-------------------------------| 
#|-----------------------------------------------------------------------------|
# segregateAttributesAndClass
#|-----------------------------------------------------------------------------|
    def segregateAttributesAndClass(self, inputArr, inputHeader):
        """
        given function takes inputArr and inputHeader which contains attributes
        and class values,and
        returns attributeArr, attributeHeader and classArr
        """
        # finding total rows and column of dataArr
        dataRows, dataCols = np.shape(inputArr)
        # retrieving last column of dataArr
        classArr = inputArr[:, dataCols-1]
        
        #retrieving attributeArr
        attributeArr = inputArr[:, :dataCols-1]

        #retrieving attributeHeader
        attributeHeader = inputHeader[:dataCols-1]
        
        return attributeArr, classArr, attributeHeader
    
#|------------------------segregateAttributesAndClass -ends--------------------|           