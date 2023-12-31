''' Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made. '''


# Type 1---------------------------------------------------------------------------
sandwich_orders = ['Club Sandwich', 'Reuben Sandwich', 'Grilled Cheese Sandwich', 'Tuna Salad Sandwich']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print('I made your ' + sandwich.title() + ".")
    finished_sandwiches.append(sandwich)
sandwich_orders.clear()
print(sandwich_orders)
print(finished_sandwiches)


# Tyep 2 ---------------------------------------------------------------------------
sandwich_orders = ['Club Sandwich', 'Reuben Sandwich', 'Grilled Cheese Sandwich', 'Tuna Salad Sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich.title() + ".")
    finished_sandwiches.append(sandwich)

print(sandwich_orders)
print(finished_sandwiches)