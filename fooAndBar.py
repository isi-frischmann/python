'''
FOO: prime number can be devided only by 1 or itself. for example 5
BAR: a square number is a value which is multiplyed by itself. for example 3*3 = 9 --> 9 is a square number, 16, 25'''

'''pseudocode:
- find prime number
- find square numbers
- creat for loop 
- iterate through loop from 100 - 100000
- if it is a prime number print "Foo"
- if it is a square number print "Bar"
- if it non of both print "FooBar"
'''

start = 2
stop = 10

is_prime = True

#Prime numbers are not working correctly 
for i in range(start, stop, +1):
    if i > 1:
        # prime_numbers = 0
        for a in range(2, i):
            raw_input("i={}, a={}".format(i, a)) #raw_input shows you what i and a is already...
            if i % a == 0:
                is_prime = False
                # raw_input("i={}, a={}".format(i, a))
                print "false"
                break
            else:
                print"Prime {}".format(i)
            

# Square numbers are working!
for b in range(start, stop):
    x = b * b
    print "Square", x


#Code from Zack which is working
# start = 10
# end = 20

# is_perfect = False
# is_prime = True
# for x in range(start, end+1):
#     for num in range(2, x-1):
#         if x % num == 0:
#             is_prime = False
#             if x == num ** 2:
#                 print("Bar", x)
#                 is_perfect = True

#     if is_prime and x != 1:
#         print("Foo", x)
#     elif not is_perfect and not is_prime:
#         print("FooBar", x)
#     is_prime = True
#     is_perfect = False