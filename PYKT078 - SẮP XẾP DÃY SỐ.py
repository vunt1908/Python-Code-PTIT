for t in range(int(input())):
    n, m = [int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    b0= []
    l0= []
    Max = max(arr)
    for i in range(n):
        if arr[i]==Max:
            arr.insert(i, m)
            break
    for i in arr:
        if i<0:
            b0.append(i)
        else:
            l0.append(i)
    # b0.sort()
    # l0.sort()
    for i in b0:
        print(i, end=" ")
    for i in l0:
        print(i, end=" ")
    # arr.append(m)
    # arr.sort()
    # for i in range(len(arr)):
    #     print(arr[i], end=" ")
    print()