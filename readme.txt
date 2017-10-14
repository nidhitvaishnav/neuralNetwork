
1. We have used Python 2.7 to implement Neural Network using Backpropagation Algorithm.
2. The code is written in Eclipse IDE. The project name is neuralNetwork. It comprises src folder which contains
   following .py files.

1) dataProcessingUI.py
2) neuralNetworkUI.py
3) myIO.py
4) dataPreprocess.py
5) neuralNetwork.py
6) myUtility.py

3.a To perform the data pre-processing task, we call dataPreprocessingUI as per follow:
	python dataProcessingUI.py {CSVDataSourcePath} {CSVOutputPath}
Example:python dataProcessingUI.py https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data ../dataset/refinedIris.csv


3.b To create neural network with trainingData and test it with testing data, we call neuralNetworkUI.py as per follow:
	python neuralNetworkUI.py {CSVOutputPath} {trainingPercent} {maxIteration} {numberOfHiddenLayers} {numberOfNeuron}
Example:python neuralNetworkUI.py ../dataset/refinedIris.csv 80 200 2 2


4. Assumptions:
I.   We have used mean square error as a metric to calculate the training as well as the testing error.
II.  Weights for input layer are zero. Weights are input to the hidden layers and the output layers.
III. Learning rate is 0.5


5. DataProcessing.py reads csv file using myIO.py, from https://archive.ics.uci.edu/ml/datasets.html; 
Data has been read using myIO.py and pre-processing has been done using dataPreprocess.py
I.   It doesnot provide headers, so dummy headers has been provided
II.  Pre processing has been done as per follow:
     a. removing null values
     b. converting categorical / nominal values into numerical values
     c. scaling attribute data
III. writing data to a csv file provided in the command line argument
   
6. neuralNetwork.py performs following tasks:
I.   It reads the dataset from csv file provided in input using myIO.py
II.  It splits the dataset into training and testing dataset using myUtility.py
III. Initialization of network
     a. take weights randomly for hidden and output layers
IV.  forword propogation
     a. neuron activation: sigma(wi*xi)
     b. neuron transfer: sigmoid function = 1/(1+e(-x))
V.   Back propogation
     a. transfer derivative
     b. error back propogation
VI.  Train network
     a. update weights
VII. Predict dataset based on the neural network
VIII.Find mean square value for training and testing
IX.  Print neural network, and mean square error values

7. we have used standard libreries such as pandas for data processing, numpy for calculations, random for random weight generation

8. This project has been tested on
I.   https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
II.  https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data
III. https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
Note: As the size of adult dataset is too large, pandas gives warning to convert data from csv to dataFrame
But it gives proper output files, and proper results