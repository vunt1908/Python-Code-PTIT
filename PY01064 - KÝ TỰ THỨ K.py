def loading(n, k):
    if k==2**(n-1):
        return n
    if k>2**(n-1):
        return loading(n-1, k-2**(n-1))
    return loading(n-1, k)

for t in range(int(input())):
    n, k = [int(x) for x in input().split()]
    print(chr(loading(n, k) + ord('A')-1))