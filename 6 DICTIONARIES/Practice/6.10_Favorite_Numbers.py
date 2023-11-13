''' Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person's
name along with their favorite numbers. '''

favorite_numbers = {}

favorite_numbers['ali'] = 7, 61
favorite_numbers['ela'] = 2, 13
favorite_numbers['ami'] = 8, 32
favorite_numbers['nil'] = 9, 31
favorite_numbers['tom'] = 5, 60

for person, numbers in  favorite_numbers.items():
    print(person.title() + "'s favorite number is:")
    for number in numbers:
        print("\t" + str(number))