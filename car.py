# Python

class Wheel:
    def __init__(self):
        self.price = 100

class Seat:
    def __init__(self):
        self.price = 200

class Engine:
    def __init__(self):
        self.price = 5000

class Vehicle:
    def __init__(self):
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        self.seats = [Seat(), Seat(), Seat(), Seat()]
        self.engine = Engine()

    def price(self):
        return sum(wheel.price for wheel in self.wheels) + sum(seat.price for seat in self.seats) + self.engine.price

class Sedan(Vehicle):
    pass

class Coupe(Vehicle):
    def __init__(self):
        super().__init__()
        self.seats = [Seat(), Seat()]

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = [Wheel(), Wheel()]
        self.seats = [Seat()]

vehicles = [Sedan(), Coupe(), Motorcycle()]
for vehicle in vehicles:
    print(vehicle.price())