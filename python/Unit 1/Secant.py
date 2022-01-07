import math
acc = 0.001

def f(x):
    result = math.pow(x,3)-2*x-5
    return result

x1 = float(input("Enter x1 = "))
x2 = float(input("Enter x2 = "))

while (abs(f(x2)-f(x1))>acc):
    print ("---------------------------------------------------------------------------")
    print ("x1=",x1,"\nx2=",x2)
    print ('f(x1)=',f(x1))
    print ('f(x2)=',f(x2))
    x3 = x2-( (x2-x1)/(f(x2)-f(x1)) )*f(x2)
    x1=x2
    x2=x3
    print ('x3=',x3)
    