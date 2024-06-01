for t in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    l=min(arr)
    r=max(arr)
    arr.sort()
    cnt={}
    d=0
    for i in arr:
        cnt[i]=1
    for i in range(l,r):
        if not(i in cnt):
            d+=1
    print(d)