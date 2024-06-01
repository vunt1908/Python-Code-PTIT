for t in range(int(input())):
    n=int(input())
    arr1=[int(x) for x in input().split()]
    arr2=[int(x) for x in input().split()]
    arr1.sort()
    arr2.sort()
    check = 'YES'
    for i in range(0,n):
        if arr1[i] > arr2[i]:
            check='NO'
            break
    print(check)
    