for t in range(int(input())):
    s=input()
    s=s+'v'
    tmp, sol=0, 0
    for i in range(1,len(s)):
        if s[i].isalpha():
            if i!=0 and s[i-1].isdigit(): sol=max(sol, tmp)
            tmp=0
        else: 
            tmp = tmp * 10 + int(s[i])
    print(sol)
        