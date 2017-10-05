import copy


class DataPreprocess:
    
#|-----------------------------------------------------------------------------|
# removeNullValues
#|-----------------------------------------------------------------------------|
    def removeNullValues(self, inputDataList):
        """
        given function removes data which has null values
        """
        listWithoutNull = copy.deepcopy(inputDataList)
        for data in inputDataList:
            for dataCol in data:
                
                if (dataCol=='?'):
                    listWithoutNull.remove(data)
                    break
                #if data[col] ends
            #for col -ends
        #for data -ends
        #debug
        print ('listWithoutNull =\n {}'.format(listWithoutNull))
        print ('inputDataList size = {} '.format(len(inputDataList)))
        print ('listWithoutNull size= \n{}'.format(len(listWithoutNull)))
        #debug -ends
        return listWithoutNull
#|------------------------removeNullValues -ends-------------------------------|    