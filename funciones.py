def imprimir_suma(a, b):
    print(a + b)


def imprimier_resta(a, b):
    print(a - b)


def imprimir_producto(a, b):
    print(a * b)


class Avion:

    def __init__(self, nro_de_vuelo):
        self.nro_de_vuelo = nro_de_vuelo

    
    def anunciarse(self):
        print(f"Soy un avion y mi número de vuelo hoy es {self.nro_de_vuelo}")
