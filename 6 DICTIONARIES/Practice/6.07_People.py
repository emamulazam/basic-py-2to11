''' Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person. '''

informations_1 = {
    'first_name': 'emamul',
    'last_name': 'azam',
    'age' : 18,
    "city" : 'barishal'
}
informations_2 = {
    'first_name': 'sahed',
    'last_name': 'islam',
    'age' : 21,
    "city" : 'dhaka'
}
informations_3 = {
    'first_name': 'rejaul',
    'last_name': 'khan',
    'age' : 17,
    "city" : 'feni'
}

peoples = [informations_1, informations_2, informations_3]

for people in peoples:
    print(people['first_name'].title() + " " +
          people['last_name'].title() + " live in " +
          people['city'].title() + " and his/her age is " +
          str(people['age']) + '.')