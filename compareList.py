# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". 
# If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

listOne = [4, 5, 3, 8, 90, 78]
listTwo = [4, 5, "Munich", 6, 4, 90]

if set(listOne) == set(listTwo):
    print "The lists are the same"
else:
    print "The lists are not the same"