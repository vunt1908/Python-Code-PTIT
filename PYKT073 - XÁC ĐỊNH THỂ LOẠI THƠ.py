n= int(input())
i=0
tmp=-1
count=0
m=[]
while i<n:
    s=input().split()
    if len(s) == 7 and (count==4 or tmp!=2):
        if count==4:
            count=0
        tmp=2
        m.append(tmp)
    elif (len(s)==6 or len(s)==8) and tmp!=1:
        tmp=1
        count=0
        m.append(tmp)
    if tmp==2:
        count+=1
    i+=1
print(len(m))
for i in m:
    print(i)