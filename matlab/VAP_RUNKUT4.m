function[]=VAP_RUNKUT4(fun,x0,y0,xn,h)
n=(xn-x0)/h;
for i=1:n
k1=h*feval(fun,x0,y0);
k2=h*feval(fun,x0+h/2,y0+k1/2);
k3=h*feval(fun,x0+h/2,y0+k2/2);
k4=h*feval(fun,x0+h,y0+k3);
k=1/6*(k1+2*k2+2*k3+k4);
yn=y0+k;
x0=x0+h;
y0=yn;
end
yn

