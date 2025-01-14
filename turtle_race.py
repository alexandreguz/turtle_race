import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height= 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -140
turtles_list = []
speed = [10, 15, 20, 25]
game_over = False

for color in colors:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240, y= y_position)
    turtles_list.append(new_turtle)
    y_position += 50

turtle_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race" )

while not game_over:
    for turtle in turtles_list:
        turtle.forward(random.choice(speed))
        if turtle.xcor() >= 230:
            turtle_color = turtle.pencolor()
            game_over = True
if turtle_color == turtle_bet:
    print("You Win")
else:
    print(f"You Lose. The winner turtle was {turtle_color}")

screen.exitonclick()



################  solucao da professora ######################

# from turtle import Turtle, Screen
# import random
#
# is_race_on = False
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -40, -10, 20, 50, 80]
# all_turtles = []
#
# #Create 6 turtles
# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.penup()
#     new_turtle.color(colors[turtle_index])
#     new_turtle.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in all_turtles:
#         #230 is 250 - half the width of the turtle.
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost! The {winning_color} turtle is the winner!")
#
#         #Make each turtle move a random amount.
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)
#
# screen.exitonclick()


