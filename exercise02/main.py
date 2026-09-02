from carro import Carro

carros = [
    Carro("Toyota", "Corolla", "Prata"),
    Carro("Honda",  "Civic",   "Preto"),
    Carro("Ford",   "Mustang", "Vermelho"),
]

if __name__ == "__main__":
    for carro in carros:
        print(carro.ligar())