from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Prius 1", 100, 50)

# Try driving the car a few times and check the outcome
print(f"Attempted to drive 30 km, actually drove {my_car.drive(30)} km.")

print(f"Attempted to drive 50 km, actually drove {my_car.drive(50)} km.")

print(f"Attempted to drive 70 km, actually drove {my_car.drive(70)} km.")

# Final state of the car to compare the actual value is correct
print(f"Final car state: {my_car}")


