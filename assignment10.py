# importing turtle library
import turtle

val = 50
pen = turtle.Turtle()
pen.color("orange","green")
pen.pensize(2)
pen.shape("turtle")

for i in range(val):
    pen.forward(i*10)
    # in clockwise
    pen.right(144)

turtle.done()