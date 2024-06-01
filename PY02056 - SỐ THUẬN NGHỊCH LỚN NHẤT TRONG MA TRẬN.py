import math

def check(a):
    if a != a[::-1] or len(a)<2:
        return False
    return True

n, m = [int(x) for x in input().split()]
a=[]
for i in range(n):
    a.append(list(int(i) for i in input().split()))
tmp=0
for i in range(n):
    for j in range(m):
        if check(str(a[i][j])):
            tmp=max(tmp, a[i][j])
if tmp==0:
    print('NOT FOUND')
else:
    print(tmp)
    for i in range(n):
        for j in range(m):
            if check(str(a[i][j])) and a[i][j]==tmp:
                print('Vi tri [' + str(i) + '][' + str(j) + ']')