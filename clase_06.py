# F strings
mi_variable = "mi arbol es un roble"
otro_string = f"la variable mi_variable dice lo siguiente: {mi_variable}"

print(mi_variable)
print(otro_string)

# Ejercicio: escribir un código que sume dos números 
# y que guarde el resultado en una variable


def mi_func(a, b):
    resultado = a + b
    return resultado


caso_1 = mi_func(0, 0)
caso_2 = mi_func(1, 1)
caso_3 = mi_func(-4, -10)

print("caso 1:", caso_1)
print("caso 2:", caso_2)
print("caso 3:", caso_3)


# Ejemplo, funcion par_o_impar
def par_o_impar(un_numero):
    if un_numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

par_o_impar(0)
par_o_impar(2)
par_o_impar(10)
par_o_impar(16)
par_o_impar(1)
par_o_impar(31)
par_o_impar(95)
par_o_impar(3)
par_o_impar(311111111111)
par_o_impar(99)


##########################################################################
# DICCIONARIOS
##########################################################################


mi_dict = dict()
print(mi_dict)

mi_dict["uno"] = "el primer valor"
print(mi_dict)

mi_dict["doscientos"] = "otro valor"
print(mi_dict)

mi_dict[0] = 1
print(mi_dict)

mi_dict["uno"] = [1,3,4]
print(mi_dict)

del mi_dict["doscientos"]
print(mi_dict)

mi_lista = mi_dict.pop("uno")
print("mi lista es: ", mi_lista)
print(mi_dict)

# borramos todo el contenido diccionario
mi_dict.clear()
print(mi_dict)


mi_dict_quesos = {"queso_1": "roquefort", "queso_2": "brie", "queso_3": "gruyere"}
mi_dict_frutas = {"fruta_1": "uva", "fruta_2": "datiles"}

print(mi_dict_quesos)
print(mi_dict_frutas)

mi_dict_quesos.update(mi_dict_frutas)

print(mi_dict_quesos)
print(mi_dict_frutas)

print("*****************************************************")
print(f"el diccionario de quesos tiene {len(mi_dict_quesos)} elementos")
print(f"el diccionario de frutas tiene {len(mi_dict_frutas)} elementos")

print("*****************************************************")
if "fruta_2" in mi_dict_frutas:
    print("fruta_2 es una de las claves del diccionario de frutas")

if "botella" in mi_dict_frutas:
    print("botella es una de las claves del diccionario de frutas")
else:
    print("botella  NO es una de las claves del diccionario de frutas")

##########################################################################
# CONJUNTOS
##########################################################################
