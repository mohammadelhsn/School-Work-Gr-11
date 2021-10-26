import turtle

width1 = int(input("Enter the width of the first circle: "))
circolour = input("Enter the colour of the first circle: ")
radius1 = int(input("Enter the radius of the first circle: "))
distance1 = int(input("Enter the distance between the first and second circle: "))
angle1 = int(input("Enter the angle between the first and second circle: "))
distance2 = int(input("Enter the distance between the second and third circle: "))
dotcolour = input("Enter the colour of the dots: ")
dotsize = int(input("Enter the size of the dots: "))

t = turtle.Turtle()
t.ht()
turtle.bgcolor("black")
t.width(width1)
t.color(circolour)
t.circle(radius1)
t.forward(distance1)
t.right(angle1)
t.forward(distance2)
t.dot(dotsize, dotcolour)

turtle.exitonclick()