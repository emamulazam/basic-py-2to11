''' Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary. '''

informations = {
    'first_name': 'emamul',
    'last_name': 'azam',
    'age' : 18,
    "city" : 'barishal'
}

for value in informations:
    print(value.title() + ' is ' + str(informations[value]).title() + ".")

# print(informations)
# print(informations.keys())
# print(informations.values())