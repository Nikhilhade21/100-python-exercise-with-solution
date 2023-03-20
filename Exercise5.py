'''Define a class which has at least two methods: - getString: to get a string
from console input - printString: to print the string in upper case.'''

class IOstring:
    def __init__(self):
        pass
    def get_string(self):
        self.s = input("enter the string:" )
    def print_string(self):
        print(self.s.upper())

xx = IOstring()
xx.get_string()
xx.print_string()