''' Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend's favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.'''


my_favorite_pizza = ['BD pizza', 'USA pizza', 'UK pizza']
friend_favorite_pizza = my_favorite_pizza[:]
my_favorite_pizza.append('pak pizza')
friend_favorite_pizza.append('indian pizza')

print('My favorite pizzas are:')
for value in my_favorite_pizza:
    print(value.title())

print("\nMy friend's favorite pizzas are:")
for value in friend_favorite_pizza:
    print(value.title())