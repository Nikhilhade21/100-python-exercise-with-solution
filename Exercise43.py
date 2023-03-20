'''Write a program which can filter() to make a list whose elements are 
even number between 1 and 20 (both included).'''

def even(i):
    return i % 2 == 0

li = [i for i in range(1, 21)]
# print(li)
li2 = filter(even, li)

print(list(li2))

# way 2

def even(x):
    return x % 2 == 0

evenumber = filter(even, range(1, 21))
print(list(evenumber))