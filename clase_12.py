class Animal:

    ruido = None

    def __init__(yo_mismo, nombre):
        yo_mismo._nombre = nombre

    def hablar(yo_mismo):
        print(f"{yo_mismo.ruido}, mi nombre es {yo_mismo._nombre}")


class Gata(Animal):

    ruido = "miau"


class Burro(Animal):

    ruido = "frfnwlreflksnflsrf"


mi_otra_gata = Gata("Olivetta")
mi_burro = Burro("Burro")


mi_otra_gata.hablar()
mi_burro.hablar()

print(type(mi_otra_gata))
print(type(mi_burro))


print(mi_burro._nombre)