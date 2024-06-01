for t in range(int(input())):
    n=int(input())
    a=list(int(x) for x in input().split())
    b=list(int(x) for x in input().split())
    a.sort()
    b.sort()
    check='YES'
    for i in range(0,n):
        if a[i] > b[i]:
            check='NO'
            break
    print(check)