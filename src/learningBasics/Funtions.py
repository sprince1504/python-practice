# basic function example globa variable
x = "Prince"

def myfunction():
    print("Ohh Hello",x)

myfunction()

# basic function example globa variable & local vairable
x = "Prince"

def myfunctionExample():
    x = "Rajan"
    print("Hello ",x)

myfunctionExample()


# with Global keyword
global x
x = "Prince"

def globaKeyWorkExample():
    x= "Rajan"
    print("You Again ! with Global Keyword",x)

globaKeyWorkExample()

print("But you will be still",x)