
from turtle import Screen,Turtle
import pandas
t = Turtle()
screen = Screen()
screen.title("U.S. Game screen")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(data)
score = 0
while(score<50):
    answer_state = screen.textinput(title = f"{score}/50"+" Guess State: ", prompt="Enter your answer").title()
    print(answer_state)
    if answer_state in all_states:
        print("Correct")
        score+=1
        t1 = Turtle()
        t1.hideturtle()
        t1.penup()
        x_coor = int(data[data["state"]==answer_state].x)
        y_coor = int(data[data["state"] == answer_state].y)
        print(x_coor)
        print(y_coor)
        t1.goto(x_coor,y_coor)
        t1.write(answer_state)
    else:
        print("Try again")

screen.mainloop()