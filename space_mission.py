class SpaceShip:
    def __init__(self,name:str,fuel:int):
        self.name= name
        self.fuel = fuel
    def launch(self):
        if self.fuel < 50:
            return f"Not enough fuel"
        self.fuel = self.fuel - 50
        return f"Launching {self.name}"
    def refuel(self,fuel_more:int):
        if fuel_more < 0:
            print (f"Fuel value cannot be less than zero")
        else :
            return f"{fuel_more} units of fuel  has been added . Your fuel level is now { self.fuel + fuel_more}"

class CargoShip(SpaceShip):
    def __init__(self,name,cargo_weight:int,fuel):
        super().__init__(name,fuel)
        self.cargo_weight = cargo_weight
    def launch(self):
        return f"It took {self.name} {self.cargo_weight - (50 + (self.fuel * 2))} units of fuel to launch"
class PassengerShip(SpaceShip):
    def __init__(self,name,passenger_count:int,fuel):
        super().__init__(name,fuel)
        self.passenger_count = passenger_count   
    def launch(self):
     return  "Too many passengers cannot launch"  if self.passenger_count > 100 else f"{self.name } launched and has {self.fuel - 50} units of fuel left"
            
# SAMPLE EXECUTION
# Create objects
cargo_ship = CargoShip("Galactic Hauler", 200, 30)
passenger_ship = PassengerShip("Star Voyager", 100, 80)

# Attempt to launch both ships
print()
print(cargo_ship.launch())
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 200 - (50 + 30*2) = 90
print()
print(passenger_ship.launch())
# Output: Launching Star Voyager!
# Fuel after launch: 100 - 50 = 50

# Refuel both ships
print(cargo_ship.refuel(50))# Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.
print()
print(passenger_ship.refuel(30))
# Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# Launch again after refueling
print()
print(cargo_ship.launch())
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 140 - (50 + 30*2) = 30
print()
print(passenger_ship.launch())
# Output: Launching Star Voyager!
# Fuel after launch: 80 - 50 = 30

# Try to refuel with invalid amount
print()
print(cargo_ship.refuel(-10))
# Output: Cannot refuel with negative amount.

# Test PassengerShip with too many passengers
passenger_ship.passenger_count = 120
print()
print(passenger_ship.launch())
# Output: Too many passengers. Cannot launch.

# Try to launch cargo ship with low fuel
cargo_ship = SpaceShip("Galactic Hauler", 30)
print()
print(cargo_ship.launch())
# Output: Not enough fuel to launch.





# Vehicle should at least store:
#   - name

# class Vehicle:
#     def __init__(self, name):
#         self.name = name

#     def describe(self):
#         return f"Vehicle: {self.name}"

# class Car(Vehicle):
#     def __init__(self, name, number_of_doors):
#         super().__init__(name)
#         self.number_of_doors = number_of_doors

#     def describe(self):
#         return f"Car: {self.name} with {self.number_of_doors} doors"


# #
# # Car should extend Vehicle and also store:
# #   - number_of_doors
# #
# # They should both have a method that returns a string description.
# #
# # Below is only usage. Students must write the classes above it.
# # ============================================

# # Create a Vehicle
# vehicle = Vehicle(name="Bicycle")
# print(vehicle.describe())
# # Expected output format (example):
# # "Vehicle: Bicycle"

# # Create a Car
# car = Car(name="Toyota", number_of_doors=4)
# print(car.describe())
# # Expected output format (example):
# # "Car: Toyota with 4 doors"