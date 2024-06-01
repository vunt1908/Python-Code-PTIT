from xml.dom import InuseAttributeErr


n=int(input())
sum=0
arr = [int(i) for i in input().split()]
for i in range(0, n-1):
    if arr[i]!=arr[i+1]:
        sum+=1
print(sum)