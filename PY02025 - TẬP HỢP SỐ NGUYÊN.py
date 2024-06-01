n, m = [int(x) for x in input().split()]
arr1= list(int(x) for x in input().split())
arr2= list(int(x) for x in input().split())

def out(x):
    tmp={}
    for i in x:
        if i not in tmp:
            tmp[i]=1
    return sorted(tmp.keys())

arr1 = out(arr1)
arr2 = out(arr2)

ans1=[]
ans2=[]
ans3=[]

for i in arr1:
    if i in arr2:
        ans1.append(i)
for i in arr1:
    if i not in arr2:
        ans2.append(i)
for i in arr2:
    if i not in arr1:
        ans3.append(i)

for i in ans1:
    print(i, end=" ")
print()
for i in ans2:
    print(i, end=" ")
print()
for i in ans3:
    print(i, end=" ")
print()

