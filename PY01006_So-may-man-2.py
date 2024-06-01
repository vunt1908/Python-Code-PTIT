def checkNum(s):
    for i in s:
        if i!='4' and i!='7':
            return False
    return True
t=int(input())
for i in range(t):
    s=input()
    if checkNum(s)==True:
        print("YES")
    else :
        print("NO")