from .Vehicle import Vehicle

class Car(Vehicle):
    VALID_DOORS = (2, 4)

    def __init__(self, brand: str, model: str, doors: int):
        super().__init__(brand, model)

        if not isinstance(doors, int) or doors not in self.VALID_DOORS:
            raise ValueError(
                f"Invalid number of doors: {doors!r}. "
                f"Accepted values: {self.VALID_DOORS}."
            )

        self.doors = doors

    def __str__(self) -> str:
        return f"{super().__str__()} | Doors: {self.doors}"

    def __repr__(self) -> str:
        return (
            f"Car(brand={self.brand!r}, model={self.model!r}, "
            f"doors={self.doors})"
        )