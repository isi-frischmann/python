# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

word_list = ['hello','world','my','name','is','Anna']
char = 'l' #charakter you want to search
found = []
# new_list = ['hello','world']

for letter in word_list:  # search for each word in list word_list
    if char in letter:  # if letter you are searching is in the word (which you get loop by loop from line 6)
        found.append(letter)   # then add word to the found list

print found
