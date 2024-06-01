def solve(n):
    c, d=0, 0
    while n>0:
        tmp=n%10
        if tmp!=0 and tmp!=1 and tmp!=2:
            return False
        else:
            if tmp==2:
                c+=1
            n=int(n/10)
            d+=1
    if c> 1/2*d:
        return True
    return False

for t in range(int(input())):
    n=int(input())
    br=0
    for i in range(2, 9999999):
        if solve(i):
            br+=1
            if br == n+1:
                break
            print(i, end=" ")
    print()
