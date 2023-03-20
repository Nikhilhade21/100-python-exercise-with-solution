'''Define a function that can accept two strings as input and print the string
with maximum length in console. If two strings have the same length, then the
function should print all strings line by line.'''


def strtwo(s1, s2):
    k1 = len(s1)
    k2 =  len(s2)
    if k1 > k2:
        print(s1)
    elif k2 > k1:
        print(s2)
    elif k1 == k2:
       print(s1 +"\n" + s2)
    else:
        print("error:")

strtwo("nikhil", "hadehj")

# way 2

fun = (
    lambda a, b: print(max((a, b), key=len))
    if len(a) != len(b)
    else print(a + "\n" + b)
)

fun("nikhil", "hadehh")