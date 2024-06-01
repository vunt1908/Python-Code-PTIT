import math


t=int(input())
for i in range(t):
    s=input()
    sum=0
    check=0
    for i in s:
        sum+=int(i)
    for i in range(1,len(s)):
        if abs(int(s[i])-int(s[i-1]))==2:
            check=1
    if check==1 and sum%10==0:
        print("YES")
    else :
        print("NO")