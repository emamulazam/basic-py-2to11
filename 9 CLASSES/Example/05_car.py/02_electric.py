"A set of classes that can be used to represent electric cars."

from car import Car

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

my_tesla = ElectrucCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()