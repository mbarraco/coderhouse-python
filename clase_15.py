####################
# 58
####################
import collections

Fish = collections.namedtuple("Fish", ["name", "species", "tank"])
mi_pececito = Fish("Nemo", "pez payaso", None)
print(mi_pececito.name)
mi_dict = mi_pececito._asdict()
print(mi_dict)

####################
# 60
####################
from collections import Counter

mi_palabra = "abracabra"
mi_contador = Counter(mi_palabra)
print(list(mi_contador.elements()))
print(list(mi_contador.most_common(1)))


####################
# 63
####################
from datetime import datetime

today_and_now =  datetime.now()
print(today_and_now)
print(today_and_now.year)
print(today_and_now.microsecond)

####################
# 65
####################
mi_fecha = datetime(2022, 1, 9, 9, 15, 8)
print(mi_fecha.strftime("%Y %B %d"))


####################
# 66
####################

from datetime import datetime, timedelta

ahora = datetime.now()

dentro_de_una_semana = ahora + timedelta(days=7)
hace_una_semana = ahora - timedelta(days=7)

print(ahora.strftime("%B - %d - %Y "))
print(dentro_de_una_semana.strftime("%B / %d / %Y "))
print(hace_una_semana.strftime("%B / %d / %Y "))


#################
# 71
####################

import math

print(math.ceil(1.4))
print(math.floor(1.4))
print(round(1.499999))
print(round(1.5))


#################
# 74
####################


from random import randrange, choice

print(randrange(12, 25))
print(randrange(12, 25, 2))


mi_lista = [1, True, False, "Orca", {"key": "value"}]

print(choice(mi_lista))
print(choice("abracadabra"))


#################
# 15
####################

import sys

print(sys.argv)

for indice, argumento in enumerate(sys.argv):
    print(f"el argumento nro {indice} es {argumento} y es del tipo {type(argumento)}")


#################
# 16
####################
import sys


def imprimir_suma(a, b):
    print(a+b)


if len(sys.argv) == 3:
    mi_numero = int(sys.argv[1])
    mi_otro_numero = int(sys.argv[2])
    imprimir_suma(mi_numero, mi_otro_numero)
else:
    print("Se requieren exactamente  2 argumentos")