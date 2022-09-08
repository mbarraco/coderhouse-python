# Objetos: guía de ejercicios


1. Implementar una clase `Gato` que se inicialice con un `nombre`. Agregarle la acción `hablar`, cuando se llame a esta acción, el código debe imprimir en la consola el mensaje 
```bash
mi_gato = Gato("pancho")
mi_gato.hablar()

>> Miau! soy un gato
```

2. Modificar la clase anterior de forma tal que cuando "hagamos hablar" al gato, nos salude de la siguiente manera:
```bash
mi_gato = Gato("pancho")
mi_gato.hablar()

>> Miau! soy un gato y mi nombre es Pancho
```
**extra**: lograr imprimir el nombre del gato siempre en mayúscula independientemente de cómo lo haya ingresado el usuario, tal como en el ejemplo anterior.

3. Modificar la clase anterior para obtener el siguiente comportamiento:
```bash
mi_gato = Gato("pancho")
print(mi_gato)

>> Soy un objeto de la clase Gato y me llaman Pancho
```