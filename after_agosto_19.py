# ******************* KAHOOT, Respuesta en codigo de cada pregunta. *******************


# ******************* diapo 2
# variable1 = 1
# variable2 = ["nombre"]
# variable3 = 1.5
# variable4 = {}
# variable5 = {variable2[0]:"juan"}

# print(type(variable1))
# print(type(variable2))
# print(type(variable3))
# print(type(variable4))
# print(type(variable5))


# ******************* diapo 3
# variable1 = 1 > 2
# variable2 = "edad" in ["nombre", "apellido", "sobrenombre"]
# variable3 = 1.5 + 2.5 == 5
# variable4 = 0 == True

# print(variable1)
# print(variable2)
# print(variable3)
# print(variable4)


# ******************* diapo 4
# datos = [1, -5, 123,34, "Una cadena", "Otra cadena"]
# print(datos.pop(1))


# ******************* diapo 5
# password = 123456
# user = "Juan"

# if  user == "Juan" or password == 123456 and user == "juan":
#     print("Bienvenido Juan")
# else: 
#     print("Algun dato es incorrecto")


# ******************* diapo 6
# num = 5
# while num < 0:
#     print(f"{num}")
#     num -= 1


# ******************* diapo 7
# for l in "hola":
#     print(l)


# ******************* diapo 8
# mi_dict = {"nombre": "Joaquin", "apellido": "Zuazo"}
# mi_dict.append("edad": 35)
# print(mi_dict["edad"])



# ******************* diapo 9
# mi_nuevo_dict = {"nombre": "Joaquin", "apellido": "Zuazo"}
# mi_nuevo_dict["edad"] = 35
# mi_nuevo_dict["nombre"] = "Juan"
# del mi_nuevo_dict["Zuazo"]
# print(mi_nuevo_dict)




# ******************* Repaso de dict y funciones *******************


# Idea
# Vamos a construir una agenda sobre un dict de python. Vamos a construir funciones que nos permitan, como usuarios realizar las siguientes operaciones:


mi_agenda = {}


# Consultar el email de un contacto conociendo sólo su nombre
# suponemos que la clave va a ser el nombre
def consulta_agenda(nombre, agenda = {}):
    return agenda.get(nombre, False)

print(consulta_agenda(agenda = mi_agenda, nombre = "Joaquin"))


# Agregar un contacto a la agenda
# vamos a necesitar pasarle a la funcion, la clave (que va a ser el nombre), y el dato, (que va a ser el email),
def agregar_contacto_agenda(agenda, nombre, email):
    agenda[nombre] = email
    return agenda

mi_agenda = agregar_contacto_agenda(mi_agenda, "Joaquin", "jzuazociolfi@gmail.com")

print(mi_agenda)


# Borrar un contacto de la agenda
# la funcion va a recibir solo la clave (nombre del contacto)
def borrar_contacto(agenda, nombre):
    dato_borrado = agenda.pop(nombre)
    print(f"Borre correctamente el dato: {dato_borrado} que correspondia a la clave {nombre}")
    return agenda

mi_agenda = borrar_contacto(mi_agenda, "Joaquin")

mi_agenda = agregar_contacto_agenda(mi_agenda, "Marco", "MarcoJS@gmail.com")
mi_agenda = agregar_contacto_agenda(mi_agenda, "Mariana", "MarianaGanoTodo@gmail.com")


# Modificar el email de un contacto en la agenda
# la funcion va a recibir la clave (nombre) y nuevo dato (email)
def modifica_contacto(agenda, nombre, nuevo_email):
    agenda[nombre] = nuevo_email
    return agenda

mi_agenda = modifica_contacto(mi_agenda, "Marco", "beleza@gmail.com")
print(consulta_agenda("Marco", mi_agenda))


# Modificar el nombre de un contacto en la agenda.
def modificar_clave_agenda(agenda, nombre, nuevo_nombre):
    dato = agenda.pop(nombre)
    agenda[nuevo_nombre] = dato
    return agenda

mi_agenda = modificar_clave_agenda(mi_agenda, "Marco", "Marcos")

print(mi_agenda)




# ******************* Ejercicio propuesto por Nazareno post after *******************


# Realizar una funcion que reciba un diccionario donde cada clave contiene una lista.
# ademas recibe la clave del dict que se quiere ordenar y si es desc o asc.
# debe retornar el dict con esa clave ordenada.


dicc = {"clave1":['c','a','b'], "clave2":['casa','auto','barco'], "clave3":[2,1,3]}


def diccionario_ord(dic, clave, des):
    print(f"entre asi {dic}")
    valor = dic.get(clave)
    valor.sort(reverse=des)
    dic[clave] = valor
    return dic

print(diccionario_ord(dicc, "clave1", False))