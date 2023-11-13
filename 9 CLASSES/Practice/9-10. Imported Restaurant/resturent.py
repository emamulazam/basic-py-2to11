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

