'''Define a function which can generate and print a tuple where the 
value are square of numbers between 1 and 20 (both included).'''

fuct = lambda:((i ** 2 for i in range(1, 21)))
t = type(fuct)
print(*fuct(),t)

# way 2

def sq_of_num():
    return tuple(i ** 2 for i in range(1, 21))

print(sq_of_num())