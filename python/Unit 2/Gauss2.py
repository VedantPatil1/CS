import math


def f(x):
    result = math.pow(x,3)+x-1
    return result


xo = 1
xn = 4


a = (xn-xo)/2
b = (xn+xo)/2

x1 = -a /math.sqrt(3) +b
x2 = a/math.sqrt(3) +b

I = (f(x1)+f(x2))*a

print(I)