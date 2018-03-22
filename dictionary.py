# Create a dictionary containing some information about yourself. 
# The keys should include name, age, country of birth, favorite language.

my_dict = {
    'name': 'Isabell Frischmann', 
    'age': '27', 
    'countryOfBirth': 'Austria, Tyrol', 
    'favoriteLanguage': 'I don\'t know yet'
    }

def myPersonality(dictionary):
    for key in my_dict:
        if key == 'name':
            print "My name is {}".format(my_dict[key])
        if key == 'age':
            print "I'm {} old".format(my_dict[key])
        if key == 'countryOfBirth':
            print "I'm born in {}".format(my_dict[key])
        if key == 'favoriteLanguage':
            print "My favorite language is - {}".format(my_dict[key])        

myPersonality(my_dict)

    