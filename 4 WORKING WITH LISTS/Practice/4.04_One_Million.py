''' Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.) '''

one_million = [value for value in range(1,1000001)]
for value in one_million:
    print(value)