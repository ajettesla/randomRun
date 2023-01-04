import random
import turtle
from turtle import *

timmy = Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]
timmy.speed("fastest")

for i in range(300):
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    timmy.pencolor(r, g, b)
    timmy.pensize(15)
    timmy.setheading(random.choice(directions))
    timmy.forward(random.randint(50, 80))







screen = Screen()
screen.title("Random Walk")
screen.exitonclick()