import math


t=int(input())    
for i in range(t):
    n=int(input())
    print("1", end="")
    for i in range(2, int(math.sqrt(n))+1):
        c=0
        while n%i==0:
            c=c+1
            n=n/i 
        if c!=0:
            print(" * ", end="")
            print(i, end="^")  
            print(c, end="")
        if n==1:
            break
    if n!=1:
        print(" * {}^{}".format(int(n),1))
    else:
        print()
    
            