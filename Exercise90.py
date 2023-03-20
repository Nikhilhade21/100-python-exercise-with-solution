'''Please write a program which count and print the numbers of each character 
in a string input by console.'''


import string

s = input("enter the string:")
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print("{}, {}".format(letter, cnt))

