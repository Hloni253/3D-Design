import turtle

#recommended angles - 30, 90
#interesting, 360 is an octagon

screen = turtle.Screen()

line = turtle.Turtle()
line.speed(0)

def initial_shape(length, angle):
    for i in range(2):
        line.fd(length)
        line.right(angle)
    half_length=length/2
    for i in range(2):
        line.fd(half_length)
        line.right(angle)
    line.fd(length)
    line.right(angle)
    quarter_length=length/4
    for i in range(2):
        line.fd(quarter_length)
        line.right(angle)
    line.fd(half_length)
    

def repeated_shape(length, angle):
    for i in range(4):
        initial_shape(length, angle)


def angle_repeated_shape(length, angle):
    while True:
        initial_shape(length, angle)
        line.right(10)
        line.fd(50)
        

def multiple_repeated_shapes(length, angle):
    while True:
        initial_shape(length, angle)
        line.left(45)
        line.fd(length)
        

multiple_repeated_shapes(30, 90)