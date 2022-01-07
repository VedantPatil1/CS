#Curve fitting Exponential Function
import numpy as np
import math


x = [0,1,2,3]
y = [2,2.2103,2.4428,2.6997]


n = len(x)


sumx = 0
sumx2 = 0
sumy = 0
sumxy = 0


for i in range(n):
    Y = math.log(y[i])
    sumx = sumx + x[i]
    sumx2 = sumx2 + math.pow(x[i],2)
    sumy = sumy + Y
    sumxy = sumx + (x[i] * Y)

dA = np.array([[sumxy,sumx],[sumy,n]])
dB = np.array([[sumx2,sumxy],[sumx,sumy]])
dS = np.array([[sumx2,sumx],[sumx,n]])

A = np.linalg.det(dA)/np.linalg.det(dS)
B = np.linalg.det(dB)/np.linalg.det(dS)

a = math.exp(B)
b = A

print ('y= ',a,'* e^(',b,'x)')