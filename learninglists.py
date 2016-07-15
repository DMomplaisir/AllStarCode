myList = ["words", "are", "great", "and"]
myList.append(3) # add a value to end 
print (myList) 

del myList[4] #everything will move up one 
print (myList) 

print(len(myList)) # will print out amount of elements

# print out numbers in 10 - 20
numList = []
for x in range(10,21):
    numList.append(x)
    #easier way to do numList = range(10,21)
print (numList)


# print 5 0's
zeroList = []
for x in range(5):
    zeroList.append(0)
print (zeroList)

#create empty list 
emptyList = []

#get size of list
randList = ["a", 5, "doodle", 3, 10]
print(len(myList))
#delete from a list
del randList[3]
print (randList)
#add element to list
randList.append(30)
print (randList)

#replace element
randList[0] = 8.4
print (randList)

# add to top of list
randList.insert(0,'a')
print (randList)

# oddList
oddList = [] 
for x in range (0,11):
    if x % 2 != 0:
        oddList.append(x)
print (oddList)

#loops in Pythonlist
for i in oddList:
    print(i)
    # assigns i to each element in loop.
for i in range(len(myList)):
    print(myList[i])
    #same things 
    