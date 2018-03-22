# Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
# your function should display what the grade is for a particular score. Here is the grade table:

# pseudocode:
# - creating for loop and pick random number 10 times
# - creat ten different scores
# - create random number between 60-100
# - split the scores numbers with the different grade
# - after 10 times stop the loop

import random #add the random library

def randomNumber(start, end): #start where the random number should start 
    random_num = 0
    for x in range (10): #the loop will run 10 times

        random_num = random.randint(start, end) #always implements to found a random number for integers!!!!
        if random_num > 59 and random_num <= 69:
            print "Score: "+str(random_num)+"; Your grade - D" #set the random number to a string!!

        if random_num > 70 and random_num <= 79:
            print "Score: "+str(random_num)+"; Your grade - C"

        if random_num > 80 and random_num <= 89:
            print "Score: "+str(random_num)+"; Your grade - B"

        if random_num > 90 and random_num <= 100:
            print "Score: "+str(random_num)+"; Your grade - A"

randomNumber(60, 100)


