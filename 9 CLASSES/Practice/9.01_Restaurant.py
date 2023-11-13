''' Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods. '''

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
print("Restaurant Name:", me.restaurant_name)
print("Cuisine Type:", me.cuisine_type)

me.describe_restaurant()
me.open_restaurent()