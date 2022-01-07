function[]=VAP_TRAP(fun,x0,xn,n)
h=(xn-x0)/n;
y0=feval(fun,x0);
yn=feval(fun,xn);
yr=0;
for i=1:1:n-1
yr=yr+feval(fun,x0+i*h)
i
end
I=(h/2)*(y0+yn+2*yr);
h
I
