'''
Source to Karpathys blog: http://karpathy.github.io/neuralnets/
Simulating a neuron behavior for
f(x,y,a,b,c) = sig(ax+by+c)
'''

import math

def Sig(u):
    return 1 / (1 + math.exp(-u))

def Circuit(a, b, c, x, y):
    return Sig(a*x + b*y + c)

class Neuron:
    x, y, a, b, c = 0, 0, 0, 0, 0
    p, q, r = 0, 0, 0
    f = 0
    dfda, dfdb, dfdc, dfdx, dfda, dfdb = 0, 0, 0, 0, 0, 0
    def __init__(self, a, b, c, x, y, step):
        self.a, self.b, self.c, self.x, self.y, self.step = a, b, c, x, y, step
    def Product(self, u, v):
        return u * v
    def Sum(self, u, v):
        return u + v
    def Sig(self, u):
        return 1 / (1 + math.exp(-u))
    def Forward(self):
        self.p = self.Product(self.a, self.x)
        self.q = self.Product(self.b, self.y)
        self.r = self.Sum(self.Sum(self.p, self.q), self.c)
        self.f = self.Sig(self.r)
    def Backward(self, printGrad):
        dpda, dpdx = self.x, self.a
        dqdb, dqdy = self.y, self.b
        drdp, drdq, drdc = 1, 1, 1
        drda, drdx = drdp * dpda, drdp * dpdx
        drdb, drdy = drdq * dqdb, drdq * dqdy
        dfdr = self.f*(1-self.f)
        self.dfda, self.dfdx = dfdr * drda, dfdr * drdx
        self.dfdb, self.dfdy = dfdr * drdb, dfdr * drdy
        self.dfdc = dfdr * drdc
        print("dfda, dfdb, dfdc, dfdx, dfdy", self.dfda, self.dfdb, self.dfdc, self.dfdx, self.dfdy)
    def Output(self, printOut):
        a = self.dfda * self.step + self.a
        b = self.dfdb * self.step + self.b
        c = self.dfdc * self.step + self.c
        x = self.dfdx * self.step + self.x
        y = self.dfdy * self.step + self.y
        print("a, b, c, x, y", a, b, c, x, y)
    def Gradient(self):
        h = 0.0001
        da = (Circuit(self.a + h, self.b, self.c, self.x, self.y) - Circuit(self.a, self.b, self.c, self.x, self.y))/h
        db = (Circuit(self.a, self.b + h, self.c, self.x, self.y) - Circuit(self.a, self.b, self.c, self.x, self.y))/h
        dc = (Circuit(self.a, self.b, self.c + h, self.x, self.y) - Circuit(self.a, self.b, self.c, self.x, self.y))/h
        dx = (Circuit(self.a, self.b, self.c, self.x + h, self.y) - Circuit(self.a, self.b, self.c, self.x, self.y))/h
        dy = (Circuit(self.a, self.b, self.c, self.x, self.y + h) - Circuit(self.a, self.b, self.c, self.x, self.y))/h
        print("da, db, dc, dx, dy",da, db, dc, dx, dy)


neuron = Neuron(-1, 3, 1, 2, -3, 0.01)
neuron.Forward()
neuron.Backward(True)
neuron.Output(True)
neuron.Gradient()
