class Veiculo:
    def __init__(self, marca: str, modelo: str):
        if not marca or not isinstance(marca, str):
            raise ValueError("Marca não pode ser vazia.")
        if not modelo or not isinstance(modelo, str):
            raise ValueError("Modelo não pode ser vazio.")

        self.marca = marca.strip()
        self.modelo = modelo.strip()

    def __str__(self) -> str:
        return f"Marca: {self.marca} | Modelo: {self.modelo}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"marca={self.marca!r}, modelo={self.modelo!r})"
        )