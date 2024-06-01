import math


n, x = [int(i) for i in input().split()]
b=[0]*10001

def prime():
    b[0]=b[1]=1
    for i in range(2, int(math.sqrt(10000))+1):
        if b[i]==0:
            for j in range(i*i, 10001, i):
                b[j]=1

prime()

arr=[0]
for i in range(10001):
    if b[i]==0:
        arr=arr+[i]
d=0
for i in range(n+1):
    x+=arr[d]
    print(x, end=" ")
    d+=1