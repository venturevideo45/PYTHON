import turtle

turtle.Screen().bgcolor("lightblue")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Square on Canvas")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i + 1
turtle.done()
    