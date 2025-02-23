from abc import ABC,abstractmethod


# bad way........
# class Vehicle:

#     def __init__(self,vehicle_type):
#         self.vehicle_type = vehicle_type

#     def start(self):
#         if self.vehicle_type == "car":
#             print('starting the car')
#         elif self.vehicle_type == "motorcycle":
#             print('starting motorcycle')
#         elif self.vehicle_type == "bicycle":
#             print('starting the bicycle')
#         else:
#             print("invalid vehicle type")


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print('starting the car....')

class Motorcycle(Vehicle):
    def start(self):
        print('starting the motorcycle....')

class Bicycle(Vehicle):
    def start(self):
        print('starting the bicycle....')

class VehicleFactory:
    def __init__(self):
        self.factory = dict(car=Car,motorcycle=Motorcycle,bicycle=Bicycle)

    def create_vehicle(self,vehicle_type):
        if vehicle_type in self.factory:
            vehicle = self.factory.get(vehicle_type)
            return vehicle()
        

factory = VehicleFactory()


car = factory.create_vehicle('car')
car.start()

motorcycle = factory.create_vehicle('motorcycle')
motorcycle.start()