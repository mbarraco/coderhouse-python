## Ejercicio extra: AGENDA
def agregar_contacto_a_agenda(un_nombre, un_email, una_agenda):
    una_agenda[un_nombre] = un_email
    return una_agenda

agenda = dict()
print(agenda)
agenda = agregar_contacto_a_agenda("mariano", "mariano@coder.com", agenda)
agenda = agregar_contacto_a_agenda("facundo", "facundo@coder.com", agenda)
agenda = agregar_contacto_a_agenda("mariano", "este mail es incorrecto", agenda)
print(agenda)



# CLASE 07
mi_diccionario = {'mariano': 37, 'juan': 38, 'alberto': 80}

for clave, valor in mi_diccionario.items():
    print("la clave es: " + str(clave))
    print("el valor es: " + str(valor))
    print("*" * 90)



print("." * 90)
print("." * 90)
print("." * 90)

# EJERCICIO SUPER DIFICIL, caso de estudio: imprimir elementos ordenados del diccionario
claves =  list(mi_diccionario.keys())
claves.sort()

for clave in claves:
    print("la clave es: " + str(clave))
    print("el valor es: " + str(mi_diccionario[clave]))
    print("*" * 90)
