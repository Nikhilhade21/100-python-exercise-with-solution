'''The Fibonacci Sequence is computed based on the following formula:
f(0)=0,
f(1)=1,
f(n) = f(n - 1) + f(n - 2), n > 1
Please write a program to compute the value of f(n) with a given n input by
console and prints all the values all along.'''

def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n - 1) + f(n - 2)
    return fibo[n]

n = int(input("enter:"))
fibo = [0] * (n + 1)

f(n)
fibo = [str(i) for i in fibo]
ans = ",".join(fibo)
print(ans)