'''Define a class named Circle which can be constructed by a radius. The 
Circle class has a method which can compute the area.'''

class Circle:
    def area(r):
        return 3.14 * (r * r)
    
circle = Circle

print(circle.area(5))

# way 2

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return 3.1416 * (self.radius ** 2)
    
circle = Circle(5)
print(circle.area())