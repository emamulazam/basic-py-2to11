def print_models(unprinted_desingns, completed_models):
    '''
    Simlate printing each desing, untill none are left.
    Move each desing to completed_models after printing.
    '''
    while unprinted_desingns:
        currrent_design = unprinted_desingns.pop()
        # Simulate creating a 3D print from the design.
        print("printing model: " + currrent_design)
        completed_models.append(currrent_design)

def show_completed_models(completed_models):
    "Show all the models that were printed."
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphon case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

''' If you're writing a function and notice the function is diong
too many different tasks, try to split the code into two funtions '''