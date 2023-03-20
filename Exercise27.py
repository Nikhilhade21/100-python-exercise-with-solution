'''Define a function that can convert a integer into a string and print it in
console.'''

def strnum(num):
    n = str(num)
    print(n,type(n))

strnum(5)

# way 2

conv = lambda x: str(x)

n = conv(10)
print(n)
print(type(n))