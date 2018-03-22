''' pseudocode:
-create two lists from 0 - 12 (listHorizontal and listVertical)
- create a for loop which goes through each index of listVertical
-create a for loop in the for loop which goes through each index in listHorizontal 
    -and multiplies it with index 0 from listVertical
'''
#first row (horizontal) is wrong. There needs to be numbers and no x

listVertical = [1,2,3,4,5,6,7,8,9,10,11,12]
listHorizontal = [1,2,3,4,5,6,7,8,9,10,11,12]


for i in listVertical:
    newLine = ''
    for a in listHorizontal:
        newLine += str(i * a) + ' '  
    print 'x', newLine