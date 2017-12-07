# -*- coding: UTF-8 -*-


#$ header function matmat(*double [:,:], *double [:,:], *double [:,:]) results(*double [:,:], int)
def matmat(a,b,d):
    nm = shape(a)
    mp = shape(b)

    n = nm[0]
    m = nm[1]
    p = mp[1]

    for i in range(0, n):
        for j in range(0, m):
            for k in range(0, p):
                c[i,j] = d[i,j] + a[i,k]*b[k,j]

    return c, n

n = 3
m = 4
p = 3

a = zeros((n,m), double)
b = zeros((m,p), double)

for i in range(0, n):
    for j in range(0, m):
        a[i,j] = (i-j)*1.0

for i in range(0, m):
    for j in range(0, p):
        b[i,j] = (i+j)*1.0

print(a)
print(b)

c = zeros((n,p), double)
c, nn = matmat(a,b,c)
print(c)
