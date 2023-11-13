# Right way

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # friend_foods geting my_foods list item

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n-----------------------------------------------------------------------\n")


#-----------------------------------------------------------------------------

# Wrong way

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # friend_foods and my_foods list is same list

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)