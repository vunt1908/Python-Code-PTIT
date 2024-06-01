class HCN:
    def __init__(self, d, r, c):
        self.d = d
        self.r = r
        self.c = c
    def cv(self):
        return (self.d + self.r)*2
    def dt(self):
        return self.d*self.r
    def color(self):
        return self.c.title()
    def check(self):
        return self.d > 0 and self.r > 0

arr = input().strip().split()
r = HCN(int(arr[0]), int(arr[1]), arr[2])
if r.check():
    print(r.cv(), r.dt(), r.color())
else:
    print('INVALID')