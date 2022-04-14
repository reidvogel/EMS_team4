#imports



def Login(self):
while True:
    input_role = input('\nAre you a user or admin? :')
    input_user = input('\nPlease log in by providing your user credentials \nUser Name :')
    input_password = input('Password : ')
    role_search = [item for item in list_of_users if item.role == input_role and input_user == list_of_users[item].name][0]
    user_search = [item for item in list_of_users if username in item == input_user]

    if(role_search.role == 'user')
        if (user_search == True):

            if (password_search):
                print('Successfully logged in!')
                print ('Welcome,' + item.user + '! Please choose of the following options by entering the corresponding user menu number.') 
                break;
                print('Your password is not correct. Please try again!')
        else:
            print ('Your username is not correct. Please try again!')
    elif(role_search.role == 'admin'):
        if (password_search):
            print('Successfully logged in!')
            print('Welcome,' + username + '! Please choose of the following options by entering the corresponding menu number.')
            break;
            print('Your password is not correct. Please try again!')
        else:
            print('Your username is not correct. Please try again!')

if __name__ == "__main__":
    User.Login()
