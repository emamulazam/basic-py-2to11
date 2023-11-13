def describe_pet(pet_name, animal_type='dog'): # Default Values
    "Display information about a pet."
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# A hamster named willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamser named Harry.
describe_pet('harry', 'hamser')
describe_pet(pet_name='harry', animal_type='hamser')
describe_pet(animal_type='hamser', pet_name='harry')

'All style in one.'