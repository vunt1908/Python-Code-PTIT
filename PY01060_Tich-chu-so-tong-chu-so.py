from re import A


for t in range(int(input())):
    a=list(int(x) for x in input())
    s, p= 0, 1
    for i in range(0, len(a), 2):
        if a[i]!=0:
            p*=a[i]
    for i in range(1, len(a), 2):
        s+=a[i]
    print(str(p) + " " + str(s))