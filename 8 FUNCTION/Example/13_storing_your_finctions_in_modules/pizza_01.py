def make_pizza(size, *toppings):
    "Summarize the pizza we are about to make."
    print("\nMake a " + str(size) +
          "-inch pizza with the folloing toppings:")
    for topping in toppings:
        print("- " + topping)