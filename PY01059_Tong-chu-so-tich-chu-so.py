for t in range(int(input())):
    n=list(int(x) for x in input())
    s, p = 0, 0
    for i in range(len(n)):
        if i%2==0:
            s+=n[i]
        else:
            if n[i]!=0:
                if p==0:
                    p=n[i]
                else:
                    p*=n[i]
    print(str(s) + " " + str(p))