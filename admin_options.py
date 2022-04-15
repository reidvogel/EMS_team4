from prog_tracker_classes import *
from class_main_options import *
from login import *
import csv

# add new user(s) to the user list:
def add_user():
    # input username:
    username = input("Enter the username: ")
    for u in list_of_users:
        if u.username == username:
            print("This username is already in use. Please try entering a unique username.")
        else: break
    
    # Input new password:
    password = input("Enter password: ")
    
    # Input role of the new user:
    role = input("Enter 'user' or 'admin': ")
    if role == "user" or "admin": 
        return
    else: print("Error: you must enter 'user' or 'admin'")

    user = User(username, password, role)
    list_of_users.append(user)



# Update/edit existing users:
def admin_update_users():
    # Locate user by entering their username
    username = input("Enter existing user's username: ")
    for u in list_of_users:
        if u.username == username:
            list_of_users == u
            break
        else:
            print("User not found")
            return
    while True:
        # Edit existing username
        username = input("Enter new username: ")
    
        # update password:
        password = input("Enter password: ")

        # Input role of the new user:
        role = input("Enter 'user' or 'admin': ")
        if role == "user" or "admin": 
            return
        else: print("Error: you must enter 'user' or 'admin'")
    
    list_of_users.username = username
    list_of_users.password = password
    list_of_users.role = role


def remove_user():
    # Locate user by entering their username
    username = input("Enter existing user's username: ")
    for u in list_of_users:
        if u.username == username:
            list_of_users == u
            break
        else:
            print("User not found")
            return
    users = [user for user in users if user.username != users]



# Administration User Menu options:
def admin_user_menu():
    while True:
        print("""Select option:
    1: See all users
    2: view user information
    3: Add user information
    4: Edit user information
    5: Remove user information""")

        option = input("option: ")
    
        match option:

            # See all users
            case "1":
                for user in list_of_users: print(user) 
        
            # View user information
            case "2":
                username = input("enter username: ")
                for user in list_of_users:
                    if str(user.username) == username:
                        print(user)
                        break
                    else: print(f"No user with the username {username} was found.")
            # Add user information
            case "3": add_user()
            case "4": admin_update_users()
            case "5": remove_user()
            case _: print("Not a valid input.")