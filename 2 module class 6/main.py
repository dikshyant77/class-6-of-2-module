import turtle 
turtle.Screen().setup(300 , 400)
polygon= turtle.Turtle()

numberofsize= 6 
sizelength = 70
angle = 360 / numberofsize
for i in range(numberofsize):
    polygon.forward(sizelength)
    polygon.right(angle)
turtle.done()


