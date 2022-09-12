########################################################
# 23 - Alternativa 1
########################################################

class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describirse(self):
        print(f"Soy un {self.especie} del tipo {type(self)}")


class Perro(Animal):
    def __init__(self, especie, nombre, dueno):
        self.dueno = dueno
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        print("barf barf")


class Escarabajo(Animal):
    def hablar(self):
        print("crcrcrcrcrc!")

    def picar(self):
        print("estoy picando!")


mi_perro = Perro("mamifero", "tito", "Robert")
mi_escarabajo = Escarabajo("insecto", "El dorado")


mi_perro.hablar()
mi_escarabajo.hablar()
mi_escarabajo.picar()
########################################################
# 23 - Alternativa 2
########################################################

class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describirse(self):
        print(f"Soy un {self.especie} del tipo {type(self)}")


class Perro(Animal):
    def __init__(self, especie, nombre, dueno):
        super().__init__(especie, nombre)
        self.dueno = dueno

    def hablar(self):
        print(f"barf barf, mi humano es {self.due}")


class Escarabajo(Animal):
    def hablar(self):
        print("crcrcrcrcrc!")

    def picar(self):
        print("estoy picando!")


mi_perro = Perro("mamifero", "tito", "Robert")
mi_escarabajo = Escarabajo("insecto", "El dorado")


mi_perro.hablar()
mi_escarabajo.hablar()
mi_escarabajo.picar()


########################################################
# 23 - Herencia multiple
########################################################


class Uno:
    def hablar(self):
        print("Uno")

class Dos(Uno):
    def hablar(self):
        print("dos")

class Tres(Dos):
   pass


# Esto es herencia multiple propiamente dicho
class Alfa:
    def hablar(self):
        print("Alfa")

class Beta:
    def hablar(self):
        print("Beta")

class Delta:
    def hablar(self):
        print("Delta")

class Gama(Alfa, Beta, Delta):
    pass


mi_tres = Tres()
mi_tres.hablar()


mi_gama = Gama()
mi_gama.hablar()


########################################################
# 47 - Duck Typing (?)
########################################################
def leer_patente(xx):
    xx.mostrar_patente()


class Auto:
    def __init__(self, patente):
        self.patente = patente

    def mostrar_patente(self):
        print(f"mi patente es {self.patente}")


class Bicicleta:
    def mostrar_patente(self):
        print("no tengo patente!")


class Avion:
    def __init__(self, matricula):
        self.matricula = matricula

    def mostrar_matricula(self):
        print(self.matricula)


mi_auto = Auto("bja640")
leer_patente(mi_auto)
mi_bici = Bicicleta()
leer_patente(mi_bici)
mi_avion = Avion("LV454")
leer_patente(mi_avion)