import turtle

name = input("What is your name? ")
bgcolor = input('What colour would you like the background to be? ')
tcolor = input('What colour would you like the turtle to be? ')
font_size = int(input('What size would you like the font to be? '))

if font_size < 50:
    font_size = 50
if bgcolor.lower() != "black":
    bgcolor = "black"
if tcolor.lower() != "white":
    tcolor = "white"

t = turtle.Turtle()

rootwindow = turtle.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

turtle.bgcolor(bgcolor)
t.color(tcolor)

font = ('Arial', font_size, 'normal')
t.write(name, font=font, align='center')

turtle.exitonclick()
