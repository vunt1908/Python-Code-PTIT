import antigravity
from operator import le


for t in range(int(input())):
    n=input()
    l, tmp, s=len(n), -1, '0'
    for i in range(l-2, -1, -1):
        if n[i] > n[i+1]:
            tmp=i
            break
    if tmp==-1:
        print(-1)
        continue
    tmp2=tmp+1
    for i in range(tmp+2, l):
        if n[i] > s and n[i] > n[tmp+1] and n[i] < n[tmp]:
            s=n[i]
            tmp2=i
    n=n[:tmp:] + n[tmp2] + n[tmp+1:tmp2:] + n[tmp] + n[tmp2+1::]
    if n[0]=='0':
        print(-1)
    else:
        print(n)
