# Ejercicio: escribir un codigo que diga si un numero es multiplo de 5

def la_funcion_de_roque(este_coso_que_pongo_aca):
    print(f"la funcion recibió un: {este_coso_que_pongo_aca}")
    if este_coso_que_pongo_aca % 5 == 0:
        return "es multiplo"
    else: 
        return "no es multiplo"
    

print("*" * 90)
alguien_que_espera_algo = la_funcion_de_roque(2.5)

print(alguien_que_espera_algo)

"""
1. Elegir nombre de la funcion y escribir el esqueleto
2. Escribir 1 caso de prueba
3. Hacer pasar el caso de prueba
4. Repetir 2 y 3 hasta el cansancio

"""

# Escribir una funcion que me diga si una palabra tiene más de 10 letras
def calcular_si_palabra_tiene_mas_de_10_letras(una_palabra):
    longitud = len(una_palabra)
    if longitud > 10:
        return True
    else:
        return False


# TESTS
tiene_mas_de_10_letras = calcular_si_palabra_tiene_mas_de_10_letras("12345678")
if tiene_mas_de_10_letras == False:
    print("funciona bien")
else:
    print("funciona mal")


tiene_mas_de_10_letras = calcular_si_palabra_tiene_mas_de_10_letras("asd;aioushFPIusdhgfiusahdfpiudhfpiusdhpfiuagsdf")
if tiene_mas_de_10_letras == True:
    print("funciona bien")
else:
    print("funciona mal")

tiene_mas_de_10_letras = calcular_si_palabra_tiene_mas_de_10_letras("aaaaaaaaaaa")
if tiene_mas_de_10_letras == True:
    print("funciona bien")
else:
    print("funciona mal")


tiene_mas_de_10_letras = calcular_si_palabra_tiene_mas_de_10_letras("aa")
if tiene_mas_de_10_letras == False:
    print("funciona bien")
else:
    print("funciona mal")

tiene_mas_de_10_letras = calcular_si_palabra_tiene_mas_de_10_letras("")
if tiene_mas_de_10_letras == False:
    print("funciona bien")
else:
    print("funciona mal")

# Escribir una funcion que calcule la suma de dos numeros
def sumar_numeros(un_numero, otro_numero):
    return un_numero + otro_numero

suma = sumar_numeros(0, 0)
if suma == 0:
    print("correcto")
else:
    print("error")


suma = sumar_numeros(8, 9)
if suma == 17:
    print("correcto")
else:
    print("error")




# Entregable

def calcular_si_es_bisiesto(year):  # year es año en inglés
    if year % 4 == 0:
        return True
    else:
        return False


# 400 es bisiesto (porque 400 es multiplo de 400)
es_bisiesto = calcular_si_es_bisiesto(400)
if es_bisiesto == True:
    print("correcto")
else:
    print("incorrecto")

# 100 no es bisiesto
es_bisiesto = calcular_si_es_bisiesto(100)
if es_bisiesto == False:
    print("correcto")
else:
    print("incorrecto")

# 2012 es bisiesto,
es_bisiesto = calcular_si_es_bisiesto(2012)
if es_bisiesto == True:
    print("correcto")
else:
    print("incorrecto")


# 2010 no es bisiesto, 
es_bisiesto = calcular_si_es_bisiesto(2010)
if es_bisiesto == False:
    print("correcto")
else:
    print("incorrecto")

# 2000 es bisiesto,
es_bisiesto = calcular_si_es_bisiesto(2000)
if es_bisiesto == True:
    print("correcto")
else:
    print("incorrecto")

# 1900 no es bisiesto.
es_bisiesto = calcular_si_es_bisiesto(1900)
if es_bisiesto == False:
    print("correcto")
else:
    print("incorrecto")