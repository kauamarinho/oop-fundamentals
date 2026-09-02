from .veiculo import Veiculo


class Carro(Veiculo):
    PORTAS_VALIDAS = (2, 4)

    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)

        if not isinstance(portas, int) or portas not in self.PORTAS_VALIDAS:
            raise ValueError(
                f"Quantidade de portas inválida: {portas!r}. "
                f"Valores aceitos: {self.PORTAS_VALIDAS}."
            )

        self.portas = portas

    def __str__(self) -> str:
        return f"{super().__str__()} | Portas: {self.portas}"

    def __repr__(self) -> str:
        return (
            f"Carro(marca={self.marca!r}, modelo={self.modelo!r}, "
            f"portas={self.portas})"
        )