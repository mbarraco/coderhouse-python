# EJEMPLO 1
class Gata:
    
    patas = 4

    def __init__(self, nombre, madre):
        self.nombre = nombre
        self.madre = madre
        

    def mostrarse(self):
        print(self.nombre)
        print(self.patas)
        print(self.madre)
        print(type(self))


aceituna = Gata("Aceituna", "Manuela")
orca = Gata("Orca", "Una gata que no conocemos")


orca.mostrarse()
aceituna.mostrarse()


# Ejemplos
class Persona:

    reloj = "casio"
    sombra = True

    def __init__(self, nombre, segundo_nombre, pais):
        self.nombre = nombre
        self.segundo_nombre = segundo_nombre
        self.pais = pais


    def presentarse(self):
        print(f"Buenas noches, mi nombre es {self.nombre} {self.segundo_nombre} y estoy en {self.pais}")

    def cambiar_de_pais(self, pais):
        self.pais = pais


    def __str__(self):
        return f"Esta persona se llama {self.nombre}"

    def __len__(self):
        return 509

    def __getitem__(self, pos):
        return 1


persona_1 = Persona("Roberto", "Arnaldo", "Birmania")
persona_2 = Persona("Elena", "Silvia", "Latvia")
print(len(persona_1))
print(persona_1[0])
persona_1.presentarse()
persona_2.presentarse()
persona_2.cambiar_de_pais("Argentina")
persona_2.presentarse()


#
# Diapositiva 47
#
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}"

    
class Gata:

    def __init__(self, nombre, humano):
        self.nombre = nombre
        self.humano = humano

    
    def presentarse(self):
        print(f"Miau! soy {self.nombre} y vivo con mi humane que se va a presentar ahora:\n {self.humano.presentarse()} ")


mi_hermana = Persona("Soledad")
orca = Gata("Orca", mi_hermana)

orca.presentarse()


# Ejercicio para pensar diapo 62

class Atleta:

    def __init__(self, nombre, apellido, altura, peso):
        pass

    def obtener_indice_masa_corporal(self):
        pass



atleta_1 = Atleta("mariano", "lopez", 1.7, 74)

print(atleta_1.obtener_indice_masa_corporal())