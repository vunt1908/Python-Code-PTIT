import math


def isPrime(a):
    a=int(a)
    if(a<2): 
        return False
    for i in range(2, int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True

for t in range(int(input())):
    s=input()
    tmp=0
    for i in range(len(s)-4, len(s), 1):
        tmp=tmp*10+int(s[i])
    if isPrime(tmp):
        print("YES")
    else:
        print("NO")
