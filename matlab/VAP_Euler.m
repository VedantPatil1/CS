function[]=VAP_Euler(fun,x0,y1,xn,h)
while x0<xn
    y1=y1+h*feval(fun,x0,y1);
x0=x0+h;
end
y1
