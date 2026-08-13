import turtle
import pandas # type: ignore




screen = turtle.Screen()
screen.title("U.S States Game")
image= "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# stack overflow code... get the coordinates of where the mouse is the x and y,,,
# helps get the coordinate of each states placements

# def get_mouse_click_cor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_cor)
# makes the screen not to exit after taping to get the coordinates
# turtle.mainloop()

correct_guesses = []
score = 0

data = pandas.read_csv("./50_states.csv")

while score < 50:
    state = screen.textinput(title=f"{score} / 50 States correct",  prompt="What's another states name? ").title()
    # save the unguessed states in a new csv called states_to_learn.csv
    if state == 'Exit':
    #     missing_states = []
    #     for each_state in data.state.to_list():
    #         if each_state not in correct_guesses:
    #             # mean it is missing
    #             missing_states.append(each_state)

    # now fix above with list comprehension learnt in day 26
        missing_states = [each_state for each_state in data.state.to_list() if each_state not in correct_guesses]

        # print(missing_states)
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("states_to_learn.csv")
        break

    # check if state is among the all 50 states in csv
    if state in data.state.values and state not in correct_guesses:
        # next here is to locate the x and y in the scrren
        # write correct answers to the map
        state_data = data[data.state == state]
        x = state_data.x.item()
        y= state_data.y.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(state)
        correct_guesses.append(state)
        score+= 1

