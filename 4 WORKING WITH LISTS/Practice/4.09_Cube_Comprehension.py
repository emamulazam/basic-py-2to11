''' Use a list comprehension to generate a list of the
first 10 cubes.'''

number = [value**3 for value in range(1,11)]
print(max(number))
print(min(number))
print(sum(number))