''' A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu. '''

# Initial menu
original_menu = ("Pizza", "Burger", "Salad", "Pasta", "Ice Cream")

# Print the original menu using a for loop
print("Original Menu:")
for food in original_menu:
    print(food)

# Trying to modify an item (Python will reject this)
# Uncomment the following line to see the error
# original_menu[0] = "Sushi"

# Revised menu
revised_menu = list(original_menu)  # Convert tuple to list for modification
revised_menu[0] = "Sushi"  # Replace the first item
revised_menu[2] = "Steak"  # Replace the third item
revised_menu = tuple(revised_menu)  # Convert back to tuple

# Print the revised menu using a for loop
print("\nRevised Menu:")
for food in revised_menu:
    print(food)


