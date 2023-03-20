'''With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a 
program to make a list whose elements are intersection of the above given lists.
'''

li1 = [1,3,43,6,78,55,35]
li2 = [12,24,35,24,88,120,55,43]

set1 = set(li1)
set2 = set(li2)

intersection = set.intersection(set1, set2)
print(intersection)

# way2

for i in li1:
    for t in li2:
        if i == t:
            print(i)