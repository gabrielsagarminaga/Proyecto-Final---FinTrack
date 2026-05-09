from dataclasses import dataclass

@dataclass
class Movimiento:
    tipo: str
    monto: float
    categoria: str
    descripcion: str
    fecha: str