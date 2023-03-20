'''Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized.'''

def user_input():
    while True:
        s = input("enter: ")
        if not s:
            return
        yield s

for line in map(str.upper, user_input()):
    print(line)