"""
Author: Cole Honeck
Last Update: 10/12/2022
Program: QualityIce_Draft_v4.py

Summary:
This program is used to order ice cream from the restaurant,including the size of the order,the flavor of the order,
and toppings added to the order. This program also calculates the total price from the size, flavor, and toppings.

Varables:
totalSize - the price for size
totalFlavor - the price for flavor
totaltoppings - the price for toppings
totalCost - total cost for order
IceCreamChoice.png
errorPhoto.png
"""

from tkinter import *

#Varaibles for cost of size, flavor, and toppings
totalSize = 0
totalFlavor = 0
totalToppings = 0


# Calcultes amount for the size for small
def sizeSmall():
    smallButton["state"] == "normal"
    global totalSize
    totalSize = 1
    smallButton["state"] = "disabled"
    mediumButton["state"] = "normal"
    largeButton["state"] = "normal"
    
# Calcultes amount for the size for medium
def sizeMedium():
    mediumButton["state"] =="normal"
    global totalSize
    totalSize = 2
    mediumButton["state"] = "disabled"
    smallButton["state"] = "normal"
    largeButton["state"] = "normal"
    
# Calcultes amount for the size for large
def sizeLarge():
    largeButton["state"] =="normal"
    global totalSize
    totalSize = 3
    largeButton["state"] = "disabled"
    mediumButton["state"] = "normal"
    smallButton["state"] = "normal"

#Calculates the amount for flavor for clicking 
def flavorVanilla():
    global totalFlavor
    totalFlavor = 1
    VanillaButton["state"] = "disabled"
    ChocolateButton["state"] = "normal"
    MintButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "normal"
    
def flavorChocolate():
    global totalFlavor
    totalFlavor = 1
    ChocolateButton["state"] = "disabled"
    VanillaButton["state"] = "normal"
    MintButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "normal"
    
def flavorMint():
    global totalFlavor
    totalFlavor = 1
    MintButton["state"] = "disabled"
    ChocolateButton["state"] = "normal"
    VanillaButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "normal"
    
def flavorStrawberry():
    global totalFlavor
    totalFlavor = 1
    MintButton["state"] = "normal"
    ChocolateButton["state"] = "normal"
    VanillaButton["state"] = "normal"
    StawberryButton["state"] = "disabled"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "normal"
    
def flavorMatcha():
    global totalFlavor
    totalFlavor = 2
    MintButton["state"] = "normal"
    ChocolateButton["state"] = "normal"
    VanillaButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "disabled"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "normal"
    
def flavorNeaplitan():
    global totalFlavor
    totalFlavor = 3
    MintButton["state"] = "normal"
    ChocolateButton["state"] = "normal"
    VanillaButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "disabled"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "normal"
    
def flavorCoffee():
    global totalFlavor
    totalFlavor = 2
    MintButton["state"] = "normal"
    ChocolateButton["state"] = "normal"
    VanillaButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "disabled"
    ButterscotchButton["state"] = "normal"
    
def flavorButterscotch():
    global totalFlavor
    totalFlavor = 2
    MintButton["state"] = "normal"
    ChocolateButton["state"] = "normal"
    VanillaButton["state"] = "normal"
    StawberryButton["state"] = "normal"
    MatchaButton["state"] = "normal"
    NeaplitanButton["state"] = "normal"
    CoffeeButton["state"] = "normal"
    ButterscotchButton["state"] = "disabled"

# Calculates amount for the toppings for clicking the button
def topChocolateChips():
    chocolateButton["state"] = "disabled"
    chocolateChips = 0.50
    global totalToppings
    totalToppings = totalToppings + chocolateChips

def topSprinkles():
    sprinklesButton["state"] = "disabled"
    sprinkles = 0.50
    global totalToppings
    totalToppings = totalToppings + sprinkles

def topCarmel():
    caramelButton["state"] = "disabled"
    caramel = 0.75
    global totalToppings
    totalToppings = totalToppings + caramel

def topOreos():
    oreosButton["state"] = "disabled"
    oreos = 0.75
    global totalToppings
    totalToppings = totalToppings + oreos

def topCookieDough():
    cookiedoughButton["state"] = "disabled"
    cookieDough = 1
    global totalToppings
    totalToppings = totalToppings + cookieDough

def topMarshmallows():
    marshmallowsButton["state"] = "disabled"
    marshmallows = 1
    global totalToppings
    totalToppings = totalToppings + marshmallows

def topNuts():
    nutsButton["state"] = "disabled"
    nuts = 0.50
    global totalToppings
    totalToppings = totalToppings + nuts

def topMnMs():
    MnMsButton["state"] = "disabled"
    MnMs = 0.75
    global totalToppings
    totalToppings = totalToppings + MnMs

#Clears all the toppings choices with button
def clearToppings():
    clearButton["state"] = "normal"
    chocolateButton["state"] = "normal"
    sprinklesButton["state"] = "normal"
    caramelButton["state"] = "normal"
    oreosButton["state"] = "normal"
    cookiedoughButton["state"] = "normal"
    marshmallowsButton["state"] = "normal"
    nutsButton["state"] = "normal"
    MnMsButton["state"] = "normal"
    global totalToppings
    totalToppings = 0

#Error message if size or flavor isn't clicked
def errorMessage():
    if totalSize == 0 or totalFlavor == 0:
        error=Toplevel(root)
        error.title("Error Message")
        error.geometry("700x300")

        #Location of buttons and labels with configuration
        errorLabel = Label(error,text="Error: Please make sure that you pick your flavor and size before you submit.", font = ("Helvetica",14))
        errorLabel.grid(row = 0, column = 0, sticky = "NSEW")
        closeButton = Button(error, text="Back to Ordering Screen", font= 30, command=error.destroy)
        closeButton.grid(row = 1, column = 0, sticky = "NSEW")

        #Location of image
        errorPhoto = PhotoImage(file = "errorPhoto.png", master=error)
        labelError = Label(error, image = errorPhoto)
        labelError.place(x = 200, y = 60)
        error.image = errorPhoto
        
    else:
        submitScreen() 
    
    


# Calculates amount for the size, flavor, and toppings
def submitScreen():
    totalCost = totalSize + totalFlavor + totalToppings
    order=Tk()
    order.title("Order Screen")
    order.geometry("300x180")


    #Labels for order summary, includes labels for cost and what cost is for
    orderLabel = Label(order,text="Order Summary:", font =("Helvetica",14))
    sizeCostLabel = Label(order,text="Size Cost: ", font = ("Helvetica",14))
    flavorCostLabel = Label(order,text="Flavors Cost: ", font = ("Helvetica",14))
    toppingsCostLabel = Label(order,text="Toppings Cost: ", font = ("Helvetica",14))
    totalCostLabel = Label(order,text="Total Cost: ", font = ("Helvetica",14))

    sizePayLabel = Label(order,text= "$" + "%.2f" % totalSize, font = ("Helvetica",14))
    flavorPayLabel = Label(order,text= "$" + "%.2f" % totalFlavor, font = ("Helvetica",14))
    toppingsPayLabel = Label(order,text= "$" + "%.2f" % totalToppings, font = ("Helvetica",14))
    totalPayLabel = Label(order,text= "$" + "%.2f" % totalCost, font = ("Helvetica",14))

    #Buttons for back and submit
    backButton = Button(order, text="Back to Ordering Screen", font=30, command=order.destroy)
    submitButton = Button(order, text="Submit Order", font=30, command=submitExit)
    
    
    #Label locations for order summary
    orderLabel.grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")
    sizeCostLabel.grid(row = 2, column = 1, sticky = "W")
    flavorCostLabel.grid(row = 3, column = 1, sticky = "W")
    toppingsCostLabel.grid(row = 4, column = 1, sticky = "W")
    totalCostLabel.grid(row = 7, column = 1, sticky = "W")


    sizePayLabel.grid(row = 2, column = 2, sticky = "NSEW")
    flavorPayLabel.grid(row = 3, column = 2, sticky = "NSEW")
    toppingsPayLabel.grid(row = 4, column = 2, sticky = "NSEW")
    totalPayLabel.grid(row = 7, column = 2, sticky = "NSEW")

    #Button location for order summary
    backButton.grid(row = 8, column = 1, sticky = "NSEW")
    submitButton.grid(row = 8, column = 2, sticky = "NSEW")

    

#Submit order and exit program
def submitExit():
    exit()
    

root=Tk()
root.title("QualityIce")
root.geometry("700x350")

#Locatiion of where the image is
choicePhoto = PhotoImage(file = "IceCreamChoice.png")
labelChoice = Label(root, image = choicePhoto)
labelChoice.place(x = 0, y = 0)


#Size button and label configuration
sizeLabel = Label(root,text="Click one size cup.", font = ("Helvetica",14))
smallButton = Button(root, text="Small", command=sizeSmall, font=30)
mediumButton = Button(root, text="Medium", command=sizeMedium, font=30)
largeButton = Button(root, text="Large", command=sizeLarge, font=30)

#Flavor button and label configuration
flavorLabel = Label(root,text="Click one flavor of ice cream", font = ("Helvetica",14))
VanillaButton = Button(root, text="Vanilla", command=flavorVanilla, font=30)
ChocolateButton = Button(root, text="Chocolate", command=flavorChocolate, font=30)
MintButton = Button(root, text="Mint", command=flavorMint, font=30)
StawberryButton = Button(root, text="Stawberry", command=flavorStrawberry, font=30)
MatchaButton = Button(root, text="Matcha", command=flavorMatcha, font=30)
NeaplitanButton = Button(root, text="Neaplitan", command=flavorNeaplitan, font=30)
CoffeeButton = Button(root, text="Coffee", command=flavorCoffee, font=30)
ButterscotchButton = Button(root, text="Butterscotch", command=flavorButterscotch, font=30)

#Toppings button and label configuration
toppingsLabel = Label(root,text="Pick toppings you want.", font = ("Helvetica",14))
chocolateButton = Button(root, text = "Chocolate Chips", command=topChocolateChips, font=30)
sprinklesButton = Button(root, text = "Sprinkles", command=topSprinkles, font=30)
caramelButton = Button(root, text = "Caramel", command=topCarmel, font=30)
oreosButton = Button(root, text = "Oreos", command=topOreos, font=30)
cookiedoughButton = Button(text = "Cookie Dough", command=topCookieDough, font=30)
marshmallowsButton = Button(root, text = "Marshmallows", command=topMarshmallows, font=30)
nutsButton = Button(root, text = "Nuts", command=topNuts, font=30)
MnMsButton = Button(root, text = "M&Ms", command=topMnMs, font=30)
clearButton = Button(root, text = "Clear", command=clearToppings, font=30)

#Submit button and label configuration
submitButton = Button(root, text = "Submit", font=30, command=errorMessage)

#Size label and button postions
sizeLabel.grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")
smallButton.grid(row = 1, column = 0, sticky = "NSEW")
mediumButton.grid(row = 1, column = 1, sticky = "NSEW")
largeButton.grid(row = 1, column = 2, sticky = "NSEW")

#Flavor label and button postions
flavorLabel.grid(row = 2, column = 1, columnspan = 2, sticky = "NSEW")
VanillaButton.grid(row = 3, column = 0, sticky = "NSEW")
ChocolateButton.grid(row = 3, column = 1, sticky = "NSEW")
MintButton.grid(row = 3, column = 2, sticky = "NSEW")
StawberryButton.grid(row = 3, column = 3, sticky = "NSEW")
MatchaButton.grid(row = 4, column = 0, sticky = "NSEW")
NeaplitanButton.grid(row = 4, column = 1, sticky = "NSEW")
CoffeeButton.grid(row = 4, column = 2, sticky = "NSEW")
ButterscotchButton.grid(row = 4, column = 3, sticky = "NSEW")

#Toppings label and button postions
toppingsLabel.grid(row = 5, column = 1, columnspan = 2, sticky = "NSEW")
chocolateButton.grid(row = 6, column = 0, sticky = "NSEW")
sprinklesButton.grid(row = 6, column = 1, sticky = "NSEW")
caramelButton.grid(row = 6, column = 2, sticky = "NSEW")
oreosButton.grid(row = 6, column = 3, sticky = "NSEW")
cookiedoughButton.grid(row = 7, column = 0, sticky = "NSEW")
marshmallowsButton.grid(row = 7, column = 1, sticky = "NSEW")
nutsButton.grid(row = 7, column = 2, sticky = "NSEW")
MnMsButton.grid(row = 7, column = 3, sticky = "NSEW")
clearButton.grid(row = 8, column = 0, columnspan = 4, sticky = "NSEW")

#Sumbit button position
submitButton.grid(row = 10, column = 0, columnspan = 4, sticky = "NSEW")


