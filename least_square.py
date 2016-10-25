import numpy as np

numRows = 1600
numCols = 4

np.random.seed(0)

def create_twice(x):
  return x * 2

if __name__ == '__main__':
  x = np.random.randn(numRows, numCols)
  t = create_twice(x)
