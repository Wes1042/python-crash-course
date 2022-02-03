class Users(): # << initializing base clase(parent)
    def __init__(self,first_name,last_name,age,email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    
    def describe_user(self): # Using a constructor
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.age)
        print(self.email)

    def greet_users(self):
        print("Hello " + self.first_name.title() +" " + self.last_name.title())
    
class Admin(Users): # Creating a User specification (child)
    def __init__(self, first_name, last_name, age, email,):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()

class Privileges(Users): # Creating a place holder for priviledges for insances(child)
    def __init__(self, privileges=[]):
        self.privileges = []

    def show_privileges(self):
            """Prints out priveleges"""
            for x in self.privileges:
                print("This user " + x)
            # print("\n This user ".join(self.priviledges ))



# wes = Admin("Wesley", "T" , 19 , "test@test.com")
# wes.describe_user()
# wes.greet_users()
# wes.privileges.privileges = [
#     "can add post",
#     "can delete post",
#     "can ban users"]
# wes.privileges.show_privileges()



