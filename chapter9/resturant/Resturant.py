

class Resturant():
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_resturant(self):
        print("The resturant name is " + self.name.title())
        print("type of cuisine is " + self.type)

    def open_resturant(self):
        print(self.name.title() + " resturant is open")


wes_dinner = Resturant("Wesley's dinner","bougie")
donda=Resturant("kanye", "top notch")
dog = Resturant("Dogs", "woof woof food")

wes_dinner.describe_resturant()
wes_dinner.open_resturant()

donda.describe_resturant()
dog.describe_resturant()
