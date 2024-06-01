P="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    nhap=input()
    if nhap=="0": break
    k, s=nhap.split()
    k=int(k)
    out=""
    for i in s:
        x=0
        for j in P:
            if i==j:
                break
            x+=1
        x=(x+k)%28
        out=P[x]+out
    print(out)