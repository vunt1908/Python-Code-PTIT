for t in range(int(input())):
    n=int(input())
    arr = [int(i) for i in input().split()]
    count={}
    c_max=0
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in arr:
        if count[i] > c_max:
            c_max=count[i]
            tmp=i
    if c_max > n/2:
        print(tmp)
    else:
        print("NO")
