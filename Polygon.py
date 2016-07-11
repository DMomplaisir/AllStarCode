from Myro import *
init("sim") 

sides = 3
penDown()

def polygonMaker(sides): 
    angle = 360.0 / sides
    forward(1.0,1)
    turnBy(angle, "deg")
    return;
    
for x in range (0, sides):
    polygonMaker(sides)
