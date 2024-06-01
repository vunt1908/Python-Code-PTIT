def luythua(a):
    if a==0:
        return 1
    return a*luythua(a-1)
s=1
n=int(input())
for i in range(2,n+1):
    s+=(1/luythua(i))
print(s)
