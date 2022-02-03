

class Users():
    def __init__(self,first_name,last_name,age,tier):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.tier = tier
        self.login_attempts = 0 
    
    def describe_user(self):
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.age)
        print(self.tier)

    def greet_users(self):
        print("Hello " + self.first_name.title() +" " + self.last_name.title())

    def increment_attempts(self):
        """Increments the value login attempts by 1 """
        self.login_attempts += 1 
    def reset_login_attempts(self):
        self.login_attempts = 0 


wes = Users("Wesley", "T" , 19 , 5)
wes.increment_attempts()
print("This user has attempted to logging " + str(wes.login_attempts) + " many times") 

wes.describe_user()
wes.greet_users()
wes.reset_login_attempts()
print("This user has attempted to logging " + str(wes.login_attempts) + " many times") 



# finn = Users("Finn" , "The human" , 15 , 2)
# finn.describe_user()
# finn.greet_users()