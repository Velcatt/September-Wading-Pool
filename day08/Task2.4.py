import turtle


def spiral(size):
    screen = turtle.Screen()
    cursor = turtle.Turtle()
    cursor.color("red")
    for i in range(100):
        cursor.forward(i * size)
        cursor.right(100 - i)
    screen.exitonclick()


spiral(0.5)
