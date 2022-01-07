import math


def f(x):
    result = math.exp(x)/x
    return result

xo=1
xn = 2
n = 8

h = (xn-xo)/n
sum = 0

for i in range (1,n):
    
    sum = sum + f(xo+(i*h))
    print(sum)

I=0.5*h*(f(xo)+f(xn)+(2*sum))

print (I)
