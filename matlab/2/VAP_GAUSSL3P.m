
function[]=VAP_GAUSSL3P(fun,x0,xn)
a=(xn-x0)/2;
b=(xn+x0)/2;
x1=-a*sqrt(3/5)+b;
x2=a*sqrt(3/5)+b;
x3=b;
f1=feval(fun,x1);
f2=feval(fun,x2);
f3=feval(fun,x3);
I=(8/9*f3+(f1+f2)*5/9)*a;
I
