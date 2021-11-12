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
guessed_states = []
with open("user_progress.csv") as user_progress:
    for line in user_progress.readlines():
        guessed_states.append(line.strip())


def locate_states_progress():
    if len(guessed_states) > 0:
        for state_saved in guessed_states:
            state_row_data = state_data[state_data.state == state_saved]
            user.goto(int(state_row_data.x), int(state_row_data.y))
            user.write(state_saved, move=False, align="center", font=("Verdana", 10, "normal"))


locate_states_progress()

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"You guessed {len(guessed_states)}/50", prompt="Write any of the state names "
                                                                                         "correctly.").title()
    if user_answer in states_list and user_answer not in guessed_states:
        state_row = state_data[state_data.state == user_answer]
        user.goto(int(state_row.x), int(state_row.y))
        user.write(user_answer, move=False, align="center", font=("Verdana", 10, "normal"))
        guessed_states.append(user_answer)
    elif user_answer.lower() == "exit":
        with open("user_progress.csv", mode="w") as user_progress:
            for state in guessed_states:
                user_progress.write(f"{state}\n")
        break
    elif user_answer.lower() == "clear":
        with open("user_progress.csv", mode="w") as user_progress:
            pass


