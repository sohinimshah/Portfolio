from PIL import Image

# RGB values for recoloring.


#ask user input
PictureName = input("Choose a picture: panda.jpg, dog.jpg, turtle.jpg, duck.jpg, cat.jpg, chameleon.jpg\n")
PalletChoice = input("Choose a color pallet:\n1, 2, 3, or 4?\n")



darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
hotPink = (255, 105, 180)
darkOrchid = (153, 50, 204)
coral = (255, 127, 80)
limeGreen = (50, 205, 50)
aquamarine = (127, 255, 212)
lightSlateBlue = (132, 112, 255)
gray = (190, 190, 190)
lightSkyBlue = (135, 206, 250)
darkOrange = (255, 140, 0)
paleGreen = (152, 251, 152)
brightYellow = (255, 255, 0)
violetRed = (208, 32, 144)
# Import image.
my_image = Image.open(PictureName) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
def ColorPallet1():
    for x in image_list:
        intensity = x[0] + x[1] + x[2]
        if intensity < 182:
            recolored.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            recolored.append(red)
        elif intensity >= 364 and intensity < 546:
            recolored.append(lightBlue)
        elif intensity >= 546:
            recolored.append(yellow)

def ColorPallet2():
        for x in image_list:
            intensity = x[0] + x[1] + x[2]
            if intensity < 182:
                recolored.append(aquamarine)
            elif intensity >= 182 and intensity < 364:
                recolored.append(gray)
            elif intensity >= 364 and intensity < 546:
                recolored.append(hotPink)
            elif intensity >= 546:
                recolored.append(lightSlateBlue)

def ColorPallet3():
        for x in image_list:
            intensity = x[0] + x[1] + x[2]
            if intensity < 182:
                recolored.append(coral)
            elif intensity >= 182 and intensity < 364:
                recolored.append(darkOrchid)
            elif intensity >= 364 and intensity < 546:
                recolored.append(lightSkyBlue)
            elif intensity >= 546:
                recolored.append(limeGreen)

def ColorPallet4():
        for x in image_list:
            intensity = x[0] + x[1] + x[2]
            if intensity < 182:
                recolored.append(darkOrange)
            elif intensity >= 182 and intensity < 364:
                recolored.append(paleGreen)
            elif intensity >= 364 and intensity < 546:
                recolored.append(violetRed)
            elif intensity >= 546:
                recolored.append(brightYellow)



def PickColorPallet():
    if PalletChoice == "1":
        ColorPallet1()
    elif PalletChoice == "2":
        ColorPallet2()
    elif PalletChoice == "3":
        ColorPallet3()
    elif PalletChoice == "4":
        ColorPallet4()
    else:
        print("Sorry, you did not type 1, 2, or 3.")


PickColorPallet()

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
