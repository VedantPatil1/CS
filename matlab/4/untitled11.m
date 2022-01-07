x=input('Enter the values of x');
y=input('Enter the values of y');
n=length(x);
sumx=0;sumy=0;sumx2=0;sumxy=0;
for i=1:1:n
sumx=sumx+x(i);
    sumx2=sumx2+(x(i))^2;
sumxy=sumxy+y(i)*x(i);
sumy=sumy+y(i);
end
p=[sumx2,sumx;sumx,n];
q=[sumxy;sumy];
s=p\q
A=s(1)
B=s(2)
fprintf('Y=%f*X+%f',A,B)
