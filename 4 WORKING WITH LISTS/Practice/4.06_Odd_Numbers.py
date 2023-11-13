''' Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number. '''

odd_number = [value for value in range(1,20,2)]
for value in odd_number:
    print(value)