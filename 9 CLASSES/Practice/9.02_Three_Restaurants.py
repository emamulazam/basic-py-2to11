''' Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance. '''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title() + ".")
        print("Cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurent(self):
        print("The resturant is open.")

me = Restaurant("DC", "desi")
you = Restaurant("ms", "chy")
he = Restaurant("mo", "bidesi")

me.describe_restaurant()
you.describe_restaurant()
he.describe_restaurant()