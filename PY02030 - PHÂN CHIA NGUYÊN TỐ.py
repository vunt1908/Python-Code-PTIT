import math

def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
a=list(int(x) for x in input().split())
dd={}
b=[]
for i in a:
    if i not in dd:
        dd[i]=1
        if len(b) == 0:
            b.append(i)
        else:
            b.append(i+b[-1])
res = -1
for i in range(0, len(b)):
    if check(b[i]) and check(b[-1]-b[i]):
        res=i
        break
if res==-1:
    print('NOT FOUND')
else:
    print(res)