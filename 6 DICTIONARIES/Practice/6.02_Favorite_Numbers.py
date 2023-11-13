''' Use a dictionary to store people's favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person's name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program. '''

favorite_numbers = {}

favorite_numbers['ali'] = 7
favorite_numbers['ela'] = 2
favorite_numbers['ami'] = 8
favorite_numbers['nil'] = 9
favorite_numbers['tom'] = 5

for value in favorite_numbers:
    print(value.title() + "'s favorite number is " +
          str(favorite_numbers[value]) + '.')