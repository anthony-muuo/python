from turtle import Turtle

class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.pensize(3)

        self.left(90)
        self.penup()
        self.goto(0,300)
        self.setheading(270)

        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
    
