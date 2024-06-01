while True:
    n=int(input())
    if n==0: 
        break
    # for i in range(n-1):
    #     a=[int(x) for x in input().split()]
    #     arr=list(int(x) for x in a)
    # arr=[int(x) for x in input().split()]
    # arr=sorted(arr)
    # d=0
    # for i in range(1, len(arr)):
    #     if arr[0]!=arr[i]:
    #         d=1
    #         break
    # if d==0:
    #     print("BANG NHAU")
    # else:
    #     print(arr[0], end=" ")
    #     print(arr[len(arr)-1])
    arr=[0]*n
    for i in range(n):
        arr[i]=int(input())
    if min(arr)==max(arr):
        print("BANG NHAU")
    else:
        print(min(arr), end=" ")
        print(max(arr))