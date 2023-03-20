'''Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence'''

data = input("enter: ").split(",")
data = list(
    filter(lambda i: int(i, 2) % 5 ==0, data)
)

print(",".join(data))