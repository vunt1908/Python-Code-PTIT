import math


n=int(input())
arr = [int(i) for i in input().split()]
arr.sort()
for i in range(0, n-1):
    for j in range(i+1, n):
        if math.gcd(arr[i], arr[j])==1:
            print(str(arr[i])+ " " + str(arr[j]))
            #print()