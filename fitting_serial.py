import numpy as np

numElements = 2000
numOutput = 1
x = np.random.uniform(0, 1, numElements)
noise_factor = 0.2
noise = np.random.randn(numElements) * noise_factor
w = np.random.randn(1,1)

def f(x):
  return x * 2

def network(x, w):
  return x * w

def loss(t, y):
  return (t-y)**2

def derv(t, y, x):
  return 2 * (y-t) * x

def delta(t, y, x, lrate):
  return derv(t, y, x).sum() * lrate

if __name__ == '__main__':
  t = f(x) + noise
  for i in range(10):
    y = network(x, w)
    dw = delta(t, y, x, 0.001)
    w = w - dw
  print w
