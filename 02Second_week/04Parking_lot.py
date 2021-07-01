def parking_lot(count):
    parking = set()
    for i in range(count):
        data = input().split(", ")
        command, car = data
        if command == "IN":
            parking.add(car)
        else:
            parking.remove(car)
    if parking:
        for car in parking:
            print(car)
    else:
        print("Parking Lot is Empty")


count_of_cars = int(input())
parking_lot(count_of_cars)
