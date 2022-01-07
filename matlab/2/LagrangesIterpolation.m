clc
clear all
x=input('enter x vector');
y=input('enter y vector');
xn=input('Enter value of xn: ');
n=length(x);
sum=0;
pr=1;
i=1;
j=1;
while i<=n
    while j<=n
        if i~=j
            pr=pr*((xn-x(j))/(x(i)-x(j)));
        end
        j=j+1;
    end
    sum=sum+y(i)*pr;
    i=i+1;
    j=1;
    pr=1;
end
sum
