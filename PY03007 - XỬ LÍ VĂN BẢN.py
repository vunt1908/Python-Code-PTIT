import re
s=''
while True:
    try:
        s+=input()
    except EOFError:
        break
s = re.split('[.?!]',s)
for i in s:
    if len(i)>0:
        tmp=re.sub('\s+',' ',i.strip())
        print(tmp[0].upper() + tmp[1:].lower())