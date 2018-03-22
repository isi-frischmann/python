# #Find and Place
# #words = "It's thanksgiving day. It's my birthday, too!"
# #print words.find('day')

# #newString = "month"
# #print words.replace().('day', newString)

# #Min and Max

# #x = [2,54,-2,7,12,98]
# #print max(x)
# #print min(x)

# #First and Last
# # x = ["hello",2,54,-2,7,12,98,"world"]
# # #print x[0] 
# # #print x[-1]
 
# # newString = [] 
# # # x.pop(0)insert.(newString)
# # # print x
# # # print newString

# # first = x[0]
# # last = x[-1]
# # # print first, last

# # newString.append(last)
# # # using insert to add the index after (
# # newString.insert(0, first)

# # print newString

# #New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. 
#Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. 
#The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 



#Find and replace
words = "It's thanksgiving day. It's my birthday, too!"

print words.find('day')
print words.replace('day', 'month')
print words

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
#Sort your list first
x.sort()
print x

#Print min and max from list
print min(x)
print max(x)

#first and last
x[0] = 'hello'
print x
x[-1] = 'world'
x[len(x)-1] = 'good bye' #both options are working.. x[-1] and x[len(x)-1] as well!
print x 

#creat new variable and split list into half 
leftHalfOfX = x[:len(x)/2]
rightHalfOfX = x[len(x)/2:]

print leftHalfOfX
print rightHalfOfX

# a[start:end]  # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array

# take right half and insert left half on index 0
rightHalfOfX.insert(0, leftHalfOfX)

print rightHalfOfX
    