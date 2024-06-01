from cmath import sqrt
import math
from posixpath import split
from re import S


t=int(input())
# def USC(a, b):
#     if a==0 or b==0:
#         return a+b
#     else:
#         while a!=b:
#             if a>b:
#                 a=a-b
#             else:
#                 b=b-a
#     return a
def checkprimeNumber(n) :
    if n<2 :
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def sum(n) :
    s=0
    while n>0:
        s+=n%10
        n=int(n/10)
    return s
for i in range(t):
    a,b = [int(x) for x in input().split()]
    if checkprimeNumber(sum(math.gcd(a,b)))==True:
        print("YES")
    else:
        print("NO")