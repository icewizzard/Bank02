


class User:
    def __init__(self, accountnumber, username, password, email, name, age):
        self.accountnumber=accountnumber
        self.username=username
        self.password=password
        self.email=email
        self.name=name
        self.age=age
        self.access_level=1

    def moneytransfer(self):
        pass
    def changename(self, name):
        if True:
            name = input("emter your name:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
            self.name = name

    def changepassword(self, password):
        if True:
            password = input("enter new password:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
            self.password=password
            
    def insertmoney(self):
        pass

    def changeemail(self, email):
        email = input("enter your email:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
        self.email=email        

    def checkbalance(self):
        pass

    def sendmessage(self):
        pass    

class Banker(User(accountnumber, username, password, email, name, age), salary):
    def __init__(self, salary):
        self.access_level=2
        self.salary=salary

    def createuser(self, primary_key, accountnumber, username, password, email, name, age):
        accountnumber = input("number of account:")
        username = input("username of the client:")
        password = input("password of the client:")     #ליצור דף html עם פעולות של הכנסת משתמש
        email = input("email of the client:")           # להוסיף פעולות של הוצאת מספר לקוח מהDB
        name = input("name of the client:")             # להוסיף עוד עמודות לכל DB של לקוח
        age = input("age of the client:")               # להוסיף פעולה של דחיפה של לקוח חדש לDB


    def removemoney(self):
        pass

    def combineusers(self):
        pass

class Manger(Banker(salary), Account(money, currency), position):
    def __init__(self, position):
        self.access_level=3
        self.position=position

    def deleteuser(self):
        pass                    #להוסיף פעולה של מחיקה מהDB USERS

    def createbanker(self):
        accountnumber = input("number of banker:")
        username = input("username of the banker:")
        password = input("password of the banker:")     #ליצור דף html עם פעולות של הכנסת משתמש
        email = input("email of the banker:")           # להוסיף פעולות של הוצאת מספר לקוח מהDB
        name = input("name of the banker:")             # להוסיף עוד עמודות לכל DB של לקוח
        age = input("age of the banker:")               # להוסיף פעולה של דחיפה של בנקאי חדש לDB
        salary = input("salary of banker:")

    def checksalery(self):
        pass

    def deletebanker(self):
        pass                    #להוסיף פעולה של מחיקה מהDB BANKERS

    def schedule(self):
        pass          #להעזר בפרויקט הזה על מנת לבנות לוח עבודה https://github.com/lbiedma/shift-scheduling                    


class Account(User(accountnumber, username, password, email, name, age), money, currency):
    def __init__(self,money,currency):
        self.money=money
        self.currency=currency

