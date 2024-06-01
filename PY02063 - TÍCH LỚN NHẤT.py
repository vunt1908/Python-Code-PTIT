n=int(input())
a=list(int(x) for x in input().split())
a.sort()

tmp1=a[0]*a[1]
tmp2=a[-1]*a[-2]
tmp3=a[0]*a[1]*a[-1]
tmp4=a[-1]*a[-2]*a[3]

print(max(tmp1, tmp2, tmp3, tmp4))