from car import Car

cars = [
    Car("Toyota", "Corolla", "Silver"),
    Car("Honda",  "Civic",   "Black"),
    Car("Ford",   "Mustang", "Red"),
]

if __name__ == "__main__":
    for car in cars:
        print(car.start())