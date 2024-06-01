import math

def checkPr(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1

n, m = [int(x) for x in input().split()]
a=[]
for i in range(n):
    a.append(list(int(i) for i in input().split()))
tmp=0
for i in range(n):
    for j in range(m):
        if checkPr(a[i][j]):
            tmp=max(tmp, a[i][j])
if tmp==0:
    print('NOT FOUND')
else:
    print(tmp)
    for i in range(n):
        for j in range(m):
            if checkPr(a[i][j]) and a[i][j]==tmp:
                print('Vi tri ['+str(i)+']['+str(j)+']')