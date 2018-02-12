class Student:
    def __init__(self):
        self.fname=""
        self.lname =""

    def get_email(self):
        self.email = self.fname + "." + self.lname + "@gmail.com"
        return self.email.lower()

    def get_name(self):
        self.fname=input("enter the first name: ")
        self.lname=input("enter the last name: ")


s= Student()
s.get_name()
print(s.get_email())