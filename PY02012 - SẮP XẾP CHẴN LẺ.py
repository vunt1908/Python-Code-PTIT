import functools

def mykeycmp(a, b):
    if a<b:
        return 1
    else:
        return -1

arr=[]
arr_c=[]
arr_l=[]
n=int(input())
d=[0]*n
while True:
    x=[int(i) for i in input().split()]
    arr+=x
    if len(arr)==n: 
        break
for i in range(n):
    if arr[i]%2==1:
        arr_l.append(arr[i])
        d[i]=1
    else:
        arr_c.append(arr[i])
arr_c=sorted(arr_c)
arr_l=sorted(arr_l, key=functools.cmp_to_key(mykeycmp))
for i in range(n):
    if d[i]==1:
        print(arr_l[-1], end=" ")
        arr_l.pop()
    else:
        print(arr_c[-1], end=" ")
        arr_c.pop()
    

