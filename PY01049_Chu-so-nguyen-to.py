import math


def check(a):
    if a<2:
        return False
    for i in range(2, (int)(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True

for t in range(int(input())):
    s=input()
    c=0
    for i in s:
        if check(int(i)):
            c=c+1
    if check(len(s)) and c>(len(s)-c):
        print("YES")
    else:
        print("NO")
