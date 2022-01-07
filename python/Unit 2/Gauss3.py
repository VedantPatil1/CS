import math


def f(x):
    result = math.pow(x,2)-5*x+2
    return result


xo = 3
xn = 5

a = (xn-xo)/2
b = (xn+xo)/2

x1 = a*math.sqrt(3/5) +b
x2 = -a*math.sqrt(3/5) +b
x3 = b


I = ((8/9)*f(x3) + (f(x1)+f(x2))*(5/9))* a
print(I)
