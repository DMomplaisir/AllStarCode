from Myro import *
init ("sim")
# By Dylan Momplaisir
# Description: Let robot travel through an obstacle course
# without hitting any objects by detecting objects in front
# of it, then moving backwards, then turning to the side. 


count = 0
# count measuring runtime of robot
while count < 10:
    forward (1,1)
    status = getObstacle(1) 
    #getObstacle tests proximity of objects around it, using it's center IR
    
    
    if status > 5000:
        backward(0.5, 0.5)
        turnBy(90, "deg")
        #if item is in front of it, move backwards and turn 90 degrees   
    count = count + 1