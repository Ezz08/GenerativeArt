from turtle import *
from colorsys import *

speed(0)
bgcolor("black")

hue = 0

for i in range(75):
    color(hsv_to_rgb(hue,1,1))
    hue+= 0.02
    left(1)
    forward(1)
    for j in range(3):
        left(2)
        circle(150)
    hideturtle()
done()         