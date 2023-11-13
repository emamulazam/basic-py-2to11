"A set of classes used to represent gas and electric cars."

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    "A simple attempt to model a battery for a electric car."

    def __init__(self, battery_size=70):
        "Initialize the battery's attributes."
        self.battery_size = battery_size

    def describe_battery(self):
        "Print a statment describing the battery size."
        print("The car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        "Print a statment about the range the range this battery provides."
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "The car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectrucCar(Car):
    "Represent aspects of a car, specific to electric vehicles."

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()