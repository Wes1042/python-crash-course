import json
# Load the username, if it has been stored previously
# Otherwise, prompt for the username and store it.
#program is based on 
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f.obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            print("We'll remember you when you come back, " + username + " !")

def greet_user(): 
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + " !")
    else:
        get_new_username()

greet_user()