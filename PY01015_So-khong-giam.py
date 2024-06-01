t=int(input())
for i in range(t):
    s=input()
    check=1
    for i in range(0, len(s)-2):
        if s[i]>s[i+1] :
            check=0
    if check==1:
        print("YES")
    else:
        print("NO")