for t in range(int(input())):
    s=input()
    tmp = ''
    for i in range(0,len(s), 2):
        tmp+=s[i] * int(s[i+1])
    print(tmp)