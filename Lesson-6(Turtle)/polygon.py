import turtle
turtle.Screen().bgcolor("Orange")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to turtle window")
board=turtle.Turtle()
num_sides=6
side_length=70
angle=360/num_sides
for i in range(num_sides):
    board.forward(side_length)
    board.left(angle)
turtle.done()