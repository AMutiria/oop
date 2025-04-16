class RacingVehicle:
    def __init__(self, top_speed):
        self.top_speed = top_speed

    def pit_stop(self):
        print("Vehicle is in the pit stop for maintenance.")

class FormulaOneCar(RacingVehicle):
    def __init__(self, team_name, driver, color, top_speed):
        super().__init__(top_speed)
        self.team_name = team_name
        self.driver = driver
        self.color = color
        self.current_speed = 0

    def accelerate(self):
        self.current_speed += 30  # Simulate acceleration
        print(f"The {self.color} {self.team_name} car driven by {self.driver} accelerates! Current speed: {self.current_speed} km/h.")

    def overtake(self, other_car):
        print(f"The {self.color} {self.team_name} car driven by {self.driver} is attempting to overtake the {other_car.color} {other_car.team_name} car driven by {other_car.driver}!")
        # Simulate overtake logic (simplified)
        if self.current_speed > other_car.current_speed + 10:
            print(f"Overtake successful! The {self.color} {self.team_name} car is now ahead.")
        else:
            print("Overtake attempt failed.")

# Activity 2: Polymorphism Challenge with Formula One Cars

# Create instances of FormulaOneCar
car1 = FormulaOneCar("Scuderia Ferrari", "Lewis Hamilton", "red", 350)
car2 = FormulaOneCar("Mercedes-AMG Petronas", "Kimi Antonelli", "silver", 345)
car3 = FormulaOneCar("Oracle Red Bull Racing", "Max Verstappen", "blue", 355)

print("\n--- Activity 2: Polymorphism in Action ---\n")

# Demonstrate the 'accelerate' action for each car
car1.accelerate()
car2.accelerate()
car3.accelerate()

print("\n--- Overtaking Maneuvers ---\n")

# Demonstrate the 'overtake' action
car1.overtake(car2)
car3.accelerate() # Give car3 some speed
car3.overtake(car1)
car2.overtake(car3)

print("\n--- Pit Stop Example (Inherited Method) ---\n")
car1.pit_stop()