'''Define a function that can receive two integer numbers in string form
and compute their sum and then print it in console.
'''


def strsum(n1, n2):
    print(int(n1) + int(n2))


l = input("enter:")
ll = input("enter:")
strsum(l, ll)

# way 2

strsum = lambda n1, n2: int(n1) + int(n1)
print(strsum(input("entet"),input("enter:")))