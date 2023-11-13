''' Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person's name and their favorite places. '''

favorite_place = {
    'dhaka': 'ali',
    'feni': "mim",
    'faridpur': 'lima'
}

for place, person in favorite_place.items():
    print(person.title() + " want to go " + place.title() + '.')