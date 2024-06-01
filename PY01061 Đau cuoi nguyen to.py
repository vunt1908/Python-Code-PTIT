import math

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

for t in range(int(input())):
    a=list(int(x) for x in input())
    tmp1, tmp2=0, 0
    for i in range(0, 3):
        tmp1=tmp1*10+a[i]
    for i in range(len(a)-3, len(a), 1):
        tmp2=tmp2*10+a[i]
    if isPrime(tmp1) and isPrime(tmp2):
        print("YES")
    else:
        print("NO")