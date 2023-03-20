'''Write a program which takes 2 digits, X, Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be
i j.
'''

x, y = map(int, input("enter the value: ").split(","))
print(x)
lst = [[i *  j for j in range(y)] for i in range(x)]
print(lst)

