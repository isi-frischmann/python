# 1.
# SET greeting AS 'hello' 
# SET name AS 'dojo' 
# LOG name + greeting
greeting = 'hello'
name = 'dojo'

print greeting +" "+ name

# 2.
# Given an array of words: ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']
# Loop through the array
# Print each word to consol
array = ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']

for i in range(0, len(array)):
    print array[i]


# 3.
# Write a function that takes a number.
# Create an empty list.
# Multiply that number by 2.
# Push the new number to our empty list.
# Repeat 25 times.
# Print list.
def function(value):
    lst = []
    value *= 2
    for i in range(0, 25):
        lst.append(value)
    print lst

function(5)

# 4.
# Define a small program that accepts strings as inputs
# Have your program create a blank string.
# Starting at the back of the input string and walking backwards: 3a. Push each character into the blank string. 3b. 
#Repeat for all characters in input string.
# Print the reversed string.
x = 'hello'
def strings(str):
    newString = ""
    for i in range(len(str)-1,-1,-1):
        newString += x[i]
        # print x[i]
    print newString
strings(x)


# 5.
x = 10      # x EQUALS 10
x = x * 7   # x EQUALS x TIMES 7
y = 30      # y EQUALS 30
z = y + x   # z EQUALS y PLUS x
z = z * 3   # z EQUALS z TIMES 3
z = z - y   # z EQUALS z MINUS y
z = z / 27  # z EQUALS z DIVIDED_BY 27
x = z + y   # x EQUALS z PLUS y
y = 3       # y EQUALS 3
x = x + y   # x EQUALS x PLUS y

# RETURN TRUE if x MODULUS 10 EQUALS 0
# OTHERWISE RETURN FALSE
def hello(x):
    if (x % 10 == 0):
        print "true"
    else:
        print "false"
hello(10)
