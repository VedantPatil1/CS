import math


def f(x):
    result = math.exp(x)/x
    return result

xo=1
xn = 2
n = 8

h = (xn-xo)/n
set = 0
setof3 = 0
for i in range (1,n):
    if (i%3)!=0:
        set = set + f(xo+(i*h))
    else:
        setof3 = setof3 + f(xo+(i*h))

I=(h/8)*3*((f(xo)+f(xn)) + (3*set) + (2*setof3))

print (I)
