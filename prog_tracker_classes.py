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

def check_int():
    #This function checks if an input was an int type
    while True:
        try:
            arg = int(input())
            result = isinstance(arg, int)
            if result is True: return arg
        except ValueError:
            print("Please enter an integer")

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
    def addShow(self, show):
        while True:
            try:
                Show.ListShows
                print("Please enter the number corresponding to the show you would like to add to your list")
                index = check_int()
                if index not in range(len(Show.ListShows)): raise Exception
                show = Show.ListShows[index]
                self.shows.append(show)
                self.shows_prog.append(0) #automatically 0
            except Exception: print("That is not a valid option")
        
    def delShow(self, show):
        while True:
            try:
                self.showList
                print("Please enter the number of the show you would like to remove from your list")
                index=check_int()
                if index not in range(len(self.showList)): raise Exception
                index = self.shows.pop(show.name) #delete the show and grab it's index
                del self.shows_prog[index] #remove the progress from this list as well
            except Exception: print("That is not a valid option")

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
        for i in self.shows:
            print(f"{i+1}: {self.shows[i]}") #Gotta account for index starting at 0
    def showListandProg(self):
        print("These are the shows you are currently watching and your progress: ")
        for i in self.shows:
            progress = (self.shows_prog[i] / self.shows.ep[i]) * 100 
            if progress == 0:
                marker = 'not started'
            elif progress == 100:
                marker = 'completed'
            else: marker=='in progress'
            print(f"{i+1}: {self.shows.name[i]}, Progress: {marker}: {progress}%") #Gotta account for index starting at 0
            #pb.print_progress_bar(progress)
    def updateShowProg(self):
        while True:
            try:
                self.showListandProg()
                print("Please enter the number corresponding to the show you would like to update progress: ")
                index = check_int()
                index = index - 1 #Gotta account for index starting at 0
                if index not in range(len(list_of_shows)): raise Exception
                print(f"Enter the number of episodes you have watched for {self.shows[index]}")
                self.shows_prog[index] = check_int() #maybe check it's not more than episodes available
            except Exception: print("That is not a valid input")

           
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
                self.ListShows()
                print("Please enter the number corresponding to the show you would like to update: ")
                index = check_int()
                if index not in range(len(list_of_shows)): raise Exception
                list_of_shows.remove(self)
                print(f"{self.name} removed from List of Available Shows")
            except Exception: print("That is not a valid input")
    def ListShows(self):
        print("Here are all the available shows")
        for i in list_of_shows:
            print(f"{i}: {list_of_shows[i]}")
    def UpdateShow(self): #used to change number of episodes
        while True:
            try:
                self.ListShows()
                print("Please enter the number corresponding to the show you would like to update: ")
                index = check_int()
                if index not in range(len(list_of_shows)): raise Exception
                list_of_shows[index].ep = check_int()
                print(f"The number of episodes for {list_of_shows[index]} is now {list_of_shows[index].ep}")
            except: Exception: print("That is not a valid input")
        

for i in users_import:
    print(i)
    username = i[0]
    password = i[1]
    role = i[2]
    new_user = User(username, password, role)
    User.addUser(new_user)
for i in shows_import:
    title = i[0]
    ep = i[0]
    new_show = Show(title,ep)
    Show.addShow(new_show)

