import queue

while True:
    n=int(input())
    if n==0:
        break
    q=queue.Queue()
    tmp={}
    q.put(n)
    while not(q.empty()):
        k=q.get()
        tmp[k]=1
        if k==1:
            break
        if k%2==0:
            q.put(int(k/2))
        else:
            q.put(k*3+1)
    print(len(tmp))