'''Write a program which accepts a sequence of words separated by whitespace as
input to print the words composed of digits only.'''

email = input("enter:").split()

ans = [word for word in email if word.isdigit()]

print(ans)