import turtle
a = int(input())
b = int(input())
for i in range(b):
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(a)
    turtle.left(60)
turtle.done()