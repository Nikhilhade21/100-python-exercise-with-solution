'''Please write a program to print the running time of execution of ”1+1” for 100 times.'''

import time

before = time.time()

for i in range(100):
    x = 1 + 1
    print (x)

after = time.time()
exection_time = after - before

print(exection_time)