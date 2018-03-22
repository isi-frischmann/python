#Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

# pseudocode:
# - creat two different sums for the head and tail to count the amount
# - set how many times the coind should be tossed 
# - count how many times the coin was already tossed
# - set value for the tail or head

import random 

def coinTosses(times):
    sum_head = 0                    #add amount of coins how many times the head was flipped
    sum_tail = 0  
    recordList = 0                 #add how many times the coin was flipped (head&tail) []

    for amount in range(times):    #it should flipped 5000 times
    
        flip = random.randint(0, 1)     #the flip variable sets a random number between 0 and 1 () - with random.randint you will find a random integer
        recordList = recordList + 1     #counting how many times the coin is flipped

        if flip == 1:
            sum_head += 1           #counting how many times the head was flipping
            print "Attempt {}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tails so far".format(recordList, sum_head, sum_tail)

        else:
            sum_tail += 1 
            print "Attempt {}: Throwing a coin... It's a tail! ... Got {} tails(s) so far and {} head(s) so far".format(recordList, sum_tail, sum_head)

coinTosses(50)