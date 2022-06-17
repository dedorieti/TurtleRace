import turtle as t
import random as rdm
from functions import random_color

t.colormode(255)

turtle_bunch = []
colors = ["red", "blue", "yellow", "pink", "purple", "green"]
# more colors: "orange", "brown", "chocolate", "coral
is_race_on = False
screen = t.Screen()
screen.setup(width=800, height=600)

user_bet = screen.textinput(title="Make your bet", prompt=f"Pick a color {colors}")

for i in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.speed("fast")
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.color(colors[i])
    new_turtle.setpos(x=-360, y=-250 + i*50)
    new_turtle.showturtle()
    turtle_bunch.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in turtle_bunch:
        if racer.xcor() >= 200:
            is_race_on = False
            winner = racer.color()[1]
        racer.forward(rdm.randint(0, 10))


if winner == user_bet:
    print(f"You won! The winner is {winner}")
else:
    print(f"You lost! The winner is {winner}")

screen.exitonclick()