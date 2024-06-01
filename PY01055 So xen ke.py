def check(s):
    if len(s)%2==0 or int(s[0])==int(s[1]):
        return 'NO'
    for i in range(2, len(s), 2):
        if int(s[0])!=int(s[i]):
            return F'NO'
    return 'YES'

for t in range(int(input())):
    print(check(input()))