import math


def check(a):
    if a<2:
        return False
    for i in range(2,(int)(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True

for t in range(int(input())):
    s=input()
    sum=0
    for i in s:
        sum+=int(i)
    if check(sum):
        print("YES")
    else:
        print("NO")