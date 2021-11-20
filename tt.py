import turtle
a = list(map(int,input().split()))
for i in range(10):
    turtle.circle(a[i])
mx = 0
for i in range(10):
    if a[i] > mx:
        mx = a[i]
turtle.pencolor('red')
turtle.circle(mx)
turtle.done()