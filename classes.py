


class User:
    def __init__(self, username, password, email, name, age):
        self.username=username
        self.password=password
        self.email=email
        self.name=name
        self.age=age
        self.access_level=1

    def moneytransfer(self):
        pass
    def changename():
        pass

    def changepassword():
        pass

    def insertmoney():
        pass

    def changeemail():
        pass

    def checkbalance():
        pass

    def sendmessage():
        pass    

class Banker(User(username, password, email, name, age), salary):
    def __init__(self, salary):
        self.access_level=2
        self.salary=salary

    def createuser():
        pass

    def removemoney():
        pass

    def combineusers():
        pass

class Manger(Banker(salary), position):
    def __init__(self, position):
        self.access_level=3
        self.position=position

    def deleteuser():
        pass

    def createbanker():
        pass

    def checksalery():
        pass

    def deletebanker():
        pass

    def schedule():
        pass

