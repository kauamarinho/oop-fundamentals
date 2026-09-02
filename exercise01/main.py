from veiculos import Carro, Moto

# Instâncias
carros = [
    Carro("Toyota",     "Corolla",  4),
    Carro("Volkswagen", "Gol",      2),
    Carro("Ford",       "Mustang",  2),
]

motos = [
    Moto("Honda",    "CB 500F",       "Esportiva"),
    Moto("Yamaha",   "NMAX",          "Casual"),
    Moto("Kawasaki", "Ninja ZX-10R",  "Esportiva"),
]

# __str__: exibição amigável
print("=" * 55)
print("  __str__  —  exibição amigável")
print("=" * 55)

print("\n--- Carros ---")
for carro in carros:
    print(carro)

print("\n--- Motos ---")
for moto in motos:
    print(moto)

# __repr__: útil para debug
print("\n" + "=" * 55)
print("  __repr__  —  representação para debug")
print("=" * 55)

print()
for veiculo in carros + motos:
    print(repr(veiculo))

# Validações — entradas inválidas
print("\n" + "=" * 55)
print("  Validações — entradas inválidas")
print("=" * 55)

casos = [
    ("Carro com marca vazia",         lambda: Carro("",       "Gol",    4)),
    ("Carro com portas inválidas (3)", lambda: Carro("VW",    "Gol",    3)),
    ("Carro com portas negativas",     lambda: Carro("VW",    "Gol",   -1)),
    ("Moto com tipo inválido",         lambda: Moto("Honda",  "CB",  "Trial")),
]

for descricao, caso in casos:
    try:
        caso()
    except (ValueError, TypeError) as e:
        print(f"\n  [{descricao}]")
        print(f"  ValueError: {e}")