''' Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time. '''

def list_of_items(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Sandwich is ready!\n")

list_of_items("Turkey", "Lettuce", "Tomato", "Mayo")
list_of_items("Ham", "Swiss Cheese", "Pickles")
list_of_items("Peanut Butter", "Jelly")