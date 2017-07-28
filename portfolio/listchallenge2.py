from random import *


#Create the list of words you want to choose from.
Sides = ["mashed potatos", "french fries", "onion rings", "salad"]
Main = ["pasta", "pizza", "mac n' cheese", "burger"]
Desserts = ["icecream", "pie", "cake", "brownies"]

#Generates a random integer.
x = randint(0, len(Sides)-1)
y = randint(0, len(Main)-1)
z = randint(0, len(Desserts)-1)
print ("The menu today is " + Sides[x] + " " + Main[y] + " " + Desserts[z])
