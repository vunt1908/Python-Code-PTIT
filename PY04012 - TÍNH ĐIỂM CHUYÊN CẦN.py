m={}
t=int(input())
for i in range(t):
    id = input()
    ten=input()
    lop=input()
    m[id]=[ten, lop]
for i in range(t):
    id, diem= input().split()
    d=10
    for j in diem:
        if j=='m':
            d-=1
        elif j=='v':
            d-=2
    if d<0:
        d=0
    m[id]=m[id]+[d]
for i in m:
    print(i, end=' ')
    for j in m[i]:
        print(j, end=' ')
    if m[i][-1]==0:
        print('KDDK')
    else:
        print()
    