import math

def check(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

n = int(input())
arr = [int(x) for x in input().split()]
tmp=[]
for x in arr:
    if check(x):
        tmp.append(x)
tmp.sort()
j=0
for i in range(n):
    if not check(arr[i]):
        print(arr[i], end=" ")
    else:
        print(tmp[j], end=" ")
        j+=1
print()