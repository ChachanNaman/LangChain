#Class 
#__init__ : used be as constructor in a class 
#self : used as current keyword to map vars
class Car:
    def __init__(self, window,door,engine):
        self.window=window
        self.door=door
        self.engine = engine
    def self_driving(self):
        return "the car is {} type".format(self.engine)

car1 = Car(4,2,"petrol")
print(car1.window)
print(car1.door)
print(car1.engine)
print(car1.self_driving())

