a=[ [2,4,1],
    [3,2,-2],
    [1,-1,1] ]
d=[3,-2,6]
n=3

for i in range(0,n):
    print(a,'         ||||         ',d)
    for k in range(i+1,n):
        f=a[k][i]/a[i][i]
        for j in range(0,n):
            a[k][j]=a[k][j]-f*a[i][j]
        d[k]=d[k]-f*d[i]


x=[]
for i in range (n,0,-1):
    i=i-1
    temp=d[i]
    print ('fot')
    if i<n-1 :
        for j in range(i+1,n):
            temp=temp-a[i][j]*x[2-j]
            print ('.')
    x.append(temp/a[i][i])
    print (x)

print('x=%f\n',x)
