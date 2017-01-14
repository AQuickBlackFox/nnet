'''
Source to Karpathys blog: http://karpathy.github.io/neuralnets/
f(x,y,z) = x + y * z
'''

def q(a, b):
    return a + b

def Product(a, b):
    return a * b

def f(x, y, z):
    return Product(z, q(x, y))

def RecursiveCase():
    x, y, z = -2, 5, -4
    print("Initial Output:\t",x,"+",y,"*",z,"=",f(x,y,z))
    h = 0.0001
    dx = (f(x + h, y, z) - f(x, y, z))/h
    dy = (f(x, y + h, z) - f(x, y, z))/h
    dz = (f(x, y, z + h) - f(x, y, z))/h
    print(dx, dy, dz)
    step_size = 0.01
    dfdx = z
    dfdy = z
    dfdq = z
    dfdz = q(x, y)
    x = dfdx * step_size + x
    y = dfdy * step_size + y
    z = dfdz * step_size + z
    print("Final Output:\t",x,"+",y,"*",z,"=",f(x,y,z))



RecursiveCase()
