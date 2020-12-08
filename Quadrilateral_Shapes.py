import turtle

screen = turtle.Screen()

line = turtle.Turtle()
line.speed(0)

#angles - 144(star), 60(diamond), 190, 200(benz sign), 30(octagon), 72(pentagram)

def shapes(length, angle):
    while True:
        line.fd(length)
        line.rt(angle)
        line.fd(length)
        line.rt(2*angle)
        
shapes(100, 60)