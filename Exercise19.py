'''You are required to write a program to sort the (name, age, score) tuples by
ascending order where name is string, age and score are numbers. The tuples
are input by console. The sort criteria is:
1. Sort based on name
2. Then sort based on age
3. Then sort by score'''

lst = []

while True:
    s = input("enter: ").split(",")
    if not s [0]:
        break
    lst.append(tuple(s))

lst.sort(
    key=lambda x: (x[0], x[1], x[2])
)

print(lst)