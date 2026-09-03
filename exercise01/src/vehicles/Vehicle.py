class Vehicle:
    def __init__(self, brand: str, model: str):
        if not brand or not isinstance(brand, str):
            raise ValueError("Brand cannot be empty.")
        if not model or not isinstance(model, str):
            raise ValueError("Model cannot be empty.")

        self.brand = brand.strip()
        self.model = model.strip()

    def __str__(self) -> str:
        return f"Brand: {self.brand} | Model: {self.model}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"brand={self.brand!r}, model={self.model!r})"
        )