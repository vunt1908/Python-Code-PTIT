def check(s):
    for i in s:
        if i < '0' or i > '2':
            return False
    return True

for t in range(int(input())):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")
