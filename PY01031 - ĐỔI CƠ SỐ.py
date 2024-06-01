for t in range(int(input())):
    sav="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n, b = [int(x) for x in input().split()]
    tmp=""
    while(n>0):
        x=n%b
        tmp=sav[x]+tmp
        n=int(n/b)
    print(tmp)
