from login import Login
import csv


Login()



list_of_users = []

# Administration Main Menu Options:
def admin_menu(User):
    
    print("""Welcome to the Administration Menu. Please select one of the following options:
    1: See user list
    2: See TV show list
    3: exit""")
    
    option = input("option: ")

    match option:
        case "1": User.admin_user_menu()
        case "2": User.admin_tv_menu()
        case "3": pass    
        case _: print*("Not a valid input.")


def user_menu(user):
    while True:
        try:
            print("Welcome to the user menu. What would you like to do?")
            print("To edit your username or password, press 1")
            print("To View your current shows, press 2")
            print("To add a new show, press 3")
            print("To edit your progress on a current show, press 4")
            print("To remove a show from your list, press 5")
            option = input()
            if option == 1:
                user.editUser
            elif option == 2:
                user.showList
            elif option == 3:
                user.AddShow
            elif option == 4:
                user.updateShowProg
            elif option == 5:
                user.delShow
            else: raise Exception
        except Exception: print("That is not a valid option")