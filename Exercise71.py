'''Please write a program to output a random number, which is divisible 
by 5 and 7, between 10 and 150 inclusive using random module and list 
comprehension'''

import random

lst = [i for i in range(10, 150) if i % 35 ==0]
print(lst)
print(random.choice(lst))
