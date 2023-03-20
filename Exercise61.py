'''The Fibonacci Sequence is computed based on the following formula:
f(0)=0,
f(1)=1,
f(n) = f(n - 1) + f(n - 2), n > 1
Please write a program to compute the value of f(n) with a given n input by
console.'''

def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

n = int(input("enter:"))
print(f(n))
