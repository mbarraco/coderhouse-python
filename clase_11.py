# Desafio slide 21
def dividir(a, b):
    if b == 0:
        return
    else:
        return a / b


print(dividir(4, 2) == 2)
print(dividir(9, 3) == 3)
print(dividir(2, 4) == 0.5)
print(dividir(0, 8) == 0)
print(dividir(8, 0) == None)
print(dividir(-1, 0) == None)
print(dividir(99, 0) == None)


# Slide 28: Try Except
def dividir(dividendo, divisor):
    a = dividendo  # no es necesario, es solo un ejemplo pedagogico
    b = divisor  # no es necesario, es solo un ejemplo pedagogico
    try:
        print("1")
        resultado = a / b
    except:
        print("2")
        resultado = None

    print("3")
    return resultado


dividir(divisor=1, dividendo=2)
print("*" * 90)
dividir(divisor=0, dividendo=2)


# SLIDE 34
# Try Except
while True:
    try:
        n = float(input("ingresar un numero: "))
        m = 4
        print("{}/{} = {}".format(n, m, n / m))
        break
    except:
        print(
            "ingresaste algo que no es posible de interpretar como numero, pruebe de nuevo\n"
        )

# SLIDE 37
while True:
    try:
        n = float(input("ingresar un numero: "))
    except:
        print(
            "ingresaste algo que no es posible de interpretar como numero, pruebe de nuevo\n"
        )
    else:
        m = 4
        print("{}/{} = {}".format(n, m, n / m))
        break

# SLIDE 41
while True:
    try:
        n = float(input("ingresar un numero: "))
    except:
        print(
            "ingresaste algo que no es posible de interpretar como numero, pruebe de nuevo\n"
        )
    else:
        m = 4
        print("{}/{} = {}".format(n, m, n / m))
        break
    finally:
        print("se ejecuto el FINALLY!")

# SLIDE 49 - codigo ejemplo alternativo

def dividir(a, b):
    try:
        resultado =  a / b
    except KeyError:
        return None
    except ZeroDivisionError:
        return None

    return resultado


print(dividir(4, 2) == 2)
print(dividir(9, 3) == 3)
print(dividir(2, 4) == 0.5)
print(dividir(0, 8) == 0)
print(dividir(8, 0) == None)
print(dividir(-1, 0) == None)
print(dividir(99, 0) == None)


# 49 alternativo II: atrapar y utilizar Exception
def dividir(a, b):
    try:
        return  a / b
    except Exception as e:
        print("El error es de tipo:", type(e))


dividir(9, 0)