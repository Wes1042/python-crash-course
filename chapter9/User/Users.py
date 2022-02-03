

class Users():
    def __init__(self,first_name,last_name,age,tier):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.tier = tier
    
    def describe_user(self):
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.age)
        print(self.tier)

    def greet_users(self):
        print("Hello " + self.first_name.title() +" " + self.last_name.title())

wes = Users("Wesley", "T" , 19 , 5)
wes.describe_user()
wes.greet_users()

finn = Users("Finn" , "The human" , 15 , 2)
finn.describe_user()
finn.greet_users()