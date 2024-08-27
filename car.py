class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

ferrari = Car("blue", 20000)
buggati = Car("red", 30000)
print(ferrari)
print(buggati)
for car in (buggati, ferrari):
    print(car)