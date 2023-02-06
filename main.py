import turtle, pandas

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
print(data)

# screen
screen = turtle.Screen()
screen.title("U.S. Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# writing
turtle_writer = turtle.Turtle()
turtle_writer.penup()
turtle_writer.shape("turtle")
turtle_writer.color("green")
turtle_writer.pencolor("black")

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed", prompt="Guess the State name:").title()
    if answer_state == "Exit":
        break
    if str(answer_state) in str(data["state"]):
        state_row = data[data.state == answer_state]
        x = float(state_row.x)
        y = float(state_row.y)
        turtle_writer.goto(x, y)
        turtle_writer.write(f"{answer_state}", align="center", font=("Courier", 15, "normal"))
        guessed_states.append(answer_state)

remaining_states = []

for _ in all_states:
    if _ not in guessed_states:
        remaining_states.append(_)

remaining_data = pandas.DataFrame(remaining_states)
remaining_data.to_csv("remaining_states.csv")
