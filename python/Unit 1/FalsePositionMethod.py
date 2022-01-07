import math
x1=0
x2= 1
accuracy = 0.0001

def fun(x):
    result = result = 0.99403+(1.671*math.pow(10,-4)*x)+(9.7215*math.pow(10,-8)*math.pow(x,2))-(9.5838*math.pow(10,-11)*math.pow(x,3))+( 1.952*math.pow(10,-14)*math.pow(x,4)) - 1.1
    return result

def sign(num):
    res="negetive"
    if num>0:
        res="positive"
    return res
def sign_print_statement(a,b,n1,n2):
    y1 = fun(n1)
    y2 = fun(n2)
    sign_y1=sign(y1)
    sign_y2=sign(y2)
    print ("Since f(x"+a+") is", sign_y1, "and f(x"+b+") is ",sign_y2,"\n   Let x"+a+" = ",n1,"\n   and x"+b+" = ",n2)

y1 = fun(x1)
y2 = fun(x2)
while (y1*y2) > 0 :
    print("Since f(x1)*f(x2) is positive, enter different values")
    x1 = float(input("x1 = "))
    x2 = float(input("x2 = "))
    y1 = fun(x1)
    y2 = fun(x2)


sign_print_statement("1","2",x1,x2)

i=0
while abs(x1-x2)>accuracy:
    i=i+1
    x3 = ((x2*y1)-(x1*y2))/(y1-y2)
    print("x3 =(",x1,"+",x2,")    / 2 \n = ",x3)
    y3 = fun(x3)
    print ("\nf(x3)",y3)
    if (y1*y3)<0:
        print ("Since f(x1)*f(x3)<0\n   Let x1 = ",x1,"\n   and x2 = ",x3)
        x2=x3
        y2 = fun(x2)
    elif (y1*y3)>0 :
        print ("Since f(x1)*f(x3)>0\n   Let x1 = ",x3,"\n   and x2 = ",x2)
        x1=x3
        y1 = fun(x1)
    else :
        print("the root is x3 = ",x3)
        print (y3)
        break

print (x3)
print (i)