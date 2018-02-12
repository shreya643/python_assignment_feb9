class Uppercase:
    def __init__(self):
        self.str = str

    def get_string(self):
        self.str = input("Enter the string: ")


    def print_string(self):
        print(self.str.upper())


p= Uppercase()
print(p.get_string())
print(p.print_string())