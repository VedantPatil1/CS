import math
acc = 0.001
maxitr=6

def fun1(x):
    y = (x*x*x*x)-x-10
    return y

def dfun1(x):
    y = (4*x*x*x)-1
    return y

def ddfun1(x):
    y = 12*x*x
    return y

def guess(x):
    g = (fun1(x)*ddfun1(x))/(dfun1(x)*dfun1(x))
    return g

x=float(input("Initial Guess"))
g = guess(x)
while abs(g)>1:
    x=float(input("Re-Enteer Initial Guess"))
    g = guess(x)


itr = 1
while itr<=maxitr:
    print('---')
    x1= x - (fun1(x)/dfun1(x))
    print (x1)
    if abs(x1-x)<acc:
        break
    else: 
        x=x1
        itr=itr+1

print("Root of the equation is = ",x1)