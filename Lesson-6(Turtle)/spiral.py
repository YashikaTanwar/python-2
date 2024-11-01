import turtle
turtle.Screen().bgcolor("blue")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to Spiral window")
board=turtle.Turtle()
size=0
while True:
    for i in range(4):
        board.forward(size+1)
        board.left(90)
        size=size-5
    size=size+1