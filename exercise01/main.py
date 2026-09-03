from vehicles  import Car, Motorcycle

# Instances
cars = [
    Car("Toyota",     "Corolla",  4),
    Car("Volkswagen", "Gol",      2),
    Car("Ford",       "Mustang",  2),
]

motorcycles = [
    Motorcycle("Honda",    "CB 500F",      "Sport"),
    Motorcycle("Yamaha",   "NMAX",         "Casual"),
    Motorcycle("Kawasaki", "Ninja ZX-10R", "Sport"),
]

# __str__: user-friendly display
print("=" * 55)
print("  __str__  —  user-friendly display")
print("=" * 55)

print("\n--- Cars ---")
for car in cars:
    print(car)

print("\n--- Motorcycles ---")
for motorcycle in motorcycles:
    print(motorcycle)

# __repr__: useful for debugging
print("\n" + "=" * 55)
print("  __repr__  —  debug representation")
print("=" * 55)

print()
for vehicle in cars + motorcycles:
    print(repr(vehicle))

# Validations — invalid inputs
print("\n" + "=" * 55)
print("  Validations — invalid inputs")
print("=" * 55)

cases = [
    ("Car with empty brand",           lambda: Car("",      "Gol",  4)),
    ("Car with invalid doors (3)",     lambda: Car("VW",   "Gol",  3)),
    ("Car with negative doors",        lambda: Car("VW",   "Gol", -1)),
    ("Motorcycle with invalid type",   lambda: Motorcycle("Honda", "CB", "Trial")),
]

for description, case in cases:
    try:
        case()
    except (ValueError, TypeError) as e:
        print(f"\n  [{description}]")
        print(f"  ValueError: {e}")