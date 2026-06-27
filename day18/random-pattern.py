# aliasing method
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    red = random.randint(0,255)
    green= random.randint(0, 255)
    blue = random.randint(0, 255)
    colours = (red, green, blue)
    print(f"the color choosen is, {colours}")
    return colours

# 0 for east, 90 for north,, south and west.. 
direction = [0, 90 , 180, 270]

tim.pensize(12)
tim.speed(0)

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))


screen = t.Screen()

screen.exitonclick()