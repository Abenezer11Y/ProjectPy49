from abc import ABC, abstractmethod

class Vehicle(ABC):
    def move(self):
        pass
class Car(Vehicle):
    def speed_ridablility(self):
        print("I can reach upto 531km/h on land")
class Boat(Vehicle):
    def speed_ridablility(self):
        print("I can reach upto 511km/h on water")
class Airplain(Vehicle):
    def speed_ridablility(self):
        print("I can reach upto 4,000 km/h on air")

C = Car()
C.speed_ridablility()

B = Boat()
B.speed_ridablility()

A = Airplain()
A.speed_ridablility()