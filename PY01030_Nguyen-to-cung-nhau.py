def check(a, b):
    a=int(a)
    b=int(b)
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    if a==1:
        return True
    else:
        return False

n, k = [int(x) for x in input().split()]
startNum=pow(10, k-1)
endNum=pow(10,k)-1
c=0
for i in range(startNum,endNum):
    if check(n, i):
        c=c+1
        print(i, end=" ")
        if c%10==0:
            print()
