'''Program: Random Movie Generator
Description: Creates random movie titles - using Introduction, Location, and featuring'''
from random import *

intro = ["Running ", "From the Trap to", "Ending", "Savage", "Running", "Lost in", "Blood at", "Rising", "Shooting at ", "Working at"]
location = ["Saigon", "the Trap", "the 6", "You", "Bronx", "Brownsville", "South", "Ya Mom's", "the Streets", "1000 St"]
featuring = ["B.I.G", "Tupac", "President Obama", "Yeezus", "GOD", "Timmy Turner", "the Fugees", "Donald Trump", "Pikachu", "Me"]

#Declares variable to be a random number 
randintro = randrange(10)
randlocale = randrange(10)
randfeature = randrange(10) 

for x in range(10):
    
    #prints out number, and randomly selects from list" 
    print((x+1) ,intro[randintro] +  " " + location[randlocale] + " featuring " + featuring[randfeature])
    
    #Deletes entry from list, prevents repeating it 
    del intro[randintro] 
    del location[randlocale]
    del featuring[randfeature]
    
    #Continues going until the last element in the loop || changes the number each loop cycle 
    if (len(intro)) < 10 and (len(intro)) != 0:
        randintro = randrange(len(intro))
        randlocale = randrange(len(location))
        randfeature = randrange(len(featuring)) 
    else: 
        print ("Done.")