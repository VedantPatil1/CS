x=input('enter x vector');
y=input('enter y vector');
n=length(x);
sumx=0;
sumY=0;
sumxY=0;
sumxx=0;
for i=1:1:n
Y(i)=log(y(i));
sumx=sumx+x(i);
sumY=sumY+Y(i);
sumxY=sumxY+(x(i)*Y(i));
sumxx=sumxx+(x(i)*x(i));
end
%BY CRAMER'S RULE
dA=[sumxY,sumx;sumY,n];
dB=[sumxx,sumxY;sumx,sumY];
dS=[sumxx,sumx;sumx,n];
A=det(dA)/det(dS);
B=det(dB)/det(dS);
a=exp(B);
b=A;
fprintf('y = %0.4f x e^(%0.4fx) \n',a,b);
yy=a.*exp(b.*x);
plot(x,y,'-rx',x,yy,'-bv')
