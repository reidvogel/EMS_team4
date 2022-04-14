from prog_tracker_classes import User
import csv


# add new user(s) to the user list:
def add_user():
    # input username:
    username = input("Enter the username: ")
    
    # Input new password:
    password = input("Enter password: ")
    
    # Input role of the new user:
    role = input("Enter 'user' or 'admin': ")
    if role != "user" or "admin":
        print("Error: you must enter 'user' or 'admin'")
    else: return





# Update/edit existing users:
def admin_update_users():
    user = input("Enter existing user's username: ")
    for u in list_of_users:



# Administration User Menu options:
def admin_user_menu():
    option = input("""Select option:
    1: See all users
    2: view user information
    3: Add user information
    4: Edit user information
    5: Remove user information""")


    match option:

        # See all users
        case "1":
            for user in user_list: print(user) 
        
        # View user information
        case "2":
            username = input("enter username: ")
            for user in user_list:
                if str(user.username) == username:
                    print(user)
                    break
                else: print(f"No user with the username {username} was found.")
        # Add user information
        case "3": add_user()
        case "4": admin_update_users()
        case _: print("Not a valid input.")


# Administration Main Menu Options
if __name__ == "%_admin":
    while True:
        print("""Welcome to the Administration Menu. Please select one of the following options:
        1: See user list
        2: See TV show list
        3: exit""")
    
        option = input("option: ")

        match option:
            case "1": admin_user_menu()
            case "2": admit_tv_menu()
            case "3": break
            case _: print*("Not a valid input.")
    