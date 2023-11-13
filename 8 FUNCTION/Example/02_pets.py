def describe_pet(animal_type, pet_name):
    "Display information about a pet."
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hemster', 'harry')
describe_pet('dog', 'willie')
''' You can get unexpected results if you mix
up order of the arguments in a function call
when using positional arguments.'''

describe_pet(animal_type='hemster', pet_name='harry')
''' Keyword arguments free you from having to worry about correctly ordering.'''