import math


def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def check(s):
    if not isPrime(len(s)):
        return 'NO'
    c=0
    for i in s:
        if isPrime(int(i)):
            c=c+1
    if c<=(len(s)-c):
        return 'NO'
    return 'YES'

for t in range(int(input())):
    print(check(input()))