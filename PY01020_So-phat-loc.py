t=int(input())
for i in range(t):
    s=input()
    if int(s[len(s)-2])==8 and int(s[len(s)-1])==6:
        print("YES")
    else :
        print("NO")