import turtle
turtle.Screen().bgcolor("teal")
turtle.Screen().setup(800 , 800)
turtle.title("Hello ")
square = turtle.Turtle()
size=0
while True:
    for i in range(4):
        square.fd(size + 1)
        square.left(90)
        size -=5
    size+=1
    

