from Myro import *
from Graphics import *  
# imports the neccesary librarie
#

pic = makePicture("IMG_1197 (1).jpg")
#Pixels variable holds a list of all variables in pic
pixels = getPixels(pic) 


for pixel in pixels:
    #makes color palette - 
    DarkBlue = makeColor(0,51,76)
    Red = makeColor(217, 26, 33)
    Blue = makeColor(112,150,158)
    Yellow = makeColor(252, 227, 166)
    if getGray(pixel) > 180:
        setColor(pixel, Yellow) 
        #if a pixel's brightness is > 180, then we'll set it to Yellow
    elif getGray(pixel) > 120: 
        setColor(pixel, Blue)
        #Pixel brightness in between 180 and 120
    elif getGray(pixel) > 60:
        setColor(pixel,Red) 
        #Pixel brightness in between 60 - 120
    else: 
        setColor(pixel,DarkBlue)
        #if doesn't correspond with earlier conditions just Blue 
print("done") 
show(pic)    
     
    
        
