from prog_tracker_classes import *

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
                user.showListandProg
            elif option == 3:
                user.AddShow
            elif option == 4:
                user.updateShowProg
            elif option == 5:
                user.delShow
            else: raise Exception
        except Exception: print("That is not a valid option")
        
