import math

x1=1
x2=2
accuracy = 0.001

def fun(x):
    #result = math.pow(x,3) - 16*math.pow(x,2) + 3
    result = math.pow(x,3)-18
    return result
#---------------------------------------------------------------------------

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
#---------------------------------------------------------------------------

y1 = fun(x1)
y2 = fun(x2)
while (y1*y2) > 0 :

    print("Since f(x1)*f(x2) is positive, enter different values")
    x1 = float(input("x1 : "))
    y1 = fun(x1)
    print("f(",x1,") = ",y1)
    x2 = float(input("x2 = "))
    y2 = fun(x2)
    print("f(",x2,") = ",y2)


sign_print_statement("1","2",x1,x2)

i=0
while abs(x1-x2)>accuracy:
    i=i+1
    x3 = (x1+x2)/2
    print("________________________________________")
    print("\n\n",i,".)  x3 =(",x1,"+",x2,")    / 2 \n = ",x3)
    y3 = fun(x3)
    print ("f(x3) = ",y3)
    if (y1*y3)<0:
        print ("Since f(x1)*f(x3)<0   - \n\n   Let x1 = ",x1,"\n   and x2 = ",x3)
        x2=x3
        y2 = fun(x2)
    elif (y1*y3)>0 :
        print ("Since f(x1)*f(x3)>0   +\n\n   Let x1 = ",x3,"\n   and x2 = ",x2)
        x1=x3
        y1 = fun(x1)
    else :
        print (y3)
        break

print("\nthe root is x3 = ",x3)
print (i)
