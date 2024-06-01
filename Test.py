def out(x):
    tmp={}
    for i in x:
        if i not in tmp:
            tmp[i]=1
    return sorted(tmp.keys())

a=list(int(x) for x in input().split())
a=out(a)
for i in a:
    print(i, end=" ")