'''Please write a program using generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is 
input by console.'''


str_num = []
def numdiv(n):
    for i in range(0, n):
        if (i % 5 == 0):
            str_num.append(i)
        elif (i % 7 == 0):
            str_num.append(i)
    print(*(str_num))

n = int(input("enter:"))
numdiv(n)

# way 2

def generate(n):
    for i in range(n + 1):
        if (
            i % 35 == 0
        ):
            yield i

n = int(input("enter: "))
resp = [str(i) for i in generate(n)]
print(",".join(resp))

