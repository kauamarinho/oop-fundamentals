from typing import Literal

from .veiculo import Veiculo

TipoMoto = Literal["Esportiva", "Casual"]
TIPOS_VALIDOS = ("Esportiva", "Casual")


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo: TipoMoto):
        super().__init__(marca, modelo)

        if tipo not in TIPOS_VALIDOS:
            raise ValueError(
                f"Tipo de moto inválido: {tipo!r}. "
                f"Valores aceitos: {TIPOS_VALIDOS}."
            )

        self.tipo = tipo

    def __str__(self) -> str:
        return f"{super().__str__()} | Tipo: {self.tipo}"

    def __repr__(self) -> str:
        return (
            f"Moto(marca={self.marca!r}, modelo={self.modelo!r}, "
            f"tipo={self.tipo!r})"
        )