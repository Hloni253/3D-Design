import turtle

screen = turtle.Screen()

line = turtle.Turtle()
line.speed(0)

def repeated_circles(radius, c_angle, angle):
    for i in range(9):
        line.circle(radius, c_angle)
        line.rt(angle)
        
        
def petal():
    for i in range(2):
        line.circle(60, 60)
        line.rt(240)

def flower():
    for i in range(12):
        petal()
        line.right(60)
        

def ray():
    line.circle(60, 120)
    line.circle(-60, 120)

def sun():
    for i in range(9):
        ray()
        line.rt(160)
        
sun()