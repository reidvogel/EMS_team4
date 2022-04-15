from login import *
from classes import *
import csv

#Log in first and get user object
user = Login()

# Administration User Menu options:
def admin_user_menu():
    while True:
        try:
            print("Welcome to the Admin User Menu. What would you like to do?")
            print("To View all Users, press 1")
            print("To add a new user, press 2")
            print("To edit a specific user, press 3")
            print("To delete a specific user, press 4")

            option = check_int()
            if option == 1:
                User.listUsers(User)
            elif option == 2:
                username = input("Enter the username: ")
                password = input("Enter the password: ")
                role = check_role()
                new_user = User(username, password, role)
                User.addUser(new_user)
            elif option == 3:
                while True:
                    try: 
                        User.listUsers(User)
                        username = input("Which user would you like to edit? ")
                        if username in [user.name for user in list_of_users]:
                            user = [user for user in list_of_users if user.name == username][0]
                            User.editUser(user)
                            print(f"{user.name} updated")
                            break
                        else: raise Exception
                    except Exception: print("That is not a valid username")
            elif option == 4:
                while True:
                    try: 
                        User.listUsers(User)
                        username = input("Which user would you like to remove? ")
                        if username in [user.name for user in list_of_users]:
                            user = [user for user in list_of_users if user.name == username][0]
                            User.delUser(user)
                            print(f"{username} removed")
                            break
                        else: raise Exception
                    except Exception: print("That is not a valid username")
            else: raise Exception
        except Exception: print("That is not a valid input")
# Administration Shows Menu options:
def admin_tv_menu():
    print("""Select option:
    1: View All TV Show
    2: Add New TV Show
    3: Remove Specific TV Show
    4: Edit Specific TV Show""")
    option = check_int()
    match option:

        # See all tv shows
        case 1:
            Show.ListShows(Show)
        # Add user information
        case 2:
            title = input("Please enter the title of the new show:")
            print(f"Enter the total number of episodes in {title}")
            ep = check_int()
            new_show = Show(title,ep)
            Show.addShow(new_show)
        #delete show
        case 3:
            Show.delShow(Show)
        case 4:
        #edit tv show
            Show.UpdateShow(Show)
        case _:
            print("Not a valid input.")

# Administration Main Menu Options:
def admin_menu(user):
    
    print(f"""Welcome to the Administration Menu {user.name}. Please select one of the following options:
    1: Users
    2: TV Shows
    3: exit""")
    
    option = input("option: ")

    match option:
        case "1": admin_user_menu()
        case "2": admin_tv_menu()
        case "3": pass    
        case _: print*("Not a valid input.")

#User Main menu options:
def user_menu(user):
    while True:
        try:
            print(f"Welcome to the user menu {user.name}. What would you like to do?")
            print("To edit your username or password, press 1")
            print("To View your current shows, press 2")
            print("To add a new show, press 3")
            print("To edit your progress on a current show, press 4")
            print("To remove a show from your list, press 5")
            option = check_int()
            if option == 1:
                User.editUser(user)
            elif option == 2:
                User.showList(user)
            elif option == 3:
                User.addShow(user)
            elif option == 4:
                User.updateShowProg(user)
            elif option == 5:
                User.delShow(user)
            else: raise Exception
        except Exception: print("That is not a valid option")
#This is the big main function that calls the admin/ user menus
if user.role == "admin":
    admin_menu(user)
else: user_menu(user)