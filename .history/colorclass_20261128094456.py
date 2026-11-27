class Colour:
    """ An empty class -- all it has is a name """ pass
# =============================================
def display(colour):
    """ Function to print a given colour """
    print("Colour: ", colour.red, colour.green, colour.blue)



colour = Colour() # Call the constructor to make a Colour
colour.red = 255 # Give it some attributes
colour.green = 123
colour.blue = 53
display(colour)