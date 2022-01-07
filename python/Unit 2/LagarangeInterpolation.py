x = [0,1,2,5]
y = [2,3,12,147]

xn = 1.5
n = len(x)

yn = 0
for i in range(n):
    num = 1
    deno = 1
    for j in range(n):
        if j!=i:
            num = num*(xn-x[j])
            deno = deno*(x[i]-x[j])
    yn = yn + ((num/deno)*y[i])

print (yn)