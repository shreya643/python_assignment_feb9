class Uppercase:
    def __init__(self):
        self.str = str

    def get_string(self):
        self.str = input("Enter the string: ")


    def print_string(self):
        print(self.str.upper())


s= Uppercase()
print(s.get_string())
print(s.print_string())