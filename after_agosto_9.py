
nombre = "Mariana"
preferencia = "M" 
valor_esperado = "B"


nombre = "Nacho"
preferencia = "M" 
valor_esperado = "B"


nombre = "Silvia" 
preferencia = "M" 
valor_esperado = "B"


nombre = "Silvia" 
preferencia = "C" 
valor_esperado = "A"

nombre = "Alberto"
preferencia = "M" 
valor_esperado = "A"

nombre = "Alberto"
preferencia = "C" 
valor_esperado = "B"

nombre = "Mariana"
preferencia = "C" 
valor_esperado = "B"

nombre = "Nacho"
preferencia = "C" 
valor_esperado = "B"

##########################
# Codigo a testear

nombre = nombre.lower()

if preferencia== "M":
    print("1")
    if nombre[0] < "m":
        print("3")
        grupo = "A"
    else:
        print("4")
        grupo = "B"
else:
    print("2")
    if nombre[0] > "n":
        print("5")
        grupo = "A"
    else:
        print("6")
        grupo = "B"
##########################

print("nombre: " + nombre)
print("preferencia: " + preferencia)
print("el grupo es: " + grupo)
print("el valor esperado es: " + valor_esperado)

assert grupo == valor_esperado
print("finalice correctamente")
