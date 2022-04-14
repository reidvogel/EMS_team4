from prog_tracker_classes import *
from admin_options import *
from progress_tracker_login_verification import *
import csv

list_of_users = []

# Administration Main Menu Options
if __name__ == "__main__":
    while True:
        print("""Welcome to the Administration Menu. Please select one of the following options:
        1: See user list
        2: See TV show list
        3: exit""")
    
        option = input("option: ")

        match option:
            case "1": admin_user_menu()
            #case "2": admin_tv_menu()
            case "3": break
            case _: print*("Not a valid input.")
