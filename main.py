from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()

def go_forward():
    turtle.forward(10)

def go_back():
    turtle.back(10)

def go_counter_clockwise():
    turtle.right(5)

def go_clockwise():
    turtle.left(5)

def clear_drawing():
    turtle.clear()
    turtle.up()
    turtle.home()
    turtle.down()

screen.listen()
screen.onkey(fun=go_forward, key="w")
screen.onkey(fun=go_back, key="s")
screen.onkey(fun=go_counter_clockwise, key="a")
screen.onkey(fun=go_clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()