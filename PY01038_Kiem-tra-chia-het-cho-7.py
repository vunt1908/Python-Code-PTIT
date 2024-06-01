def check(a):
    for i in range(1000):
        if a%7==0:
            return a
        tmp=int(str(a)[::-1])
        a+=tmp
    return -1

for t in range(int(input())):
    a=int(input())
    print(check(a))