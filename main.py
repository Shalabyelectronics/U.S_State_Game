import pandas as pd
import turtle as tr

screen = tr.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
user = tr.Turtle()
user.hideturtle()
user.penup()
state_count = 0
state_data = pd.read_csv("50_states.csv")
states_list = state_data.state.to_list()
print(states_list)
while state_count < len(state_data.state) - 1:
    user_answer = screen.textinput(title=f"You guessed {state_count}/50", prompt="Write any of the state names "
                                                                                 "correctly.").title()
    if user_answer in states_list:
        state_row = state_data[state_data.state == user_answer]
        state_x = state_row.iloc[0, 1]
        state_y = state_row.iloc[0, 2]
        user.goto(state_x, state_y)
        user.write(user_answer, move=False, align="center", font=("Verdana", 10, "normal"))
        state_count += 1


screen.exitonclick()
