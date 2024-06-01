import math

def isPrime(a, b):
    a=int(a)
    b=int(b)
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    if a==1:
        return 'YES'
    else:
        return 'NO'

t=int(input())
for i in range(t):
    a=input()
    print(isPrime(a,a[::-1]))