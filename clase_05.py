###############################################################################
# CASOS DE PRUEBA
###############################################################################

mi_numero = 0
valor_esperado = "valor no reconocido"

# mi_numero = 1
# valor_esperado = "valor no reconocido"

# mi_numero = 35
# valor_esperado = "valor no reconocido"

# mi_numero = 2
# valor_esperado = "valor no reconocido"

# mi_numero = 20
# valor_esperado = "A"

# mi_numero = 9
# valor_esperado = "B"

# mi_numero = 6
# valor_esperado = "valor no reconocido"

#
#  mi programa
#

if (mi_numero % 2 == 0) and (mi_numero > 18):
    print("................................................ 1 ........")
    resultado = "A"
elif (mi_numero % 2 != 0) and (mi_numero % 3 == 0):
    print("................................................ 2 ........")
    resultado = "B"
else:
    print("................................................ 3 ........")
    resultado = "valor no reconocido"

#
# test
#
print("mi_numero es: " + str(mi_numero))
print("valor esperado es: " + valor_esperado)
print("resultado: " + resultado)
assert resultado == valor_esperado
print("finalizado correctamente")



###############################################################################
# While
###############################################################################
mi_numero = 0

while mi_numero < 3:
    print(" ******* ", mi_numero)
    mi_numero += 1
else:
    print("termine de ejecutar el while!")

###############################################################################
# While con input
###############################################################################

intento = 1
while intento <= 3:
    input("escribi cualquier cosa: ")
    print(intento)
    intento +=1
else:
    print("se terminaron los intentos")

###############################################################################
# For 
###############################################################################
mi_lista = [1, "a", 3, True, "mariano"]

for elemento in mi_lista:
    print(elemento)

print("termine correctamente")

###############################################################################
# For con break
###############################################################################
mi_lista = [1, "a", 3, True, "mariano"]

for elemento in mi_lista:
    print(elemento)

    if elemento == 3:
        break

print("termine correctamente")

###############################################################################
# For con enumerate
###############################################################################

mi_lista = [1, "a", 3, True, "mariano"]

for indice, elemento in enumerate(mi_lista):
    print(indice, elemento)

###############################################################################
# For con Continue
###############################################################################
# Recorrer la lista y 
# si el valor del elemento es 3 imprimir un mensaje, si no, hacer nada
mi_lista = [1, "a", 3, True, "mariano"]

for el in mi_lista:
    print(el)
    if el == 3:
        print("un mensaje")
    else:
        continue

    print("fin de bloque")