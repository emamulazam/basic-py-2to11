# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chese']
}

# Sumarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with fhe following topings:")

for topping in pizza['toppings']:
    print("\t" + topping)