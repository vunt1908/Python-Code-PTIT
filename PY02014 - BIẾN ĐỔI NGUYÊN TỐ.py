import math

def checkPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return n>1
    
n=int(input())
a=[int(x) for x in input().split()]
