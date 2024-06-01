def re_price(s, n):
    if s=="Xe_con":
        if n=="5": 
            return 10000
        else:
            return 15000
    if s=="Xe_khach":
        if n=="29":
            return 50000
        else:
            return 70000
    if s=="Xe_tai":
        return 20000

tmp={}
for t in range(int(input())):
    s=input().split()
    if s[3]=='IN':
        if s[4] not in tmp:
            tmp[s[4]]=re_price(s[1], s[2])
        else:
            tmp[s[4]]+=re_price(s[1], s[2])
tmp=sorted(tmp.items(), key=lambda x: x[0])
for i in tmp:
    print(str(i[0]) + ":", i[1])

