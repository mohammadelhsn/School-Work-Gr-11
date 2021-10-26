import turtle 

t = turtle.Turtle()
w = turtle.Turtle()

rootwindow = turtle.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

t.shape("classic")
t.color("white")
turtle.bgcolor("black")

ask = input("What is your name")

my_font = ("Arial", 20, "normal")

t.write(ask)




turtle.exitonclick()