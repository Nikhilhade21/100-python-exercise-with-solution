'''Write a program which can compute the factorial of a given numbers.The 
results should be printed in a comma-separated sequence on a single line.
Supposethe following input is supplied to the program: 8 Then, the output
 should be:40320'''


n = int(input("enter  a number: "))

fact = 1

for i in range(1, n+1):
    fact = fact * i
print(fact)