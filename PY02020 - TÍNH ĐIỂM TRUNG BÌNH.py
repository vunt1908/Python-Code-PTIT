n=int(input())
arr=[float(x) for x in input().split()]
tmp_max, tmp_min=max(arr), min(arr)
tmp=[]
for i in arr:
    if i!=tmp_max and i!=tmp_min:
        tmp.append(i)
print("{:.2f}".format(sum(tmp)/len(tmp)))