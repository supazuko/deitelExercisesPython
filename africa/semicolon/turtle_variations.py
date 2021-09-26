import turtle

loadWindow = turtle.Screen()
turtle.speed(2)


def spiral_helix():
    for i in range(100):
        turtle.circle(5 * i)
        turtle.circle(-5 * i)
        turtle.left(i)

    turtle.exitonclick()


def rainbow_benzene():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x // 100 + 1)
        t.forward(x)
        t.left(59)


spiral_helix()
rainbow_benzene()

