for t in range(int(input())):
    s=input()
    count=0
    tmp=""
    for i in s:
        if i.isdigit():
            count+=int(i)
        else:
            tmp+=i
    print(''.join(sorted(tmp)), count, sep="")