count=0
tmp=[0]*42
while True:
    arr=[int(x) for x in input().split()]
    count+=len(arr)
    s=0
    for i in arr:
        tmp[i%42]=1
    if count==10:
        break
for i in tmp:
    if i>0:
        s+=1
print(s)

