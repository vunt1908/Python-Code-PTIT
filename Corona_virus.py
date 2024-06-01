from turtle import *
speed(20)
color('blue')
bgcolor('white')
i=200
while True:
    left(i)
    forward(i*2)
    i-=1
    if i==0:
        break
end_fill()
done()