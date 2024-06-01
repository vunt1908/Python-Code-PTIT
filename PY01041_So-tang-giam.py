def check(s):
    if len(s)<3:
        return 'NO'
    arr =list(int(i) for i in s)
    kt =True
    for i in range(1, len(arr)):
        if kt and arr[i] <= arr[i-1]:
            kt=False
        elif not kt and arr[i] >= arr[i-1]:
            return 'NO'
    return 'YES'
for t in range(int(input())):
    s=input()
    print(check(s))