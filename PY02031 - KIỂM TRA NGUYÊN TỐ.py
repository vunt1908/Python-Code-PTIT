import math

def isPrime(n):
    if n<2:
        return 0
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

n, m = [int(x) for x in input().split()]
#matrix=[[]]*n*m
for i in range(n):
    matrix = [int(x) for x in input().split()]
    for i in matrix:
        if isPrime(i):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
# for i in range(n):
#     for j in range(m):
#         if isPrime(matrix[i][j]):
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()
