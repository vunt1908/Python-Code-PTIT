n, m = [int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
da={}
db={}
for x in a:
    da[x]=1
for x in b:
    db[x]=1
if da==db:
    print("YES")
else:
    print("NO")