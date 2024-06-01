arr=[]
for t in range(int(input())):
    s=input()+' '
    tmp=0
    #a=[]
    for i in range(len(s)):
        if s[i].isdigit(): 
            tmp=tmp*10+int(s[i])
        else:
            if s[i-1].isdigit():
                arr.append(tmp)
                tmp=0
for i in sorted(arr):
        print(i)