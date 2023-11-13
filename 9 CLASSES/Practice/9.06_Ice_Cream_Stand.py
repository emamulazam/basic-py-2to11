''' An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method. '''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title() + ".")
        print("Cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurent(self):
        print("The resturant is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def displays_flavors(self):
        print("Ice cream flavors available:")
        for flavor in self.flavors:
            print("- " + flavor)

ice_cream_stand = IceCreamStand("Scoops & swirls", "Ice Cream Parlor")
ice_cream_stand.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip']
ice_cream_stand.describe_restaurant()
ice_cream_stand.displays_flavors()
