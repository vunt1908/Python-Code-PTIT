for t in range(int(input())):
    s=input()
    sum=0
    for i in s:
        sum+=int(i)
    check=0
    for i in str(sum):
        check+=int(i)
    if check%3==0:
        print("YES")
    else:
        print("NO")