import csv
#from progressbar import *

#pb = ProgressBar(total=100,prefix='Here', suffix='Now', decimals=3, length=50, fill='=', zfill='-')
with open(r"teamproj\users.csv") as file:
    headers_users = next(file)
    users_import = list(csv.reader(file))
with open(r'teamproj\shows.csv') as file:
    headers_shows = next(file)
    shows_import = list(csv.reader(file))
list_of_users = []
list_of_shows = []
class IndexException(Exception): pass
def check_int():
    #This function checks if an input was an int type
    while True:
        try:
            arg = int(input())
            result = isinstance(arg, int)
            if result is True: return arg
        except ValueError:
            print("Please enter an integer")
def check_role():
    while True:
        try:
            role = input()
            if role == 'user' or role == 'admin':
                return role
            else: raise Exception 
        except Exception: print("Please enter either 'admin' or 'user'")

class User():
    def __init__(self, username, password, role):
        self.name = username
        self.password = password
        self.shows = [] 
        self.shows_prog = [] #This is the number of episodes the user has seen
        self.role = role #user or admin
    def addUser(self): #This is used by sign up or admin
        list_of_users.append(self)
    def delUser(self): 
        list_of_users.remove(self)
    def listUsers(self):
        print("These are the current users: ")
        for i in list_of_users:
            print(f"Username: {i.name}, Role: {i.role}")
    def addShow(self):
        while True:
            try:
                Show.ListShows(Show)
                print("Please enter the number corresponding to the show you would like to add to your list")
                index = check_int()
                index = index -1 #account for starting at 0
                if index in range(len(list_of_shows)): 
                    show = list_of_shows[index]
                    self.shows.append(show)
                    self.shows_prog.append(0) #automatically 0
                    print(f"{show.name} added to {self.name}'s list")
                    return
                else:raise IndexException
            except IndexException: print("That is not a valid option")
        
    def delShow(self):
        while True:
            try:
                self.showList()
                print("Please enter the number of the show you would like to remove from your list")
                index=check_int() 
                index = index - 1 #account for starting at 0
                if index in range(len(self.shows)): 
                    show = self.shows[index]
                    del self.shows[index]
                    del self.shows_prog[index] #remove the progress from this list as well\
                    print(f"{show.name} removed from {self.name}'s list")
                    return
                else: raise IndexException
            except IndexException: print("That is not a valid option!")

    def editUser(self):
        while True:
            try:
                print("To update username, press 1\nTo update password, press 2")
                var = check_int()
                if var == 1: #Username
                    print("Please enter a new username: ")
                    self.name = input()
                    return
                elif var == 2: #Password
                    print(f"Please enter a new password for {self.name}: ")
                    self.password = input()
                    return
                else: raise Exception
            except Exception: print("Please enter a valid option")
    def showList(self):
        print(f"These are the shows currently on {self.name}'s list: ")
        for i in range(len(self.shows)):
            print(f"{i+1}: {self.shows[i].name}") #Gotta account for index starting at 0
    def showListandProg(self):
        print("These are the shows you are currently watching and your progress: ")
        for i in range(len(self.shows)):
            if self.shows_prog[i] == 0:
                progress = 0
                marker = 'not started'
            elif self.shows_prog[i] == self.shows[i].ep:
                progress = 100
                marker = 'completed'
            else: 
                progress = round((self.shows_prog[i] / self.shows[i].ep) * 100 ,2)
                marker = 'in progress'
            print(f"{i+1}: {self.shows[i].name}, Progress: {marker}: {progress}%") #Gotta account for index starting at 0
            #pb.print_progress_bar(progress)
        return
    def updateShowProg(self):
        while True:
            try:
                self.showListandProg()
                print("Please enter the number corresponding to the show you would like to update progress: ")
                index = check_int()
                index = index - 1 #Gotta account for index starting at 0
                if index not in range(len(list_of_shows)): raise IndexException
                print(f"Enter the number of episodes you have watched for {self.shows[index].name}")
                self.shows_prog[index] = check_int() #maybe check it's not more than episodes available
                return
            except IndexException: print("That is not a valid input!!!")

           
class Show():
    def __init__(self, name, episodes):
        self.name = name
        self.ep = episodes
    def addShow(self):
        list_of_shows.append(self)
        print(f"{self.name} added to List of Available Shows")
    def delShow(self):
        while True:
            try:
                self.ListShows(self)
                print("Please enter the number corresponding to the show you would like to remove: ")
                index = check_int()
                index = index-1#account for starting at 0
                if index in range(len(list_of_shows)):
                    show = list_of_shows[index]
                    list_of_shows.remove(show)
                    print(f"{show.name} removed from List of Available Shows")
                    return
                else: raise Exception
            except Exception: print("That is not a valid input!")
    def ListShows(self):
        print("Here are all the available shows")
        for i in range(len(list_of_shows)):
            print(f"{i+1}: {list_of_shows[i].name} - {list_of_shows[i].ep} Episodes")
        return
    def UpdateShow(self): #used to change number of episodes
        while True:
            try:
                self.ListShows(self)
                print("Please enter the number corresponding to the show you would like to update: ")
                index = check_int()
                index = index -1 #account for starting at 0
                if index in range(len(list_of_shows)): 
                    show = list_of_shows[index]
                    print(f"Please enter the new number of episodes for {show.name}")
                    list_of_shows[index].ep = check_int()
                    print(f"The number of episodes for {list_of_shows[index].name} is now {list_of_shows[index].ep}")
                    return
                else:raise Exception
            except: Exception: print("That is not a valid input")
            return
        

for i in users_import:
    print(i)
    username = i[0]
    password = i[1]
    role = i[2]
    new_user = User(username, password, role)
    User.addUser(new_user)
for i in shows_import:
    title = i[0]
    ep = int(i[1])
    new_show = Show(title,ep)
    Show.addShow(new_show)

