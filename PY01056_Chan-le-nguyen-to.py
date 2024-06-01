import math
import re


def isPrime(a):
    if a<2:
        return False
    for i in range(2, int(math.sqrt(a)+1)):
        if n%i==0:
            return False
    return True

def check(s):
    l=len(s)
    for i in range(l):
        if i%2!= int(s[i])%2:
            return 'NO'
    n=sum(int(x) for x in s)
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return 'NO'
    if n>1:
        return 'YES'
    else:
        return 'NO'
        
for t in range(int(input())):
    s=input()
    print(check(s))