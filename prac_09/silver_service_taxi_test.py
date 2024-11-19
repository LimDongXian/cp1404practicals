from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi instance with fanciness of 2
silver_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Print the initial state
print(silver_taxi)

# Drive 18 km
distance_driven = silver_taxi.drive(18)
print(f"Distance driven: {distance_driven} km")

# Calculate and print the fare
fare = silver_taxi.get_fare()
print(f"Fare for 18 km trip: ${fare:.2f}")
