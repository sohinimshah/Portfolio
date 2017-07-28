from random import *


#Create the list of words you want to choose from.
PeopleNames = ["Beth", "Sam", "Phil", "Danny", "Gina"]

#Generates a random integer.
x = randint(0, len(PeopleNames)-1)
y = randint(0, len(PeopleNames)-1)
print (PeopleNames[x] + " " + PeopleNames[y])
