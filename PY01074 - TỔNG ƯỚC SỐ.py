def loading(n):
    sum=0
    for i in range(2, n+1):
        while(n%i==0):
            sum+=i
            n/=i
        if n==1:
            break
    return sum

s=0
arr=[int(x) for x in input().split()]
for i in range(1,len(arr)):
    s+=loading(arr[i])
print(s)
