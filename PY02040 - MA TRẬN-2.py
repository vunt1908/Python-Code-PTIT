n=int(input())
# matrix=[]
# for i in range(n):
#     arr=[]
#     for j in range(n):
#         arr.append(int(input()))
#     matrix.append(arr)
# matrix = [[int(input()) for x in range(n)] for y in range(n)]
matrix = [[]]*n
for i in range(n):
    matrix[i]=[int(x) for x in input().split()]
k=int(input())
sum_1, sum_2=0, 0
for i in range(n):
    for j in range(n):
        if i> n-j-1:
            sum_1+=matrix[i][j]
        if i< n-j-1:
            sum_2+=matrix[i][j]
distan = abs(sum_1-sum_2)
if distan <=k:
    print("YES")
else:
    print("NO")
print(distan)
