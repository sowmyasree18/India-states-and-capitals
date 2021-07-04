import turtle
import time
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.setup(800, 750)
screen.title("U.S. States Game")
image = "blankimage.gif"
screen.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv("29_states.csv")
all_states = data_states.state.to_list()

data_capitals = pandas.read_csv("capitals.csv")
all_capitals = data_capitals.capital.to_list()

guessed_states = []
guessed_capitals = []
guessed_states_and_capitals = []

t = turtle.Turtle()
t.hideturtle()
t.penup()

messagebox.showinfo("Note", "If you want to exit, type \"exit\" in text box.")

while len(guessed_states_and_capitals) < 57:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/57 States and Capitals are Correct",
                                   prompt="What's another state's name?").title()
    if user_answer == "Exit":

        turtle.shape("blank")
        t.clear()
        t.goto(-200, 345)
        t.write("UNIDENTIFIED STATES AND CAPITALS", font=("Arial", 15, "underline"))
        t.goto(-240, 305)
        t.write("States", font=("Arial", 15, "underline"))
        t.goto(153, 305)
        t.write("Capitals", font=("Arial", 15, "underline"))
        x = -253
        y = 288
        for state in all_states:
            if state not in guessed_states:
                y = y - 20
                t.goto(x, y)
                t.write(state, font=("Arial", 13, "normal"))
        x = 148
        y = 292
        for capital in all_capitals:
            if capital not in guessed_capitals:
                y = y - 20
                t.goto(x, y)
                t.write(capital, font=("Arial", 13, "normal"))
        time.sleep(5)
        break
    if user_answer in guessed_states:
        messagebox.showinfo("Note", f"You have already located {user_answer}. Try to identify other states.")

    elif user_answer in guessed_capitals:
        messagebox.showinfo("Note", f"You have already located {user_answer}. Try to identify other capitals.")

    elif user_answer in all_states:
        guessed_states_and_capitals.append(user_answer)
        guessed_states.append(user_answer)
        state_data = data_states[data_states.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer, font=("Arial", 9, "bold"))

    elif user_answer in all_capitals:
        guessed_states_and_capitals.append(user_answer)
        guessed_capitals.append(user_answer)
        capital_data = data_capitals[data_capitals.capital == user_answer]
        t.goto(int(capital_data.x), int(capital_data.y))
        if user_answer == "Chandigarh":
            t.write(f"{user_answer}●", font=("Arial", 9, "normal"))
            messagebox.showinfo("Note", "Chandigarh is the shared capital city of both Punjab and Haryana.")
        else:
            t.write(f"●{user_answer}", font=("Arial", 9, "normal"))

if len(guessed_states_and_capitals) == 57:
    messagebox.showinfo("Congrats", "Congrats!, you have located all states and capitals.")