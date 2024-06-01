def check(s):
    if len(s) != 4:
        return False
    for i in s:
        if i.isdecimal():
            if int(i)<0 or int(i)>255:
                return False
        else:
            return False
    return True

for t in range(int(input())):
    if check(input().split('.')):
        print('YES')
    else:
        print('NO')