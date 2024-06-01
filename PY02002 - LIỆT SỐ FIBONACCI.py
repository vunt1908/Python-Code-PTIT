arr = [0, 1, 1]
f1=1
f2=1
for i in range(3, 93):
    fn=f1+f2
    arr += [fn]
    f1=f2
    f2=fn
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    for i in range(a, b+1):
        print(arr[i], end= " ")
    print()