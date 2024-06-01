tmp={}
for t in range(int(input())):
    s1=input()
    s2=input()
    s3=input()
    tmp[s1]=[s2, s3]
for i in sorted(tmp):
    print(i + " " + tmp[i][0] + " " + tmp[i][1])
