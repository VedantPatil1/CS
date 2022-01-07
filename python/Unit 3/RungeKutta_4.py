import math

def f(x,y):
    result = 1 + math.pow(y,2)
    return result

    
h = 0.2
xo = 0
yo = 0
xn = 0.2

while xo<xn:
    k1 = h*f((xo),(yo))
    k2 = h*f((xo+(0.5*h)),(yo + (0.5*k1)))
    k3 = h*f((xo+(0.5*h)),(yo + (0.5*k2)))
    k4 = h*f((xo+h),(yo + k3))
    k = (1/6) *(k1 + (2*k2) + (2*k3)+ k4)
    yo = yo+k
    xo = xo + h

print (yo)

