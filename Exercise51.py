'''Write a function to compute 5/0 and use try/except to catch the exceptions.'''

# try:
#     print(5/0)

# except:
#     print("except")

# way 2

def divide():
    return 5 / 1

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you dividing a number by ZERO!!")

except:
    print("Any other exception")

print("code forward")