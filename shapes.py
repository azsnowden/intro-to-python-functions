from turtle import *
#equilateral
def triangle(size, fill, color):
    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(50)
    left(120)

#square
def square():
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

#pentagon
def pentagon():
    forward(150)
    left(72)
    forward(150)
    left(72)
    forward(150)
    left(72)
    forward(150)
    left(72)
    forward(150)
    left(72)

#hexagon
def hexagon():
    forward(150)
    left(60)
    forward(150)
    left(60)
    forward(150)
    left(60)
    forward(150)
    left(60)
    forward(150)
    left(60)
    forward(150)
    left(60)

#star
def star():
    for i in range(5):
        forward(100)
        right(144)

#circle
def circle():
    for x in range(360):
        forward(1)
        right(1)
