from random import randint
from winsound import PlaySound, SND_FILENAME
from time import sleep
import turtle

t = turtle.Turtle()
dice = turtle.Turtle()
win_lose = turtle.Turtle()

turtle.bgpic("green felt.gif")

win = turtle.Screen()

ranNum1 = randint(1, 6)
ranNum2 = randint(1, 6)

t.penup()

t.goto(200, 175)

t.write(f"{ranNum2}", font=("Arial", 50, "normal"))

sleep(2)

t.goto(0, 0)

num = f"{ranNum1} dice.gif"

win.addshape(num)

dice.shape(num)

sleep(5)

if (ranNum1 == ranNum2):
    win.clearscreen()
    win.addshape("tie.gif")
    win_lose.shape("tie.gif")
    PlaySound("tie.wav", SND_FILENAME)
if (ranNum1 > ranNum2):
    win.clearscreen()
    win.addshape("try again.gif")
    win_lose.shape("try again.gif")
    PlaySound("lose.wav", SND_FILENAME)
if (ranNum1 < ranNum2):
    win.clearscreen()
    win.addshape("winner.gif")
    win_lose.shape("winner.gif")
    PlaySound("win.wav", SND_FILENAME)



turtle.exitonclick()
