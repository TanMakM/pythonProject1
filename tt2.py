import turtle
a = int(input())
b = int(input())
for i in range(a):
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)
    b = b / 2
turtle.done()