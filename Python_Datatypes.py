"""
Python Data Types:
    Text Type: str
    Number Type: int, float, complex
    Sequence Type: list, tuple, range
    Mapping Type: dict
    Set Type: set, frozenset
    Boolean Type: bool
    Binary Type: bytes, bytearray, memoryview
"""

from wsgiref.validate import PartialIteratorWrapper


x = ["One", "Two", "Three"]
print(x)
print(type(x))

#Python Number
x=float(1)
y=int(1.8)      #convert
z=complex(1)
print(x,y,z)


#Python String
s = "Nguyen Tran Vu"
print(s)
print(len(s))
print(s[0])

for x in "string":         #fio(i,0,n)
    print(x,end='')     
print()
a="""Họ và tên: Nguyễn Trần Vũ
    Mã SV
    Lớp 
    Ngành Công nghệ thông tin
    Học viện Công nghệ bưu chính viễn thông"""
print(a)
if "Nguyễn Trần Vũ" in a:
    print("Yes, it's in string a")

b="Nguyen Tran Vu"
print(b[0:6])   #Nguyen
print(b[:6])    #Nguyen
print(b[7:])    #Tran Vu
print(b[-5:-1])     #an V

print(b.upper())
print(b.lower())
print(b.strip())     #remove Whilespace ở 2 đầu
print(b.split(","))    #tách thành các chuỗi khi gặp dấu ","

b.upper()            #lưu ý 
print(b) 
b=b.upper()
print(b)


age = 20
school = "PTIT" 
province = "Ha Noi"
txt = "My name is Nguyen Tran Vu, I am {}, I am study in {} in {}"
print(txt.format(age,school,province))

list1 = ["a", "b", "c"]
for x in list1:
    print(x, end='')
print()
for i in range(len(list1)):
    print(list1[i], end='')
print()
[print(x,end='') for x in list1]
print()

