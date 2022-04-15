from prog_tracker_classes import *
from admin_options import *
from login import *
import csv

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