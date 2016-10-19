"""
Error output
"""
from multiprocessing import Process
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

Xpart = np.zeros((numRows/numThreads, numCols))
Bpart = np.zeros((numRows/numThreads, numOut))
Ypart = np.zeros((numRows/numThreads, numOut))

Xout, Yout = [], []

for j in range(numThreads):
  Xout.append(Xpart)
  Yout.append(Ypart)

def add(X, B, idx):
  for j in range(numRows*10):
    Yout[idx] = X.dot(W) + B

if __name__=='__main__':
  jobs = []
  for i in range(numThreads):
    p = Process(target=add, args=(X[i*stride:i*stride+stride],B[i*stride:i*stride+stride],i,))
    jobs.append(p)

  for i in range(numThreads):
    jobs[i].start()

  for i in range(numThreads):
    jobs[i].join()
