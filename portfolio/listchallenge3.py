from random import *


#Create the list of words you want to choose from.
first5 = ["Bird flew through the tree", "Cow ate the lush grass", "Leaves fall on the ground"]
next7 = ["Car drove to the big mansion","Women walks to the red door", "Dog barks at the open door" ]

#Generates a random integer.
x = randint(0, len(first5)-1)
y = randint(0, len(next7)-1)
z = randint(0, len(first5)-1)

name = first5[x] + "\n" + next7[y] + "\n" + first5[z]

print(name)
