from itertools import count
import math
from operator import le


def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n=int(input())
arr = [int(x) for x in input().split()]
#prime_arr=[]
c={}
for i in arr:
    if isPrime(i)==True:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
for i in c:
    print(i, c[i])

