'''
Source to Karpathys blog: http://karpathy.github.io/neuralnets/
f(x,y) = x*y

Goal:
1. Given x = -2, x = 3, and output = -6,
How should one tweak inputs to increase the output?
'''
import numpy as np

def Multiply(x, y):
    return x * y

def randLocalSearch():
    '''
    Brute force approach to finding the possible
    x, y to get better multiplication output
    '''
    x_start = -2
    y_start = 3
    z_start = Multiply(x_start, y_start)
    tweak = 0.01
    for i in range(100):
        x = x_start + tweak * (2* np.random.rand(1,1)[0][0] - 1)
        y = y_start + tweak * (2* np.random.rand(1,1)[0][0] - 1)
        z = Multiply(x, y)
        if z > z_start:
            z_start = z
    print("Random Local Search:\t", x, " * ", y, " = ", z_start)

def numericalGradient():
    '''
    Moving inputs along the direction derivative points to,
    to increase the output.
    '''
    x_start = -2
    y_start = 3
    tweak = 0.001
    step_size = 0.01
    z_start = Multiply(x_start, y_start)
    dfdx = (Multiply(x_start + tweak, y_start) - z_start)/tweak
    dfdy = (Multiply(x_start, y_start + tweak) - z_start)/tweak
    x = dfdx * step_size + x_start
    y = dfdy * step_size + y_start
    z = Multiply(x, y)
    print("Numerical Gradient:\t", x, " * ",y," = ",z)

if __name__ == '__main__':
    randLocalSearch()
    numericalGradient()
