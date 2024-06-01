for t in range(int(input())):
    s=input() 
    l=len(s)
    tmp=1
    for i in range(1,l):
        if s[i]!=s[i-1]:
            print(tmp, end='')
            print(s[i-1], end='')
            tmp=1
        else: tmp+=1
    print(tmp, end='')
    print(s[l-1])
