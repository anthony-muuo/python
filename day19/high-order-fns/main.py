from turtle import Turtle, Screen


tim = Turtle()


def move_forwards():
    tim.forward(10)

screen = Screen()
# listen tells the screen to lister for clicks ...
screen.listen()
# onkey a fn that takes a fn
screen.onkey(key='space', fun=move_forwards)

screen.exitonclick()

