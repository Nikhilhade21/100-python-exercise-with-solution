'''Define a function which can generate a list where the values are square 
of numbers between 1 and 20 (both included). Then the function needs to 
print the last 5 elements in the list.'''

fuct = lambda: ([i ** 2 for i in range(1, 21)][-5:])
print(*(fuct()),sep="\n")

# way 2

def sqrlt():
    list = [i ** 2 for i in range(1, 21)]
    for i in range(19, 14, -1):
        print(list[i])
    # print(*(list[-5:]), sep="\n")

sqrlt()