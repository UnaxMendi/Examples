from tkinter.messagebox import NO
from user import User

class UserManager:
    users=[]

    def addUser(self,newUser):
        if newUser != None and newUser.name!=None and newUser.email!=None and newUser.adress!=None and newUser.age !=0:
            self.users.append(newUser)

    def removeUser(self, position):
        if type(position) == int and len(position)>=0 and len(self.users)!=0 and len(self.users)>position:
            self.users.pop(position)
        
    def updateUser(self, userToBeUpdate):
        return None

    def getUser(self, email):
        return None