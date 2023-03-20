'''A website requires the users to input username and password to register. Write
a program to check the validity of password input by users. Following are the
criteria for checking the password:
• At least 1 letter between [a-z]
• At least 1 number between [0-9]
• At least 1 letter between [A-Z]
• At least 1 character from [$#@]
• Minimum length of transaction password: 6
• Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria
are to be printed, each separated by a comma.'''

def is_low(x):
    for i in x:
        if "a" <= i and i <= "z":
            return True
    return False

def is_up(x):
    for i in x:
        if "A" <= i and i <= "Z":
            return True
    return False

def is_num(x):
    for i in x:
        if "0" <= i and i <= "9":
            return True
    return False

def is_other(x):
    for i in x:
        if  i == "$" or i == "#" or i == "@":
            return True
    return False

s = input("enter:").split(",")
lst = []

for i in s:
    length = len(i)
    if (
        6 <= length
        and length <= 12
        and is_low(i)
        and is_up(i)
        and is_num(i)
        and is_other(i)
    ):
      lst.append(i)

print(",".join(lst))