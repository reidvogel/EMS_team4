from tabnanny import check
from prog_tracker_classes import *

def admin_user_menu(user):
    while True:
        try:
            print("Welcome to the Admin User Menu. What would you like to do?")
            print("To View all Users, press 1")
            print("To add a new user, press 2")
            print("To edit a specific user, press 3")
            print("To delete a user, press 4")

            option = check_int()
            if option == 1:
                User.listUsers(User)
            elif option == 2:
                username = input("Enter the username: ")
                password = input("Enter the password")
                role = input("user or admin?")
                User.addUser(username, password, role)
            elif option == 3:
                while True:
                    try: 
                        User.listUsers(User)
                        username = input("Which user would you like to edit? ")
                        if username in [user.name for user in list_of_users]:
                            user = [user for user in list_of_users if user.name == username][0]
                            user.editUser
                        else: raise Exception
                    except Exception: print("That is not a valid username")
            elif option == 4:
                while True:
                    try: 
                        User.listUsers(User)
                        username = input("Which user would you like to edit? ")
                        if username in [user.name for user in list_of_users]:
                            user = [user for user in list_of_users if user.name == username][0]
                            user.delUser
                        else: raise Exception
                    except Exception: print("That is not a valid username")
            else: raise Exception
        except Exception: print("That is not a valid input")

