# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
if name.strip() == "":
  print("Invalid name. Please try again.")
  name = input("Enter passenger name: ")

distance_input = input("Enter distance (km): ")
if not distance_input.replace(".", "", 1).isdigit() or float(distance_input) <= 0:
  print("Invalid distance. Enter a number > 0.")
  distance_input = input("Enter distance (km): ")
distance = float(distance_input)

passengers_input = input("Enter number of passengers: ")
if not passengers_input.isdigit() or int(passengers_input) <= 0:
  print("Invalid input. Enter a positive whole number.")
  passengers_input = input("Enter number of passengers: ")
passengers = int(passengers_input)

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
