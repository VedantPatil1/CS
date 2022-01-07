import math


def f(x):
    result = math.exp(x)/x
    return result

xo=1
xn = 2
n = 8

h = (xn-xo)/n
odd = 0
even = 0
for i in range (1,n):
    if (i%2)==0:
        even = even + f(xo+(i*h))
    else:
        odd = odd + f(xo+(i*h))

I=(h/3)*((f(xo)+f(xn)) + (4*odd) + (2*even))

print (I)
