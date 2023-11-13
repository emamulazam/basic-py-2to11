''' Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business. '''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title() + ".")
        print("Cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurent(self):
        print("The resturant is open.")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You cannot set the number served to a lower value.")

    def increment_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print("You cannot increment the number served by a neagative value.")

restaurant = Restaurant("The Food Haven", "Italian")
print("Numver of customer served:", restaurant.number_served)

# Change the number of customers served and print it again
restaurant.number_served = 50
print(f"Updated number of customers served: {restaurant.number_served}")

# Use the set_number_served() method to set the number served
restaurant.set_number_served(100)
print(f"Updated number of customers served: {restaurant.number_served}")

# Use the increment_number_served() method to increment the number served
restaurant.increment_number_served(20)
print(f"Updated number of customers served: {restaurant.number_served}")

