# Entregable de funciones
# 5) Realizá una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:
# Si el límite inferior es mayor o igual al limite superior, devolver un ValueError con el mensaje "limites incorrectos"

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.


def recortar(numero_a_recortar, limite_inferior, limite_superior):
    if numero_a_recortar < limite_inferior:
        return limite_inferior
    elif numero_a_recortar > limite_superior:
        return limite_superior
    return numero_a_recortar


def recortar_con_excepcion(numero_a_recortar, limite_inferior, limite_superior):
    if limite_inferior > limite_superior:
        raise ValueError(
            "limites incorrectos"
        )  # esto es para arreglar el problema del enunciado

    elif numero_a_recortar < limite_inferior:
        return limite_inferior
    elif numero_a_recortar > limite_superior:
        return limite_superior
    return numero_a_recortar


# Devolver el límite inferior si el número es menor que éste
print(recortar(0, 1, 2) == 1)
print(recortar(-6, -5, 100) == -5)
print(recortar(11, 12, 14) == 12)
# Devolver el límite superior si el número es mayor que éste.
print(recortar(0, -2, -1) == -1)
print(recortar(5, 1, 4) == 4)
print(recortar(10, 8, 9) == 9)
# Devolver el número sin cambios si no se supera ningún límite.
print(recortar(0, -1, 1) == 0)
print(recortar(5, 1, 40) == 5)
print(recortar(10, -100, 100) == 10)
# extra
try:
    recortar_con_excepcion(0, 1, -90) == 1
except ValueError as e:
    print(e)

# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio
# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi.
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.


print("*" * 90)
print("Ejercicio 2")


def area_circulo(radio):
    return radio**2 * 3.14159


print(area_circulo(1) == 3.14159)
print(area_circulo(0) == 0)
print(area_circulo(10) == 314.159)


print("*" * 90)
print("Ejercicio 3")

#  Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'


def relacion(un_numero, otro_numero):
    if un_numero > otro_numero:
        return 1
    elif un_numero < otro_numero:
        return -1
    else:
        return 0


# Si el primer número es mayor que el segundo, debe devolver 1.
print(relacion(12, 6) == 1)
print(relacion(-10, -15) == 1)
print(relacion(0, -15) == 1)
# Si el primer número es menor que el segundo, debe devolver -1.
print(relacion(7, 10) == -1)
print(relacion(0, 1) == -1)
print(relacion(-10, -5) == -1)
# Si ambos números son iguales, debe devolver un 0.
print(relacion(1, 1) == 0)
print(relacion(0, 0) == 0)
print(relacion(-10, -10) == 0)
