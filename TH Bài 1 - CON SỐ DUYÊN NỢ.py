def check(s):
    if s[0]==s[len(s)-1]:
        return 'YES'
    return 'NO'
for t in range(int(input())):
    print(check(input()))
