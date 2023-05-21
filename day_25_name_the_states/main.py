import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data_frame = pandas.read_csv("50_states.csv")
dict_DF = data_frame.set_index('state').T.to_dict('list')
count = 0
boolean = False
guessed_states = []
while boolean != True:
    answer_state = screen.textinput(title=f"({count}/50) Guess the State", prompt="What's another state's name? | Type 'Exit' to quit.").title()
    if answer_state == "Exit":
        missing_state = []
        for state in dict_DF:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in dict_DF:
        guessed_states.append(answer_state)
        count+=1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_frame[data_frame.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

#turtle.mainloop()