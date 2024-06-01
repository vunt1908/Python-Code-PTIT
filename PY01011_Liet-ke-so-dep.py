def loading(a):
    if len(a) % 2 ==1 or a != a[::-1]:
        return False
    for i in a:
        if int(i) %2 != 0:
            return False
    return True

for t in range(int(input())):
    n=int(input())
    for i in range(22,n,2):
        if loading(str(i)):
            print(i, end=" ")
    print()