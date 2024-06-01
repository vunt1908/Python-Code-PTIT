n=int(input())
count=0
arr = [int(i) for i in input().split()]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            count+=1
print(count)
