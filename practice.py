import turtle 

t = turtle.Turtle()
t2 = turtle.Turtle()
text = turtle.Turtle()
win = turtle.Screen()

win.addshape("face.gif")
win.addshape("computer.gif")
t.penup()
t.goto(-200, -200)
t.shape("face.gif")
t.write("Hi!", font=("Arial", 50, "normal"))
t.goto(600, 200)
t2.shape("computer.gif")
t.write("https://youtube.com", font=("Arial", 50, "normal"))


turtle.exitonclick()