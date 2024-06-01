n=int(input())
arr = [int(x) for x in input().split()]
for i in range(0, len(arr)-2):
    for j in range(i+1, len(arr)-1):
        if (arr[i]+arr[j])%2==0:
            arr.remove(arr[i])
            arr.remove(arr[j])
print(arr)