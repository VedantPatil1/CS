
function[]=VAP_SIMP(fun,x0,xn,n)
h=(xn-x0)/n;
y0=feval(fun,x0);
yn=feval(fun,xn);
yodd=0;	
for i=1:2:n-1
yodd=yodd+feval(fun,x0+i*h);
end
yeven=0;
for j=2:2:n-1
yeven=yeven+feval(fun,x0+j*h);
end
I=(h/3)*(y0+yn+2*yeven+4*yodd);
h
I
