'''Write a program that accepts a sentence and calculate the number 
of upper case letters and lower case letters.
'''

word = input("enter:")
letter, digit = 0, 0

for i in word:
    if i.isupper():
        letter += 1
    elif i.isnumeric():
        digit += 1
print(f"Upper {letter =}")