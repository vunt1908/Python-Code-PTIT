t = int(input())
import math
def loading(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
for i in range(t):
    n=int(input())
    tmp =0
    for i in range(1,n):
        if math.gcd(i, n) == 1:tmp+=1
    if loading(tmp) ==True:
        print("YES")
    else:
        print("NO")