# Ejemplo funciones
def sumar_numeros(a, b):
    c =  a + b
    return c

mi_suma = 0
mi_numero = 10
mi_otro_numero = 20
print(mi_suma)
print("." * 90)
mi_suma = sumar_numeros(mi_numero, mi_otro_numero)
print(mi_suma)


# Ejemplo funciones 2
def guardar_contacto_en_agenda(nombre, email, agenda):
    agenda[nombre.upper()] = email.lower()
    return agenda

mi_agenda = dict()
nombre = "arya"
email = "arya@coder.com"
print("primera version: ", mi_agenda)
mi_agenda = guardar_contacto_en_agenda(nombre, email, mi_agenda)
print("segunda version: ", mi_agenda)
mi_agenda = guardar_contacto_en_agenda("samsa", "cualquier cosa", mi_agenda)
print("tercera version: ", mi_agenda)

# Ejemplo crear y escribir archivo
import random
mi_variable_aleatoria = random.random()
print(mi_variable_aleatoria)
mi_archivo = open("test.txt", "w")
mi_archivo.write(str(mi_variable_aleatoria))

# quiero leer el contenido del archivo test.txt
mi_archivo = open("test.txt", "r")
lineas_del_archivo = mi_archivo.read()
print("El contenido del archivo es:", lineas_del_archivo)


# quiero leer el contenido y guardar las lineas en una lista
mi_archivo = open("test.txt", "r")
las_lineas_de_mi_archivo = mi_archivo.readlines()
for linea in las_lineas_de_mi_archivo:
    print(linea)

#
mi_archivo = open("test.txt", "r")

la_linea = mi_archivo.readline()
la_segunda_liena = mi_archivo.readline()

# Esto es para volver a la posicion inicial del archivo
mi_archivo.seek(0)
la_tercer_linea = mi_archivo.readline()

print(la_linea)
print(la_segunda_liena)
print(la_tercer_linea)

# Ejemplo de como no "perder" un diccionario
import json

mi_agenda = {
    "bruce": "bruce@ironmaiden.com", 
    "michael": "michael@helloween.com",
    "george": None
    }

mi_archivo = open("mis_cantantes.txt", "w")
mi_agenda_dumpeada = json.dumps(mi_agenda)
print(type(mi_agenda_dumpeada))
print("*" * 90)
mi_archivo.write(mi_agenda_dumpeada)
mi_archivo.close()


mi_archivo = open("mis_cantantes.txt", "r")
mi_archivo_leido = mi_archivo.read()

print(type(mi_archivo_leido))
print("." * 90)

mi_agenda_recuperada = json.loads(mi_archivo_leido)

print(mi_agenda_recuperada)
print(type(mi_agenda_recuperada))