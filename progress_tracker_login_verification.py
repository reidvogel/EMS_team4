#imports

class User:

    def __init__(self,username,password,basket,admins, role):
        self.admins=admins
        self.username=username
        self.password=password
        self.basket=basket
        self.role=role

    def menu(self):
        pass


    def Login(self):
        while True:
            input_role = input('\nAre you a user or admin? :')
            input_user = input('\nPlease log in by providing your user credentials \nUser Name :')
            input_password = input('Password : ')
            role_search = [item for item in list_of_users if item.role == 'user']
            user_search = [item for item in username if username in item == input_role_user]

            if(role_search == 'user'):
                input_user = input('\nPlease log in by providing your user credentials \nUser Name :')

                if (user_search == True):

                    if (password_search):
                        print('Successfully logged in!')
                        print ('Welcome,' + item.user + '! Please choose of the following options by entering the corresponding menu number.')
                        global LoggedUserName
                        LoggedUserName = username;
                        return True;
                        User.user_menu()
                        break;
                        print('Your password is not correct. Please try again!')
                else:
                    print ('Your username is not correct. Please try again!')
            elif(self.role=='user'):
                if (password_search):
                    print('Successfully logged in!')
                    print('Welcome,' + username + '! Please choose of the following options by entering the corresponding menu number.')
                    LoggedUserName = username;
                    return True;
                    User.user_menu()
                    break;
                    print('Your password is not correct. Please try again!')
                else:
                    print('Your username is not correct. Please try again!')

if __name__ == "__main__":
    User.Login()