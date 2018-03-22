
# Given the following list:

students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

count = 1   #set counter how many times you are going through the for loop
for i in students:
    names = [] #set new list to add the names into it
    for key, value in i.items():
        names.append(value)
    count = count + 1  #count how many times he is going trough the for loop - don't put it into the for loop!! (counts starts always at zero!!!)
    
    print '{} {} {}'.format(count, ' '.join(names), len(names[0])+len(names[1]))
