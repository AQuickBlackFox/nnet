# 1 Nearest Neighbor Classifier

import numpy as np

numData = 10
numTest = 6
Row, Col = 16, 16
X = []
Y = []
Z = []
label = {0:"Black", 1:"Light Black", 2:"Dark Grey", 3:"Grey", 4:"Light Grey", 5:"Light White", 6:"White", 7:"Dark White"}
np.random.seed(0)

"""
A 16x16 matrix with values 0 - 255
0 - 31 = Black
32 - 63 - Light Black
64 - 95 - Dark Grey
96 - 127 - Grey
128 - 159 - Light Grey
160 - 191 - Light White
192 - 223 - White
224 - 255 - Dark White
"""
def createData():
    for i in range(numData):
        X.append(np.random.rand(16*16,1)*255)
    for i in range(numTest):
        Z.append(np.random.rand(16*16,1)*255)
#    print(X)

def getMaxId(histogram):
    count = -1
    index = -1
    for i in range(len(histogram)):
        if histogram[i] > count:
            count = histogram[i]
            index = i
    return index

def doHistogram(x):
    histogram = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(x)):
        if x[i] > -1 and x[i] < 32:
            histogram[0] += 1
        if x[i] > 32 and x[i] < 64:
            histogram[1] += 1
        if x[i] > 64 and x[i] < 96:
            histogram[2] += 1
        if x[i] > 96 and x[i] < 128:
            histogram[3] += 1
        if x[i] > 128 and x[i] < 160:
            histogram[4] += 1
        if x[i] > 160 and x[i] < 192:
            histogram[5] += 1
        if x[i] > 192 and x[i] < 224:
            histogram[6] += 1
        if x[i] > 224 and x[i] < 256:
            histogram[7] += 1
    index = getMaxId(histogram)
    return label[index]



def preClassify():
    for i in range(numData):
        Y.append(doHistogram(X[i]))

def doClassify(z):
    val = 10000
    index = -1
    for i in range(numData):
        _abs = abs(np.sum(z-X[i]))
        if val > _abs:
            val = _abs
            index = i
    return Y[index]

def oneNN():
    for i in range(numTest):
        print(doClassify(Z[i]))

createData()
preClassify()
oneNN()
