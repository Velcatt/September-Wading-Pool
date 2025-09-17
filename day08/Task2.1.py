import turtle

screen = turtle.Screen()
screen.bgcolor("white")

cursor = turtle.Turtle()
cursor.color("green")

for i in range(4):
    cursor.forward(50)
    cursor.right(90)
screen.exitonclick()
