'''Define a class, which have a class parameter and have a same instance
 parameter'''

class car:
    name = "car"
    def __init__(self, name=None):
      self.name = name

honda = car("Honda")
print(f"{car.name} name is {honda.name}")

toyota = car()
toyota.name = "Toyata"
print(f"{car.name} name is {toyota.name}")