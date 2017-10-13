from _collections import defaultdict
import numpy as np
from __builtin__ import str
from myUtility import MyUtility

names = []
for i in range(3):
    names.append("data"+str(i))
#for i ends
keys=["homework", "quizzes", "tests"]
dic={ name.capitalize():{ key:[] for key in keys} for name in names}
print ('dic = {} '.format(dic))

dic['Data1']['homework']=[12,13]
# dic['data1']={'tests':[1,2]}

# myUtil = MyUtility()
# dic = myUtil.createNestedDict(dic, [5,1,2], "data1", "homework")
#debug
print ('dic = {} '.format(dic))

#debug -ends

a=2
#debug
print ('np.exp(a) = {} '.format(np.exp(a)))
#debug -ends