# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for i in range (1, 1000):
    if i % 2 == 0:
        print i
        
# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for i in range (5, 1000000):
    if i % 5 == 0:
        print i

#creat a programm which prints the sum of the list
a = [1, 2, 5, 10, 255, 3]

print sum(i for i in a)

#print average list
b = [1, 2, 5, 10, 255, 3]

avg = sum(b)/len(b)
print avg