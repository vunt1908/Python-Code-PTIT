from audioop import mul
import functools
import re


def multiplication(n):
    p=1
    while(n>0):
        p*=n%10
        n=int(n/10)
    return p

def mycmpkey(m, n):
    if multiplication(m)>multiplication(n):
        return 1
    elif multiplication(m)==multiplication(n):
        if m>n:
            return 1
        else:
            return -1
    else:
        return -1

for t in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr=sorted(arr, key=functools.cmp_to_key(mycmpkey))
    for i in arr:
        print(i, end= " ")
    print()
