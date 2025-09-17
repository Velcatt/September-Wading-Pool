import turtle
import math


def trifractal(screen, cursor, length, depth):
    if depth == 0:
        for i in range(3):
            cursor.fd(length)
            cursor.left(120)
    else:
        trifractal(screen, cursor, length / 2, depth - 1)
        cursor.fd(length / 2)
        trifractal(screen, cursor, length / 2, depth - 1)
        cursor.bk(length / 2)
        cursor.left(60)
        cursor.fd(length / 2)
        cursor.right(60)
        trifractal(screen, cursor, length / 2, depth - 1)
        cursor.left(60)
        cursor.bk(length / 2)
        cursor.right(60)


screen = turtle.Screen()
cursor = turtle.Turtle()
cursor.color("black")
cursor.speed(0)

cursor.right(45)
trifractal(screen, cursor, 200, 6)

screen.exitonclick()
