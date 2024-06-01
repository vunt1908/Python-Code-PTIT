n=int(input())
arr = [int(i) for i in input().split()]
arr.sort()
for i in range(1, 30001):
    if not(i in arr):
        print(i)
        break