'''Write a program that accepts a sentence and calculate the number of letters
and digits.
'''

word = input("enter:")
letter, digit = 0, 0

for i in word:
    if i.isalpha():
        letter +=1
    elif i.isnumeric():
        digit += 1
print(f"{letter = }\n{digit =}")
