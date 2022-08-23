# Funciones: guía de ejercicios


1. Escribir una función que imprima el mensaje "Hello World!"
```bash
>> Hello world!
```
2. Escribir una función que no reciba parámetros, que en su cuerpo genere dos variables `mi_numero` y `mi_numero_2` con valores `10` y `20` y que imprima la suma. El resultado debería ser:
```bash
>> La suma es: 30
```
3. Escribir una función que reciba un parámetro (o argumento). La función tiene que imprimir un mensaje reportando cuál es el valor del parámetro que recibió. Por ejemplo, si recibe un `string` "esto es un texto", la función debe imprimir
```bash
>> "he recibido como parametro: esto es un texto"
```
4. Dada la siguiente función:

```python
def mi_funcion(a, b):
    x = a + b
    return x
```
   
    i. Escribir un código que imprima la suma de dos números
    ii. Escribir un código que imprima la concatenación de dos strings 

5. Escribir una función que reciba un número como argumento y que imprima un mensaje donde se muestre el numero ingresado y seexplique si el número es par o impar. Por ejemplo, si la función se llama `mi_funcion` entonces:
```python
mi_funcion(5)
>> "El numero 5 es impar"

mi_funcion(4)
>> "El numero 4 es par"
```

6. Tomar la función definida en el punto anterior y agregar el siguiente comportamiento: si el argumento pasado a la misma no es un entero `int` entonces tiene que imprimir un mensaje que diga "Argumento incorrecto" y explique el tipo de argumento recibido, por ejemplo:
```python
mi_funcion([1,23,4])
>> "Argumento incorrecto: <class 'list'>"

mi_funcion("4")
>> "Argumento incorrecto: <class 'str'>"
```

7. Implementar una función que reciba dos argumentos. Si por lo menos uno de los dos argumentos no son strings `str` entonces que devuelva el valor `False`, en cambio si los dos argumentos son strings, que devuelva el conjunto de caracteres que consituyen ambos argumentos, en mayúsculas. Por ejemplo, si la función se llama `mi_funcion`:
```python
res = mi_funcion(1, "bowie")
print(f"el resultado es: {res}")
>> el resultado es: False

res = mi_funcion(1, [])
print(f"el resultado es: {res}")
>> el resultado es: False

res = mi_funcion("a", "b")
print(f"el resultado es: {res}")
>> el resultado es: {'A', 'B'}

res = mi_funcion("david", "bowie")
print(f"el resultado es: {res}")
>> el resultado es: {'V', 'B', 'O', 'D', 'E', 'A', 'I', 'W'}
```