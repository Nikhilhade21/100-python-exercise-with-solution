'''Define a class with a generator which can iterate the numbers, which are divisible
by 7, between a given range 0 and n.'''


class MyGen:
    def by_seven(self, n):
        for i in range(0, int(n / 7) + 1):
            yield i * 7

for i in MyGen().by_seven(int (input("please enter a number... "))):
    print(i)