'''Write a program to compute: f(n) = f(n - 1) + 100, n>0 with a given n
input by console (n¿0).'''

def f(n):
    if n == 0:
      return 0
    return f(n -1) + 100

n = int(input("enter: "))
print(f(n))