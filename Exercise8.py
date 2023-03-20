'''Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alpha
betically.'''


j = input("enter: ").split(",")
j.sort()
print(",".join(j))