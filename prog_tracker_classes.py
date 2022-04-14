class User():
    list_of_users = []
    def __init__(self, username, password, role):
        self.name = username
        self.password = password
        self.shows = []
        self.shows_prog = []
        self.role = role #user or admin
    def addUser(self): #This is used by sign up or admin
        User.list_of_users.append(self)
    def delUser(self): 
        User.list_of_users.remove(self)
    def addShow(self, show):
        self.shows.append(show)
    def delShow(self, show):
        self.shows.remove(show)

    def editUser(self, var):
        '''var is what they want to update'''
        if var == 1:
            print("Please enter a new username: ")
            self.name = input()
        elif var == 2:
            print(f"Please enter a new password for {self.name}: ")
            self.password = input()
    def showList(self):
        print(f"These are the shows currently on {self.name}'s list: ")
        for i in self.shows:
            print(f"{i+1}: {self.shows[i]}") #Gotta account for index starting at 0
    def showListandProg(self):
        print("These are the shows you are currently watching and your progress: ")
        for i in self.shows:
            print(f"{i+1}: {self.shows[i]}, Progress: {self.shows_prog[i+1]}") #Gotta account for index starting at 0
    def updateShowProg(self):
        self.showListandProg()
        print("Please enter the number corresponding to the show you would like to update progress: ")
        index = input() - 1 #Gotta account for index starting at 0
        print(f"Enter the number of episodes you have watched for {self.shows[index]}")
        self.shows_prog[index] = input() #maybe check it's not more than episodes available
        
    
  
            




def Show():
    list_of_shows = []
    def __init__(self, name, episodes):
        self.name = name
        self.ep = episodes
    def addShow(self):
        Show.list_of_shows.append(self)



