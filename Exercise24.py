'''Please write a program to print some Python built-in functions documents,
such as abs(), int(), raw input(). And add document for your own function'''

def pow(n, p):
    """
    param n: This is any integer number 
    param p: This is power over n
    return: n to the power p = n `p
    """

    return n ** p

print(pow(3, 4))
print(pow.__doc__)