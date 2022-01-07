import math


def f(x,y):
    result = math.pow(x,2) + y
    return result


h = 0.02
yo = 1
xo = 0
xn = 0.02

while xo<xn:
    k1 = h * f(xo,yo)
    k2 = h * f(xo + h,yo + k1)
    yo = yo +(0.5*(k1+k2))
    xo = xo + h

print(yo)