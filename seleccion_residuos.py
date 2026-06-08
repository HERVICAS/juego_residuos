import random


def obtener_residuos(residuos, cantidad=4):
    """
    Devuelve una lista aleatoria de residuos.
    """

    cantidad = min(cantidad, len(residuos))

    return random.sample(residuos, cantidad)