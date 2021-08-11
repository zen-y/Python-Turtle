import turtle

house = turtle.Turtle()
turtle.bgcolor("blue")

#walls
house.begin_fill()
house.color("pink")

for i in range(4):
    house.forward(100)
    house.left(90)

house.left(90)
house.forward(100)
house.end_fill()

#roof
house.begin_fill()
house.color("brown")

house.right(30)
house.forward(100)
house.right(120)
house.forward(100)

house.end_fill()






turtle.done()