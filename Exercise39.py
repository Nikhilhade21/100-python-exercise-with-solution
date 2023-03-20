'''Write a program to generate and print another tuple whose values are 
even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).'''


tup = (1,2,3,4,5,6,7,8,9,10)
list = []

for i in tup:
    if i % 2 == 0:
        list.append(i,)

tup1 = tuple(list)
print(tup1,type(tup1))