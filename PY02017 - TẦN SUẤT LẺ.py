for t in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]%2==1:
            print(i)
            break