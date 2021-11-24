import turtle
from time import sleep

bgimg = int(input("Which background?\n1) Computer\n2) Face: "))
colour = int(input("Which colour?\n1) Red\n2) Blue "))
show = int(input("Show?\n1) Yes\n2) No "))
shape = int(input("Shape?\n1) Square\n2) Circle "))

while bgimg != 1 and bgimg != 2:
    bgimg = int(input("Which background?\n1) Computer\n2) Face: "))
while colour != 1 and colour != 2:
    colour = int(input("Which colour?\n1) Red\n2) Blue "))
while show != 1 and show != 2:
    show = int(input("Show?\n1) Yes\n2) No "))
while shape != 1 and shape != 2:
    shape = int(input("Shape?\n1) Square\n2) Circle "))

t = turtle.Turtle()

turtle.setup(500, 500)

img = "computer.gif" if bgimg == 1 else "face.gif"
color = "red" if colour == 1 else "blue"

win = turtle.Screen()
win.bgpic(img)

def test():
    print("test")
    win.bgpic("test.gif")
    win.update()
win.onkey(test, "Up")

if (show == 2):
    t.hideturtle()

def drawCircle():
    t.begin_fill()
    t.circle(50)
    t.color(color)
    t.end_fill()

def drawSquare():
    t.begin_fill()
    t.color(color)
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

if (shape == 1):
    drawSquare()
else:
    drawCircle()

rootwindow = turtle.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
turtle.exitonclick()