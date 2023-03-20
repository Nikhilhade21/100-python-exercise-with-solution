# import os


# for i in range(10, 101):
#   fp = open(f"Exercise{i}.py", 'x')
#   fp.close()

''' Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.Suppose
the following input is supplied to the program:'''


'''
#Answer by me
def argu(*arg):
    f = list(arg)
    g = arg
    print(f,type(f),'\n',type(g))

argu(1,2,3,8,5,5,7)
'''

lst = input("Enter values: ").split(",")
tpl = tuple(lst)

print(lst)
print(tpl)