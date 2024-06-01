s=input()
b={}
for i in range(int(len(s)/2)):
    tmp=int(s[0])*10 + int(s[1])
    if tmp in b:
        b[tmp]+=1
    else:
        b[tmp]=1
    s=s[2::]
for i in b:
    print(i, b[i])