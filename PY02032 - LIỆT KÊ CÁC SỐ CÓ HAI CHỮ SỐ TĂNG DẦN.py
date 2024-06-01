s=input()
tmp={}
for i in range(1, len(s), 2):
    tmp[int(s[i-1])*10+int(s[i])]= 1
for i in range(9, 100):
    if i in tmp:
        print(i, end=' ')