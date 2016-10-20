import multiprocessing
import numpy as np

numThreads = 8
numRows = 32000
numCols = 3
numOut = 2

stride = numRows / numThreads

X = np.ones((numRows, numCols))
W = np.ones((numCols, numOut))
B = np.ones((numRows, numOut))

def conv(idx):
  for i in range(100000):
    X[idx*stride:idx*stride+stride].dot(W) + B[idx*stride:idx*stride+stride]
  return X[idx*stride:idx*stride+stride].dot(W) + B[idx*stride:idx*stride+stride]

if __name__=='__main__':
  pool = multiprocessing.Pool(numThreads)
  Y = pool.map(conv, range(numThreads))
