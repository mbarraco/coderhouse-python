
###################################################
# Clase 15 - slide 32
###################################################

# from funciones import *
from funciones import imprimir_suma, imprimier_resta


imprimir_suma(1, 2)
imprimier_resta(5, 20)

#
# Otra versión
#
# from funciones import *
# from funciones import imprimir_suma, imprimier_resta
import funciones


funciones.imprimir_suma(1, 2)
funciones.imprimier_resta(5, 20)


###################################################
# Clase 15 - slide 46
###################################################


from mi_primer_paquete.modulo1 import llamar_al_modulo_1
from mi_primer_paquete.modulo2 import llamar_al_modulo_2

llamar_al_modulo_2()
llamar_al_modulo_1()
