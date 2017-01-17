'''
Source to Karpathys blog: http://karpathy.github.io/neuralnets/
Simulating a neuron behavior for
n1 = max(a1*x + b1*y + c1)
n2 = max(a2*x + b2*y + c2)
n3 = max(a3*x + b3*y + c3)
score = a4*n1 + b4*n2 + c4*n3 + d4
'''

import math, random

dataPoints_x = [1.2, -0.3, -3, 0.1, 3.0, 2.1]
dataPoints_y = [0.7,  0.5, -1, 1.0, 1.1, -3]
dataPoints_z = [+1, -1, +1, -1, -1, +1]

a1, a2, a3, a4 = random.random(), random.random(), random.random(), random.random()
b1, b2, b3, b4 = random.random(), random.random(), random.random(), random.random()
c1, c2, c3, c4 = random.random(), random.random(), random.random(), random.random()
d4 = random.random()

def layer1(x, y):
    return max(0, a1*x + b1*y + c1)

def layer2(x, y):
    return max(0, a2*x + b2*y + c2)

def layer3(x, y):
    return max(0, a3*x + b3*y + c3)

def layer4(x, y, z):
    return a4*x + b4*y + c4*z + d4

for j in range(400):
    for i in range(len(dataPoints_z)):
        x = dataPoints_x[i]
        y = dataPoints_y[i]
        z = dataPoints_z[i]
        n1 = layer1(x, y)
        n2 = layer2(x, y)
        n3 = layer3(x, y)
        score = layer4(n1, n2, n3)
        pull = 0
        if z == 1 and score < 1:
            pull = 1
        if z == -1 and score > -1:
            pull = -1
        step = 0.01
        dscore = pull
        da4 = n1 * dscore
        dn1 = a4 * dscore
        db4 = n2 * dscore
        dn2 = b4 * dscore
        dc4 = n3 * dscore
        dn3 = c4 * dscore
        dd4 = 1 * dscore
        if n3 == 0:
            dn3 = 0
        if n2 == 0:
            dn2 = 0
        if n1 == 0:
            dn1 = 0
        da1 = x * dn1
        db1 = y * dn1
        dc1 = 1 * dn1
        da2 = x * dn2
        db2 = y * dn2
        dc2 = 1 * dn2
        da3 = x * dn3
        db3 = y * dn3
        dc3 = 1 * dn3
        da1 += -a1
        da2 += -a2
        da3 += -a3
        db1 += -b1
        db2 += -b2
        db3 += -b3
        da4 += -a4
        db4 += -b4
        dc4 += -c4
        a1 += step * da1
        b1 += step * db1
        c1 += step * dc1
        a2 += step * da2
        b2 += step * db2
        c2 += step * dc2
        a3 += step * da3
        b3 += step * db3
        c3 += step * dc3
        a4 += step * da4
        b4 += step * db4
        c4 += step * dc4
        d4 += step * dd4


for i in range(len(dataPoints_z)):
    x = dataPoints_x[i]
    y = dataPoints_y[i]
    z = dataPoints_z[i]
    print(a1 * x + b1 * y + c1, z)
