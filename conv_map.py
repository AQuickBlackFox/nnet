"""
Output Error
"""

import multiprocessing
import numpy as np

numThreads = 16
numRows = 32000
numCols = 2
numOut = 3

stride = numRows / numThreads

np.random.seed(0)
X = np.ones((numRows, numCols))
W = np.ones((numCols, numOut))
B = np.ones((numRows, numOut))
Y = np.ones((numRows, numOut))

Xpart = np.ones((numRows/numThreads, numCols))
Bpart = np.ones((numRows/numThreads, numOut))
Ypart = np.ones((numRows/numThreads, numOut))


def add(idx):
  Y[idx*stride:idx*stride+stride] = X[idx*stride:idx*stride+stride].dot(W) + B[idx*stride:idx*stride+stride]

if __name__=='__main__':
  pool = multiprocessing.Pool(numThreads)
  pool.map(add, range(numThreads))
print Y
