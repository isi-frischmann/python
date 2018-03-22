# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

# def odd_even(start, stop):
#     for i in range (start, stop):
#         if i % 2 == 0:
#             print "Number is {}. This is an odd number.".format(i)
#         else:
#             print "Number is {}. This is an even number.".format(i)

# odd_even(1, 2001)


# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been multiplied by 5.
# def multiply(x):
#     lst = [2, 4, 10, 16] 
#     newList = [i * (x) for i in lst] #creating new list and 
#     print newList

# multiply(5)

# ANOTHER way:
# lst = [2, 4, 10, 16]

# listMulti = []
# for i in lst:
#     listMulti.append(i * 5)
# print listMulti


# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list.

# pseudocode:
#create new list
#go trough each index in the list and multiply them
    #add as many times 1 as the list contains values 
#multiply the first list into a new list
    #add as many times 1 as the list contains values again for the added list

lst = [2, 4, 10, 16] 

# def multiply(x):
#     newList = [i * (x) for i in range(len(list))  
#     print newList

# multiply(5)

# def layered_multiples(lst):
#     new_list = [] #creating new list
#         for i in lst:
#             new_list.append(len(lst))
#     print new_list

def layered_multiples(lst,num):
    newList = []
    for i in range(len(lst)):
        lst[i] = lst[i] * num
        innerList = []
        for i in range(0, lst[i]):
            innerList.append(1)
        newList.append(innerList)
    print newList
layered_multiples([2,4,5], 3)
