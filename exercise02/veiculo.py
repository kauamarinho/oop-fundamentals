from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self) -> str:
        pass