def check(a):
    if a != a[::-1] or len(a)==1:
        return False
    return True

for t in range(int(input())):
    s=input()
    sum=0
    for i in s:
        sum+=int(i)
    if check((str)(sum)):
        print("YES")
    else:
        print("NO")
    