import functools

class SinhVien:
    def __init__(self, Name, AC, Submit):
        self.Name = Name
        self.AC = AC
        self.Submit = Submit

def cmp(sv1, sv2):
    if sv1.AC < sv2.AC:
        return 1
    elif sv1.AC == sv2.AC:
        if sv1.Submit > sv2.Submit:
            return 1
        elif sv1.Submit == sv2.Submit:
            if sv1.Name > sv2.Name:
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1

arr = []
for t in range(int(input())):
    Name=input()
    AC, Submit = [int(x) for x in input().split()]
    arr.append(SinhVien(Name, AC, Submit))
arr = sorted(arr, key=functools.cmp_to_key(cmp))
for i in arr:
    print(i.Name, i.AC, i.Submit)