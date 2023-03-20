'''Define a custom exception class which takes a string message as attribute'''

class CustomeException(Exception):
    """Exception raised for custom purpose

    Attribute:
      message -- explanation of error
      """
    
    def __init__(self, message):
        self.message = message

num = int(input("enter:"))
try:
    if num < 10:
        raise CustomeException("Input is less than 10")
    elif num > 10:
        raise CustomeException("Input is grater than  10")
except CustomeException as ce:
    print("the error raised: " + ce.message)
