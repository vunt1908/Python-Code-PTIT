import math

class PS:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def Loading(self):
        tmp=math.gcd(self.a, self.b)
        self.a=int(self.a/tmp)
        self.b=int(self.b/tmp)
        print(self.a, "/", self.b, sep="")

a, b = [int(x) for x in input().split()]
t=PS(a,b)
t.Loading()
