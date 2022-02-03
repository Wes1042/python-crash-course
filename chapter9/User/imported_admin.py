from Admin import Admin

wes = Admin("Wesley", "T" , 19 , "test@test.com")
wes.describe_user()
wes.greet_users()
wes.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban users"]
wes.privileges.show_privileges()