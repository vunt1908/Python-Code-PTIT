s=input()
h=0
t=0
for x in s:
    if x>='a' and x<='z':
        t=t+1
    if x>='A' and x<='Z':
        h=h+1
if h>t:
    print(s.upper())
else:
    print(s.lower())