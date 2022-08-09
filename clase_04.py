
#repaso
nombre = "mariano"
edad = 37


cond_1 = nombre != "****"
cond_2 = edad > 10 and edad < 18
cond_3 = len(nombre) >= 3 and len(nombre) < 10
cond_4 = edad * 4 > 40

mi_variable = cond_1 and cond_2 and cond_3 and cond_4

print("cond 1: " + str(cond_1))
print("cond 2: " + str(cond_2))
print("cond 3: " + str(cond_3))
print("cond 4: " + str(cond_4))

print("mi variable:" + str(mi_variable))

# Primer ejemplo de control de flujo condicional

print("hola")

mi_condicion = 300 > 200

if mi_condicion:
    print("mundo")
    print("loco")
else:
    print("clase")
    print("de coder")
    print("python")

print("como estan?")

# OTRO EJEMPLO
mi_edad = 7

print(mi_edad)


if mi_edad <= 5:
    print("nivel inicial")
else:
    if mi_edad > 5 and mi_edad <= 12:
        print("nivel primario")
    else:
        if mi_edad > 12 and mi_edad <= 17:
            print("nivel secundario")
        else:
            if mi_edad > 17:
                print("nivel universitario")


print("fin")

# ELIF
mi_edad = 21

print(mi_edad)


if mi_edad <= 5:
    print("nivel inicial")

elif mi_edad > 5 and mi_edad <= 12:
    print("nivel primario")

elif mi_edad > 12 and mi_edad <= 17:
    print("nivel secundario")

elif mi_edad > 17:
    print("nivel universitario")

print("fin")

# EJEMPLO not
mi_variable = 20 > 150

if not mi_variable:

    print("es verdad!")

print("fin")

# EJEMPLO CONDICION COMPUESTA
mi_variable = 200 > 150

mi_otra_varible = "mariano" == "mariano"


print("mi_variable: " + str(mi_variable))
print("mi_otra_varible: " + str(mi_otra_varible))

if mi_variable and mi_otra_varible:
    print("las dos son verdaderas")


print("fin")