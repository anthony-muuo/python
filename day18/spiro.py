import turtle as t
import random

# drawing a circle
timmy = t.Turtle()
t.colormode(255)



def random_color():
    red = random.randint(0,255)
    green= random.randint(0, 255)
    blue = random.randint(0, 255)
    colours = (red, green, blue)
    return colours

timmy.speed(0)

def draw_spiro(times_to_draw):
    for i in range(int(360 / times_to_draw)):
        timmy.color(random_color())
        timmy.circle(100)
        current_position = timmy.heading()
        timmy.setheading(current_position + times_to_draw)
    
draw_spiro(15)

screen = t.Screen()
screen.exitonclick()