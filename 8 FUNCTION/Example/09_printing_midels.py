# Start with some designs that need to be printed.
unprinted_degings = ['iphon case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each desing, untill none are left.
# More each desing to completed_models after printing.
while unprinted_degings:
    currrent_design = unprinted_degings.pop()

    # Simulate creating a 3D print from the design.
    print("printing model: " + currrent_design)
    completed_models.append(currrent_design)

# Display all complered models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)