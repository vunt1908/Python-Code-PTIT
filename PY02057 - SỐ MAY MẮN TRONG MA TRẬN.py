n, m = [int(x) for x in input().split()]
a=[]
for i in range(n):
    a.append(list(int(i) for i in input().split()))
minn=99999999
maxx=0
for i in range(n):
    for j in range(m):
        maxx=max(maxx, a[i][j])
        minn=min(minn, a[i][j])
tmp=maxx-minn
check=False
for i in range(n):
        for j in range(m):
            if a[i][j]==tmp:
                if check==False:
                    print(a[i][j])
                print('Vi tri [' + str(i) + '][' + str(j) + ']')
                check=True
if check==False:
    print('NOT FOUND')
    