'''Please write a program to print the list after removing even numbers 
in [5,6,77,45,22,12,24].'''


li = [5,6,77,45,22,12,24]
lst = list(filter(lambda n: n % 2 != 0, li))

print(lst)