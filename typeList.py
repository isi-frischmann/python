# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. 
# If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

# pseudocode:
# make an array
list = [3, "Luci", 5, 6, 43.45, "15/07/18", 45, 5, 6, 7, 4, 76, "Manuel"]
newList = [] 
sum = 0
# go trough list
for i in list:
# check if the data is string or integer
    if isinstance(i, int) or isinstance(i, float):
        sum += i  # if data is number add it to a sum
    else:
        newList.append(i)  # if data is a string concatenate into new string

print sum, newList    # print num and print string 
        
# print (" " .join(newList)) #

# check if string only print xyz - else check if string and int print mixed - else check if only int print int
if sum > 0 and len(newList) == 0:
    print "Integer only"
elif    sum == 0 and len(newList) > 0: #You have to check sum and newList other wise it is checking just the newList
    print "String only"
else:
    print "Mixed"

