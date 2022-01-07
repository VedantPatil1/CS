
function[]=VAP_RK2(fun,x0,y0,xn,h)
n=(xn-x0)/h;
for i=1:n
k1=h*feval(fun,x0,y0);
k2=h*feval(fun,x0+h,y0+k1);
k=1/2*(k1+k2);
yn=y0+k;
x0=x0+h;
y0=yn;
end
yn
