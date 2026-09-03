from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self) -> str:
        pass