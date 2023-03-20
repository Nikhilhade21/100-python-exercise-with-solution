'''Write a program to solve a classic ancient Chinese puzzle: We count 35 heads
and 94 legs among the chickens and rabbits in a farm. How many rabbits and
how many chickens do we have?'''

total_leg = 94
heads_chickens = 35

chickens = total_leg - (heads_chickens * 2)
rabbits = 24 / 4

print(f"the total number of rabbits is {int(rabbits)} and chickens is {heads_chickens}")

# way 2

def solve(numheads, numlegs):
    ns = "No solution"
    for i in range(numheads + 1):
        j = numheads
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)
print(solution)