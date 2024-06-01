import math


while True:
    count=0
    l, r, n = [int(x) for x in input().split()]
    if l==-1 or r==-1 or n==-1:
        break
    for i in range(l, r+1):
        for j in range(2, n+1):
            if math.gcd(i,j)==1:
                count+=1
    print(count)