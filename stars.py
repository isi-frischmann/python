# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

# pseudocode:
# - going trough array
# - for every number print *

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(x):
    for val in x:
        print "*" *val 

draw_stars(x)


# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
# You may use the .lower() string method for this part.

# pseudocode:
# - call the function from part one
# - check if the input is a string or an integer
# - print value from each input with the first digit
# - if it is an int print the amount in * 
#import re

ring = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_dif(ring):
    for singleValue in ring:    #go through variable
        if type(singleValue) != int: #when value is int skip this part - if string go into if statement
            print singleValue[0].lower() * len(singleValue) #for string print the first letter in lowercase as many times as length of the string
        else:
            print "*" * singleValue #for int print * signs as many times as the value (4 = 4times)
        
draw_dif(ring)

