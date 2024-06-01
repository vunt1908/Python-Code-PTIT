while True:
    arr= [int(i) for i in input().split()]
    if arr== [0, 0, 0, 0]:
        break
    for i in range(0, 999999):
        if arr[0]==arr[1] and arr[1]==arr[2] and arr[2]==arr[3]:
            print(i)
            break
        tmp=arr[0]
        arr[0]=abs(arr[0]-arr[1])
        arr[1]=abs(arr[1]-arr[2])
        arr[2]=abs(arr[2]-arr[3])
        arr[3]=abs(arr[3]-tmp)
