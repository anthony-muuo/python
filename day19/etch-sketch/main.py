from turtle import Turtle, Screen


tim = Turtle()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(100)

def clockwise():
    tim.right(10)

def anti_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=clockwise)
screen.onkey(key='d', fun=anti_clockwise)
screen.onkey(key='c', fun=clear)


screen.exitonclick()

