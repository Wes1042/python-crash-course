"""A class that can be used to represent a car"""
class Car():
    """A simple attempt to represent a cat."""

    def __init__(self,make, model , year):
        """Initialize attributes to describe car"""
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0 # << setting a new attribute with a default value

    def get_descriptive_name(self):
        """Return a neatly formative descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """
        Set the odometer to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading: #<< if odometer is greater than or equal to do the following
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self,miles): # << accepting miles
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
# class Battery():
#     """A simple attempt to model a battery for an electric car"""
#     def __init__ (self, battery_size=70):
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")

#     def get_range(self):
#         """print a statement about the range this battery provides"""
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270

#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)

#     def upgrade_battery(self):
#         #self.battery = self.battery_size
#         print("Current Battery capacity is " + str(self.battery_size))
#         if self.battery_size < 85 :
#             self.battery_size = 85
#         print("This battery is now at " + str(self.battery_size) + " Capacity")

# class ElectricCar(Car): 
#     """Represent aspect of a car, specific to electric vehicles"""
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class
#         Then initialize attributes specific to an electric car
#         """
#         super().__init__(make, model, year) #<< similar to sending the data to the parent class
#         self.battery = Battery() #<< get battery from class
#     #     self.battery_size = 70

#     # def describe_battery(self):
#     #     """Print a statement describing the battery size"""
#     #     print("This car has a " + str(self.battery_size) + "-kWh battery.")

#     def fill_gas_tank(null):
#         """Electric cars don't have gas tanks."""
#         print("This car doesn't need a gas tank!")
# # my_new_car = Car('audi' , 'a4' , 2016)
# # print(my_new_car.get_descriptive_name())
# # my_new_car.read_odometer()
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()
# # my_new_car.update_odometer(54)
# # my_new_car.read_odometer()

# # print("\n\n\n")
# # my_used_car = Car('subaru','outback', 2013)
# # print(my_used_car.get_descriptive_name())
# # my_used_car.update_odometer(23500)
# # my_used_car.read_odometer()
# # my_used_car.increment_odometer(100)
# # my_used_car.read_odometer()