import math
from operator import le


n=int(input())
arr = [int(i) for i in input().split()]
arr.sort()
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if math.gcd(arr[i], arr[j])==1:
            print(arr[i], arr[j])