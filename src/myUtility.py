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
        #finding number of training and testing rows
        nRows, nCols= inputDataFrame.shape
        trainingRows = int(float(nRows*trainingPercent)/float(100))
        testingRows = nRows - trainingRows
        
        
        #TODO: random seed for debugging
        random.seed(1)
        
        #finding random index for training dataset
        trainingRowsIndex = random.sample(range(0,nRows), trainingRows)
        
        #debug
        print ('nRows = {}, trainingRows = {}, testingRows = {},'\
                             'trainingRowIndex = {}'.format(nRows, trainingRows,\
                                        testingRows, len(trainingRowsIndex)))
        print ('trainingRowsIndex =\n {} '.format(trainingRowsIndex))
        #debug -ends
        
        trainingDataArr = np.empty([trainingRows, nCols])
#         #debug
#         print ('trainingDataArr.shape = {} '.format(trainingDataArr.shape))
#         #debug -ends
        for myIndex in trainingRowsIndex:
            tempDataArr = inputDataFrame.iloc[myIndex].as_matrix()
            #debug
            print ('{} : {} '.format(myIndex, tempDataArr))
            print ('tempDAtaArr.shape = {}'.format(tempDataArr.shape))
            #debug -ends
            
            trainingDataArr = np.vstack([trainingDataArr, tempDataArr])
        #for myIndex -ends
#         trainingDataArr = np.around(trainingDataArr, 4)
        #debug
        print ('trainingDataArr =\n {} '.format(trainingDataArr))
        #debug -ends
#|------------------------splitDataset -ends----------------------------------|    