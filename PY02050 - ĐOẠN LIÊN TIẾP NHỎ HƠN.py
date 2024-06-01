for t in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    tmp=[]
    for i in range(n):
        while len(tmp) > 0 and arr[tmp[-1]] <= arr[i]:
            tmp.pop()
        if len(tmp) ==0:
            print(i+1, end=" ")
        else:
            print(i-tmp[-1], end=" ")
        tmp.append(i)
    print()