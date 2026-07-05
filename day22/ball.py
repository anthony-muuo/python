from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # move speed
        self.accelerate_ball = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move      
        new_y = self.ycor() + self.y_move       
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        # here if the ymove is > 300 to change and - and viceversa to -300 height
        self.y_move *= -1
    
    def bounce_x(self):
        # here if the ymove is > 300 to change and - and viceversa to -300 height
        self.x_move *= -1
        self.accelerate_ball *= 0.9

    def reset_position(self):
        self.goto(0,0)
        # now go to others players direction
        self.bounce_x()
        self.accelerate_ball = 0.1