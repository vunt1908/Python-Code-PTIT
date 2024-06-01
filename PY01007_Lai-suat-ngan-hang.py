import math
t=int(input())
for i in range(t):
    n, x, m = [float(x) for x in input().split()]
    x /= 100
    tmp = math.log(m/n, 1+x)
    if tmp != int(tmp) :
        tmp = tmp + 1
    print(int(tmp))