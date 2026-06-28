from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

colors = ["red", "blue", "yellow", "green", "purple", "orange"]
all_turteles: list[Turtle] = []
user_prediction = screen.textinput(title="Make a prediction", prompt="Enter color to predict the winner in the race")

# create the turtles with the colors their axis
for index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(y=100 - (30 * index), x = -230)
    all_turteles.append(new_turtle)

if user_prediction:
    is_race_on = True

# forward .. move it forward a couple of times
while is_race_on:
    for turtle in all_turteles:
        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)
        # check winning color
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_prediction:
                print(f"You win!!. The {winning_color} turtle won")
            else:
                print(f"You lost! The {winning_color} turtle won")
    
  
screen.exitonclick()