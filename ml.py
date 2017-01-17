'''
Source to Karpathys blog: http://karpathy.github.io/neuralnets/
Simulating a neuron behavior for
f(x,y,a,b,c) = ax+by+c
'''

import math

dataPoints_x = [1.2, -0.3, -3, 0.1, 3.0, 2.1]
dataPoints_y = [0.7,  0.5, -1, 1.0, 1.1, -3]
dataPoints_z = [+1, -1, +1, -1, -1, +1]

a, b, c = 1, -2, -1

for j in range(400):
    for i in range(len(dataPoints_z)):
        x = dataPoints_x[i]
        y = dataPoints_y[i]
        z = dataPoints_z[i]

        z1 = a * x + b * y + c
        pull = 0
        if z == 1 and z1 < 1:
            pull = 1
        if z == -1 and z1 > -1:
            pull = -1
        step = 0.01
        a += step * (x * pull - a)
        b += step * (y * pull - b)
        c += step * (1 * pull - c)

for i in range(len(dataPoints_z)):
    x = dataPoints_x[i]
    y = dataPoints_y[i]
    z = dataPoints_z[i]
    print(a * x + b * y + c, z)
