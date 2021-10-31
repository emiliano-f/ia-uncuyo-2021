# La entropia deberia recibir un objeto de clase base

# Unicamente funciones
from base import Base

def entropy(_data: Base):

    elements: int = _data.length_positive + _data.length_negative
