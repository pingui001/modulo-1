flights = {}

def add_flight():
    code = input("Enter the flight code: ")
    origin = input("Enter the flight origin: ")
    destination = input("Enter the flight destination: ")
    num_seats = int(input("Enter the number of seats: "))
    seats = []
    for i in range(num_seats):
        seat = input(f"Enter seat {i+1}: ")
        seats.append(seat)
    hour = int(input("Enter the flight hour (HH): "))
    minutes = int(input("Enter the flight minutes (MM): "))
    schedule = (hour, minutes)
    flights[code] = {
        "origin": origin,
        "destination": destination,
        "seats": seats,
        "schedule": schedule,
        "occupied_seats": []
    }
    print("Flight added successfully!")

def reserve_seat():
    code = input("Enter the flight code: ")
    if code in flights:
        seat = input("Enter the seat you want to reserve: ")
        if seat in flights[code]["seats"] and seat not in flights[code]["occupied_seats"]:
            flights[code]["occupied_seats"].append(seat)
            print("Seat reserved successfully!")
        else:
            print("Seat not available or invalid")
    else:
        print("Flight not found")

def calculate_occupancy_percentage():
    code = input("Enter the flight code: ")
    if code in flights:
        total_seats = len(flights[code]["seats"])
        occupied_seats = len(flights[code]["occupied_seats"])
        percentage = (occupied_seats / total_seats) * 100
        print(f"Occupancy percentage: {percentage}%")
    else:
        print("Flight not found")

def generate_report():
    for code, flight in flights.items():
        print(f"Flight {code}")
        print(f"Origin: {flight['origin']}")
        print(f"Destination: {flight['destination']}")
        print(f"Schedule: {flight['schedule'][0]:02d}:{flight['schedule'][1]:02d}")
        print(f"Occupied seats: {len(flight['occupied_seats'])}/{len(flight['seats'])}")
        print()

def main():
    while True:
        print("1. Add flight")
        print("2. Reserve seat")
        print("3. Calculate occupancy percentage")
        print("4. Generate report")
        print("5. Exit")
        option = input("Enter your option: ")
        if option == "1":
            add_flight()
        elif option == "2":
            reserve_seat()
        elif option == "3":
            calculate_occupancy_percentage()
        elif option == "4":
            generate_report()
        elif option == "5":
            break
        else:
            print("Invalid option")

main()