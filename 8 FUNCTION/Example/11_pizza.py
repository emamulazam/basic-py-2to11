def make_pizza(size, *toppings):
    "Sumarize the pizza we are about to make."
    print("\nMakeing a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, "mushroons", 'green peppers', 'extra cheese')

''' The function in the following example hase one parametcr,
*toppings, but  this parameter collects as many arguments as the calling
line provids. ''' 