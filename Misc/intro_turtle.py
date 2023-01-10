import turtle
from time import sleep

t = turtle.Turtle()
turtle.setup(500, 500)
win = turtle.Screen()
win.bgpic("face.gif")
t.hideturtle()
win.bgpic("test.gif")
sleep(2)                                                
win.update()
t.write("Get rickrolled!", align="center", font=("Comic-Sans", 50, "normal"))
turtle.exitonclick()