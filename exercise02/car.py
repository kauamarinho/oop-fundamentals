from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str):
        super().__init__(brand, model)
        self.color = color

    def start(self) -> str:
        return f"{self.brand} {self.model} ({self.color}) is started!"