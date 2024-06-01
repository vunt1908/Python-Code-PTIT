def loading(s):
    sum=0
    for i in s:
        sum+=ord(i)-ord("0")
    return str(sum)

s=input()
d=0
while(len(s)>1):
    s=loading(s)
    d+=1
print(d)
