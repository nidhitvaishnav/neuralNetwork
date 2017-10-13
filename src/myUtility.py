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
        #print(inputDataFrame.shape)
        #print(trainingdf.shape)
        testingDataFrame = inputDataFrame.loc[~inputDataFrame.index.isin(\
                                                    trainingDataFrame.index)]
        #print(testingdf.shape)
        return trainingDataFrame,testingDataFrame
#|------------------------splitDataset -ends-----------------------------------|
#|-----------------------------------------------------------------------------|
# createNestedDict
#|-----------------------------------------------------------------------------|
    def createNestedDict(self, myDict, value, *path):
        """
        
        """
        #debug
        print ('path = {} '.format(path))
        #debug -ends
        for level in path[:-1]:
            #debug
            print ('level = {} '.format(level))
            #debug -ends
            myDict = myDict.setdefault(level, {})
        #for level -ends
        dict[path[-1]]=value
        return myDict
#|------------------------createNestedDict -ends-------------------------------|        