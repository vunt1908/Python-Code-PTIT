n, m = [int(x) for x in input().split()]
a=[[0]]*n
Min, Max, check1, check2 = 10**6, 0, 0, 0
for i in range(n):
    a[i]=[int(x) for x in input().split()]
    Min=min(Min, min(a[i]))
    Max=max(Max, max(a[i]))
tmp=Max-Min
for i in range(n):
    for j in range(m):
        if tmp==a[i][j]:
            if check1==0:
                check2=1
                print(tmp)
                check1=1
            print("Vi tri [{}][{}]".format(i, j))
if check1==0:
    print("NOT FOUND")
               