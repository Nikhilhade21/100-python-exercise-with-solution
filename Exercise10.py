'''Write a program that accepts a sequence of whitespace separated words as
input and prints the words after removing all duplicate words and sorting them
alphanumerically'''

word = sorted(
    list(set(input("enter: ").split()))
    )

print(" ".join(word))