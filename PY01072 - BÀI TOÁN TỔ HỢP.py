n, k =[int(i) for i in input().split()]
tmp={}
arr=[int(x) for x in input().split()]
b=[0]*(k+1)
for i in arr:
    tmp[i]=1
arr=sorted(list(tmp))
n=len(arr)

def Try(j):
    if j==k:
        for i in range(1,k+1):
            print(arr[b[i]-1], end=" ")
        print()
        return
    for i in range(b[j]+1, n+1):
        b[j+1]=i
        Try(j+1)
Try(0)