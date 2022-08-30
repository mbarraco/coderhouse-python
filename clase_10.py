# Ejemplo de SCOPE
xx = 200

def mi_otra_funcion(a):
    return a + 1

def my_function():
    mi_variable = 100
    mi_variable = mi_otra_funcion(mi_variable)
    print(mi_variable)
    print(xx)

my_function()

# Ejemplo de SCOPE II
mi_variable = 10

def my_function():
    mi_variable = 100
    print(f"dentro de la funcion vale: {mi_variable}")


my_function()
print(f"fuera de la funcion vale: {mi_variable}")


# Ejemplo modificacion tipos mutables
mi_lista = []
def mi_func(l):
    l.append(1)
print(mi_lista)
mi_func(mi_lista)
print(mi_lista)
mi_func(mi_lista)
print(mi_lista)

# Ejemplo 2
mi_variable = 0
def mi_func(a):
    a = 10
print(mi_variable)
mi_func(mi_variable)
print(mi_variable)

# Return multiple
def mi_funcion_que_devuelve_dos_cosas():
    return "primer elemento", "segundo elemento"
mi_variable = mi_funcion_que_devuelve_dos_cosas()
print(mi_variable)
print(type(mi_variable))
a = mi_variable[0]
b = mi_variable[1]
print(f"al principio fue creado el {a} y luego fue creado el {b}")

# 
def mi_funcion_que_devuelve_tres_cosas():
    return "primer elemento", "segundo elemento", "otro elemento"
uno, dos, tres = mi_funcion_que_devuelve_tres_cosas()
print(f"al principio fue creado el {tres}, luego fue creado el {uno} y más tarde {dos}")


# El orden importa
def mi_funcion(primero, segundo):
    print(f"el primero: {primero}")
    print("el segundo: {}".format(segundo))
mi_funcion(9, 78)
print("." * 90)
mi_funcion(78, 9)

# Parametros con nombre y valor "default" (por defecto)
def mi_funcion(aa="un valor", bebe="otro valor"):
    print(f"{aa} -> {bebe}")
mi_funcion(9, 78)
mi_funcion(78, 9)
print("*" * 90)
mi_funcion(aa=5, bebe=90)
mi_funcion(bebe=90, aa=5)
print("*" * 90)
mi_funcion()

# Ejemplo año bisiesto
def es_bisiesto(un_numero):
    return un_numero % 4 == 0


def resolver_ejercicio(un_numero):
    if type(un_numero) is not int:
        return "por favor ingresar un entero, si no, no funciono"
    else:
        return es_bisiesto(un_numero)


es_bisiesto = resolver_ejercicio("1993")
print(es_bisiesto)