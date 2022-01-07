#STRAIGHT LINE CURVE FITTING

import numpy as np
import math


x = [19,25,30,36,40,45,50]
y = [76,77,79,80,82,83,85]

n = len(x)


sumx = 0
sumx2 = 0
sumy = 0
sumxy = 0


for i in range(n):
    sumx = sumx + x[i]
    sumx2 = sumx2 + math.pow(x[i],2)
    sumy = sumy + y[i]
    sumxy = sumx + (x[i] * y[i])

'''
A=(  (n*sumxy)  +  (sumx*sumy)  )     /    (  (n*sumx2)  +  (sumx*sumx)  )
B=(  sumy - (sumx*A)  ) / n


'''
p = np.array([[sumx2,sumx],
                [sumx,n]])
q = np.array([sumxy,sumy])

s = np.divide(q,p)

A = s[0]
B = s[1]

print ('Y=',A,'X + ',B)