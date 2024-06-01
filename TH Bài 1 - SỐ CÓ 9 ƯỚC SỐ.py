n=int(input())
count, i = 0, 2
k=int(n**0.5)
arr=[i for i in range(k+1)]
while i*i<=k:
    if arr[i]==i:
        for j in range(i*i, k+1, i):
            if arr[j]==j:
                arr[j]=i
    i+=1
for i in range(2, k+1):
    tmp1=arr[i]
    tmp2=arr[i // arr[i]]
    if tmp1*tmp2==i and tmp2!=1 and tmp1!=tmp2:
        count+=1
    elif arr[i]==i:
        if i**8<=n:
            count+=1
print(count)