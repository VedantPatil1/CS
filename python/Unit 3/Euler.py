import math



def dy_dx(x,y):
    result = x+ math.pow(2,y)
    return result


y1 = 1
xo = 1
xn = 1.4
h = 0.1

x=[xo,]
y=[y1,]

while xo < xn:
    y1 = y1 + (h * dy_dx(xo,y1))
    xo=xo+h
    y.append(y1)
    x.append(xo)

print ("y=",y1)

print (y)
print(x)
