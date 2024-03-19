import turtle
import math
import random

t = turtle.Turtle()
t.speed(100)

# t.color("red")
# for i in range(8):
#     t.fd(200)
#     t.left(135)
#     t.fd(200)

t.color("red")

for i in range(2000):
    t.forward(10)
    t.left(math.sin(i/10)*25)
    t.left(random.randrange(10,20,1))


    






turtle.done()