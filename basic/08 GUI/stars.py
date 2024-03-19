import turtle
import math
import random

t = turtle.Turtle()
t.speed(100)
t.screen.bgcolor("#994444")


# for i in range(5):
#     t.fd(10)
#     t.left(216)

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.fd(size)
            star(turtle, size/2)
            turtle.left(216)

star(t, 200)







    






turtle.done()