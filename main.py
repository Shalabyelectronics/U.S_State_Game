import pandas as pd
import turtle as tr

screen = tr.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
user = tr.Turtle()
user.hideturtle()
user.penup()
state_data = pd.read_csv("50_states.csv")
states_list = state_data.state.to_list()
gussed_states = []
with open("user_progress.csv") as user_progress:
    for line in user_progress.readlines():
        gussed_states.append(line.strip())

while len(gussed_states) < 50:
    user_answer = screen.textinput(title=f"You guessed {len(gussed_states)}/50", prompt="Write any of the state names "
                                                                                 "correctly.").title()
    if user_answer in states_list:
        state_row = state_data[state_data.state == user_answer]
        user.goto(int(state_row.x), int(state_row.y))
        user.write(user_answer, move=False, align="center", font=("Verdana", 10, "normal"))
        gussed_states.append(user_answer)
    elif user_answer.lower() == "exit":
        with open("user_progress.csv", mode="a") as user_progress:
            for state in gussed_states:
                user_progress.write(f"{state}\n")

        with open("user_progress.csv") as user_progress:
            print("Ohio" in user_progress)




screen.exitonclick()
