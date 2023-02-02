import pandas as pd
import turtle

screen = turtle.Screen()  # Initialize Turtle for Screen
screen.title("U.S. States Game")  # screen title

# Getting the background to be display assign image
image = "blank_states_img.gif"  # a blank image of the US
screen.addshape(image)
turtle.shape(image)

# DATA
csv_data = pd.read_csv("50_states.csv")
all_states = csv_data.state.to_list()

# Asking user for answer (aka a State)
# First we check to see how many states the User has guessed
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Checking if answer equals a string
    if answer_state == "Exit":

        # return missing states
        # missing_states = []
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    # Checking if answer provided is in the list all_states
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = csv_data[csv_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.state.item())
        guessed_states.append(answer_state)


screen.exitonclick()  # To secure screen doesn't disappear

