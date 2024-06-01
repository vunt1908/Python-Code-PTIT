f='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    n, b= [int(i) for i in input().split()]
    s=''
    while(n>0):
        tmp=n%b
        s=f[tmp]+s
        n=int(n/b)
    print(s)