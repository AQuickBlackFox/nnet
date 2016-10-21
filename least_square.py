import numpy as np

numRows = 1600
numCols = 4

np.random.seed(0)

t = np.random.randn(numRows, numCols)
y = np.random.randn(numRows, numCols)

def least_square():
  return (t - y)**2

if __name__ == '__main__':
  print least_square()[0]
  print (t[0][0] - y[0][0])**2
