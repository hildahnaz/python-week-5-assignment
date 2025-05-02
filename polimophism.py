class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "The car drives on the road."

class Boat(Vehicle):
    def move(self):
        return "The boat sails on the water."

class Airplane(Vehicle):
    def move(self):
        return "The airplane flies in the sky."

# Demonstrating polymorphism
def vehicle_action(vehicle):
    print(vehicle.move())

# Create instances of each vehicle
car = Car()
boat = Boat()
airplane = Airplane()

# Call the move method for each vehicle
vehicle_action(car)
vehicle_action(boat)
vehicle_action(airplane)