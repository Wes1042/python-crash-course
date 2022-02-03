


class Resturant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0 

    def describe_resturant(self):
        print("The resturant name is " + self.name.title())
        print("type of cuisine is " + self.type)
        print("Number of customers served is " + str(self.number_served))

    def open_resturant(self):
        """Creates the action that the resturant is open"""
        print(self.name.title() + " resturant is open")
    
    def set_number_served(self,served):
        """Sets number serves"""
        self.number_served = served
    def increment_number_served(self,serves):
        """Updates the serves the dinner has done."""
        self.number_served += serves
class IceCreamStand(Resturant):
    """sets a ice cream stand resturant"""
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors
    def picked_flavor(self):
        """Prints out the flavor of the ice cream"""
        print("Your flavor ice cream is " + self.flavors)

# wes_dinner = Resturant("Wesley's dinner","bougie")


# ices = IceCreamStand('Ices INC' , 'ice cream stand' , 'vanilla')
# ices.describe_resturant()
# ices.picked_flavor()

# wes_dinner.describe_resturant()
# wes_dinner.open_resturant()
# print("\n")
# wes_dinner.set_number_served(3)
# wes_dinner.describe_resturant()
# print("\n")
# wes_dinner.increment_number_served(10)
# wes_dinner.describe_resturant()



# donda=Resturant("kanye", "top notch")
# dog = Resturant("Dogs", "woof woof food")
# donda.describe_resturant()
# dog.describe_resturant()
