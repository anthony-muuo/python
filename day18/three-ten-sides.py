from turtle import *
import random


tim = Turtle()
colours = [
    "red",
    "blue",
    "magenta",
    "orange",
    "purple",
    "deep pink",
    "dodger blue",
    "lime green",
    "gold",
    "cyan"
]


def draw_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        forward(100)
        right(angle)

for sides in range(3, 11):
    color(random.choice(colours))
    draw_shapes(sides)

screen = Screen()

screen.exitonclick()