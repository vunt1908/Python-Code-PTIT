for t in range(int(input())):
    s=input()
    s=s+'v'
    tmp=0
    sol=10**20
    for i in range(len(s)):
        if s[i].isalpha():
            if i!=0 and s[i-1].isdigit(): sol=min(sol,tmp)
            tmp=0
        else: 
            tmp = tmp * 10 + int(s[i])
    print(sol)
        