import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(my_turtle = None):
  for x in range(-360,360):
    y = math.sin(math.radians(x))
    my_turtle.goto(x,y)


def setupWindow(mywindow = None):
  mywindow.reset()
  mywindow.setworldcoordinates(-360, -1, 360, 1)

#inclusive?

  
def setupAxis (myturtle = None):
  myturtle.goto(-360, -1)
  myturtle.bgcolor('green')
  myturtle.speed()
  

def drawSineCurve(my_turtle = None):
  for x in range(-360,360):
    y = math.sin(math.radians(x))
    my_turtle.goto(x,y)

def drawCosineCurve(my_turtle = None):
  for x in range(-360, 360):
    y = math.sin(math.radians(x))
    my_turtle.goto(x,y)
    
def drawTangentCurve(my_turtle = None):
  for x in range(-360, 360):
    y = math.sin(math.radians(x))
    my_turtle.goto(x,y)


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
