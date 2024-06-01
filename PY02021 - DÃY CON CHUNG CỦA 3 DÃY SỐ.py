for t in range(int(input())):
    n, m, k = [int(x) for x in input().split()]
    arr1 = list(int(i) for i in input().split())
    arr2 = list(int(i) for i in input().split())
    arr3 = list(int(i) for i in input().split())
    i, j, z = 0, 0, 0
    check = False
    while i<n and j<m and z<k:
        if arr1[i] == arr2[j] and arr2[j]==arr3[z]:
            print(arr1[i], end=' ')
            check=True
            i+=1
            j+=1
            z+=1
            continue
        if arr1[i] < arr2[j] or arr1[i]<arr3[z]:
            i+=1
            continue
        if arr2[j] < arr3[z] or arr2[j] < arr1[i]:
            j+=1
            continue
        if arr3[z] < arr1[i] or arr3[z] < arr2[j]:
            z+=1
            continue
    if check==False:
        print('NO', end=' ')
    print() 