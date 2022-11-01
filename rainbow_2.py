import turtle
screen = turtle.Screen()
draw = turtle.Turtle()

def Circles(col, rad, val):
    draw.color(col)
    draw.circle(rad, -180)
    draw.up()
    draw.setpos(val, 0)
    draw.down()
    draw.right(180)
    
col = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

screen.setup(600, 600)
screen.bgcolor("white")
draw.right(90)
draw.width(10)
draw.speed(10)

for i in range(10):
    Circles(col[i], 10*(i+8), -10*(i+1))
    
draw.hideturtle()