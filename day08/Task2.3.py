import turtle


def draw_polygon(sides):
    screen = turtle.Screen()
    cursor = turtle.Turtle()
    cursor.color("red")
    for i in range(sides):
        cursor.forward(20)
        cursor.right(360 / sides)
    screen.exitonclick()


draw_polygon(3)
