'''Please write a program to generate a list with 5 random numbers between 100
and 200 inclusive.'''

import random
l1 = [i for i in range(100, 201)]
l2 = []

def rannum():
    n = 1
    while(n <= 5):
      l2.append(random.choice(l1))
      n = n + 1

rannum()
print(l2)


# way 2

resp = random.sample(range(100, 201), 5)

print(resp)