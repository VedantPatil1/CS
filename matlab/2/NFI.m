clc
clear all
x=input('enter x vector');
y=input('enter y vector');
xn=input('Enter value of xn: ');
n=length(x);
for j=1:n-1
    for i=1:n-j
        if j==1
            del(i,j)=y(i+1)-y(i);                % for del 1
        else del(i,j)=del(i+1,j-1)-del(i,j-1);    % Remaining del
        end
    end
end
del
h=x(2)-x(1);
u=(xn-x(1))/h;
term=0;
for j=1:n-1
    mult=1;
    for k=1:j
        mult=mult*(u-(k-1));
    end
    term=term+del(1,j)*mult/factorial(j);
end
yn=y(1)+term
 
