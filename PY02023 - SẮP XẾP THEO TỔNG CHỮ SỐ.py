import functools

def sum(n):
    s=0
    while(n>0):
        s+=n%10
        n=int(n/10)
    return s

def mycmpkey(m, n):
    if sum(m) > sum(n):
        return 1
    elif sum(m)==sum(n):
        if m>n:
            return 1
        else: 
            return -1
    else:
        return -1

for t in range(int(input())):
    n=int(input())
    arr = [int(i) for i in input().split()]
    #c={}
    arr=sorted(arr, key=functools.cmp_to_key(mycmpkey))
    for i in arr:
        print(i, end=" ")
    print()
