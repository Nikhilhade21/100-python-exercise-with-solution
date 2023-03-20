'''Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to 
print the first 5 elements in the list.'''

def prtlst():
    lst = [i ** 2 for i in range(1, 21)]
    l = lst[:5]
    print(*(l),sep="\n")

prtlst()

# way 2

func = lambda :([i ** 2 for i in range(1, 21)][:5])
print(*(func()), sep="\n")
