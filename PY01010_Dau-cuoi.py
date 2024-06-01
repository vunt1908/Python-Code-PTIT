t=int(input())
def checkNum(s):
    l=len(s)
    if int(s[0])!=int(s[l-2]) or int(s[1])!=int(s[l-1]) :
        return False
    return True
for i in range(t):
    s=input()
    if checkNum(s) == True :
        print("YES")
    else :
        print("NO")
