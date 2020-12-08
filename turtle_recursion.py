import turtle
import random

#try out 90

screen = turtle.Screen()

line = turtle.Turtle()
line.speed(0)

colors = ['red', 'blue', 'green', 'violet', 'orange']

def recursive_shapes():
    line.fd(100)
    line.rt(90)
    recursive_shapes()

def recursive_shapes_sequel(length, angle):
    a = random.randint(0,4)
    line.pencolor(colors[a])
    line.fd(length)
    line.rt(angle)
    recursive_shapes_sequel(length+1, angle)
    
    
def incrimenting_shapes(side, angle, increment):
    line.fd(side)
    line.rt(angle)
    incrementing_shapes(side+increment, angle, increment)
    
    
def incrimenting_angles(side, angle, increment):
    line.fd(side)
    line.rt(angle)
    incrimenting_angles(side, angle + increment, increment)
    #try- 10, 23, 93
    
    
incrimenting_angles(10, 88, 43)