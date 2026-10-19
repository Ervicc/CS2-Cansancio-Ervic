# Travel Fare Calculator
FARE_RATE = 14

while True:
    name = input("Enter passenger name: ")

    if name.strip() != "":
        break  # valid name, stop asking
    else:
        print("Invalid name. Name cannot be empty.")

while True:
    distance_input = input("Enter distance (km): ")

    # replace removes one "." so decimals like 3.5 still count as digits
    if distance_input.replace(".", "", 1).isdigit() and float(distance_input) > 0:
        distance = float(distance_input)
        break
    else:
        print("Invalid distance. Enter a number greater than 0.")

while True:
    passengers_input = input("Enter number of passengers: ")

    if passengers_input.isdigit() and int(passengers_input) > 0:
        passengers = int(passengers_input)
        break
    else:
        print("Invalid input. Enter a whole number greater than 0.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
