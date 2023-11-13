''' Ask the user for a number, and then report whether the
number is a multiple of 10 or not. '''

number = int(input("Give the number: "))

if number % 10 == 0:
    print(str(number) + " is multiple of 10.")
else:
    print(str(number) + " is not multiple of 10.")