# Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. 
# In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping.

for x in range(5): #
    print str('* * * *') 
    for x in range(0, 1): #The index 1 means going trough the for loop once
        print str(' * * * *')
