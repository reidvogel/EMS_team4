#imports
from prog_tracker_classes import *

#classes
class UsernameException(Exception): pass
class PasswordException(Exception): pass


#functions
def check_username(input_role):
    while True:
        try:
            input_user = input('\nPlease log in by providing your user credentials \nUser Name :')
            if input_user in [user.name for user in list_of_users]:
                user = [user for user in list_of_users if user.name == input_user][0]
                return user
            else: raise UsernameException
        except UsernameException:
            print("That is not a valid username")

def check_password(user):
    while True:
        try:
            input_password = input("Please enter your password")
            if input_password == user.password:
                return
            else: raise PasswordException
        except PasswordException: print("That password is incorrect")

    
    
def Login():
    while True:
        #input_role = input('\nAre you a user or admin? :')
        user = check_username()
        check_password(user)
        
        return user
