'''With a given tuple def (1,2,3,4,5,6,7,8,9,10), write a program to print 
the first half values in one line and the last half values in one line.'''

tup = (1,2,3,4,5,6,7,8,9,10)

def prttup():
     print(tup[0:5])
     print(tup[5:11])

prttup()

# way 2

tup = (1,2,3,4,5,6,7,8,9,10)

lt = int(len(tup) / 2)
print(tup[:lt], tup[lt:])