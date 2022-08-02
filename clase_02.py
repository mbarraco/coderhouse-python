mi_lista = [1, 2, 3, 4, 5]
mi_otra_lista = [6, 7, 8, 9, 10]
mi_lista_duplicada = mi_lista * 2
mi_lista_triplicada = mi_lista * 3
las_dos_listas = mi_lista + mi_otra_lista
las_dos_listas_nuevamente = mi_lista.extend(mi_otra_lista)
nuevamente_las_dos_listas = mi_otra_lista.extend(mi_lista)

una_lista_mas_compleja = mi_lista.append(mi_otra_lista)


el_primer_elemento_de_mi_lista = mi_lista[0]
el_ultimo_elemento_de_mi_lista = mi_lista[-1]
los_dos_primeros_elementos_de_mi_lista = mi_lista[0:1]
las_posiciones_impares_de_mi_lista = mi_lista[0:]


mi_lista = [1, 'hola', [4, 'si, puedo', 6], ('x', 'z')]

type(mi_lista)
type(mi_lista[3])

mi_lista[2][2] = "python!"