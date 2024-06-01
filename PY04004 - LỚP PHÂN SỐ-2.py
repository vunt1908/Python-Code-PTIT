import math

# class PS:
#     def __init__(self, a, b, c, d):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#     def Loading(self):
#         BCNN = math.lcm(self.b, self.d)
#         ts = a*(BCNN/self.b) + c*(BCNN/self.d)
#         UC = math.gcd(BCNN, ts)
#         ts=ts/UC
#         BCNN /= UC
#         print(ts, "/", BCNN, sep=" ")
a1, a2, a3, a4 = [int(x) for x in input().split()]
x = a1*a4 + a2*a3
y = a2*a4
print(str(x//math.gcd(x, y)) + '/' + str(y//math.gcd(x, y)))
