n = int(input())
chan = []
le = []
ans = []
count=0
while count < n:
    arr = [int(x) for x in input().split()]
    for i in arr:
        count+=1
        if i%2==0:
            chan.append(i)
        else:
            le.append(i)
    ans.extend(arr)
le.sort(reverse=True)
chan.sort()
i, j= 0, 0
for x in ans:
    if x%2!=0:
        print(le[i], end=' ')
        i+=1
    else:
        print(chan[j], end=' ')
        j+=1
print()