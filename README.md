# Notas - Curso básico de Python

![](https://static.platzi.com/media/avatars/Platzi-f730e65b-e92b-44d3-81c0-5c59c4dc4658.png) ![](https://static.platzi.com/media/learningpath/badges/46.png) ![](https://static.platzi.com/media/achievements/badge-basico-python-bdcc67b3-031d-4dce-8e78-5699fb243149.png)


**Tabla de Contenidos**

[TOCM]

[TOC]

# Introducción

## ¿Por qué Python?

Campos profesionales en tecnología que utilizan este lenguaje de programación:
- **Frontend:** Se encarga de llevar el diseño de una aplicación o sitio web a código.
- **IoT:** Se encarga de darle la capacidad de conectarse a internet a elementos que pueden estar a nuestro alrededor.
- **IA:** Se encarga de enseñarle a la computadora a resolver un determinado problema sin la necesidad de estar involucrados constantemente.
- **Backend:** Se encarga de crear la lógica con la cual va a funcionar una determinada aplicación y que va a ser almacenada en un servidor.
- **DevOps:** Se encarga de manejar la información almacenada en la nube de una determinada aplicación.
- **Data Science:** Se encarga de tomar la información relevante de un determinado ambiente y poder sacar conclusiones al respecto.
- **Video juegos:** Se encarga de combinar la programación, el diseño y la música para generar grandes experiencias a los usuarios.
- **Desarrollo móvil:** Se encarga de crear aplicaciones que serán almacenadas en la PlayStore o AppStore, y que podremos hacer uso de ellas desde nuestros smartphones.

Grandes  empresas que utilizan Python:

> Creo que todo empezó porque los primeros que trabajaron en Google (Sergey, Larry, Craig, …) tomaron una buena decisión de ingenieria: «Python donde podemos, C++ donde debemos.»

- [Google](http://https://stackoverflow.com/questions/2560310/heavy-usage-of-python-at-google/2561008#2561008 "Google")

- [Netflix](http:/https://netflixtechblog.com/python-at-netflix-86b6028b3b3e/ "Netflix")

- [Uber](https://eng.uber.com/tech-stack-part-one-foundation/tp:// "Uber")

- [NASA](http://https://www.nccs.nasa.gov/nccs-users/user-events/python-classes "NASA")

- [Tesla](https://wildentrepreneur.org/elon-musk-esta-contratando-para-tesla-y-no-le-importa-si-los-solicitantes-no-tienen-titulo-universitario/p:// "Tesla")

## ¿Que es un algoritmo?
- Serie de pasos ordenados para resolver un problema.
- Finito:  Debe tener un principio claro y un final claro.
- No es ambiguo: No puede significar algo en un contexto y otra cosa en otro contexto.

## Herramientas de trabajo
Las mejores herramientas para trabajar con este lenguaje son:

**1. Python 3.9.7 ó superior:** En su sitio oficial [Python.org](https://www.python.org/ "Python.org") se puede descargar el software de Python para Windows en su versión actual 3.9.7.

**2. La terminal ó consola:** Es una forma generalizada de llamar a la interfaz de usuario de línea de comandos: una pantalla (generalmente, de color de fondo negro sobre letras blancas) donde escribiendo comandos (secuencias de palabras especiales) ordenamos al sistema realizar acciones concretas.
Para este caso se utilizará [CMDER](https://cmder.net/ "CMDER") como nuestra terminal, es organizada y estilizada para trabajar.

**3. Editor de código:** Permiten editar código fuente en diversos lenguajes de programación y ofrecen múltiples herramientas para facilitar el trabajo y aumentar la productividad.
El editor seleccionado por preferencia es [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code") este se puede configurar para modificar los temas, colores, fuentes y algunas otras extensiones.

# Conceptos básicos de Python

## Explorando operadores aritméticos
Dentro de nuestra terminal se inicializa Python con el comando **py** y se podrán utilizar los operadores aritméticos básicos como:

- Suma: **+**
- Resta: **-**
- División: **/**
- Multiplicación: *****
- Cociente de una división: **//**
- Residuo de una división: **%**

[![img1](https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/1.png)](https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/1.png)

## Variables y Tipos de datos
**Variable** hace referencia a un objeto que reside en la memoria. El objeto puede ser de alguno de los tipos vistos (número o cadena de texto), o alguno de los otros tipos existentes en Python.

Cada variable debe tener un nombre único llamado identificador. Eso es muy de ayuda pensar las variables como contenedores que contienen data el cual puede ser cambiado después a través de técnicas de programación.


Los tipos de datos mas comunes o primitivos son:

[![2](https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/2.png "2")](http://https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/2.png "2")

Tipos de datos en Python:

- Text Type: str
- Numeric Types: int, float, complex
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Boolean Type: bool
- Binary Types: bytes, bytearray, memoryview

[![3](https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/3.png "3")](httphttps://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/3.png:// "3")

## Convertir un dato en un tipo diferente de dato

- **input("")** para pedirle al usuario que introduzca datos.
- **int()** con datos o variables dentro de parentesis para convertirlo en número entero.
- **str()** para convertir números tanto decimales como enteros a strings.

[![4](https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/4.png "4")](http://https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/4.png "4")

## Operadores lógicos y de comparación
- **and** para comparar si dos valores son verdaderos.
- **or** cuando quieres saber si al menos una de tus variables cuenta con los requisitos que buscas.
- **not** para invertir el valor booleano.
- **==** compara dos valores y te dice si son iguales o no.
- **!=** Compara dos valores y te dice sin son diferentes o no.
- **>** Compara si es mayor que otro valor.
- **<** Compara si es menor que otro valor.
- **>=** igual o mayor que el valor a comparar.
- **<=** igual o menor que el valor a comparar.

[![5](https://github.com/hackmilo/Notas---Curso-b-sico-de-Python/blob/main/img/5.png?raw=true "5")](http://https://github.com/hackmilo/Notas---Curso-b-sico-de-Python/blob/main/img/5.png?raw=true "5")

[![6](https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/6.png "6")](http://https://raw.githubusercontent.com/hackmilo/Notas---Curso-b-sico-de-Python/main/img/6.png "6")

## Primer programa: Convertir moneda local a dólares
Para el primer programa se hará un conversor de moneda local a dólares para esto se crea el archivo **conversor.py** y se abre por medio de **VS Code** para editarlo, primero declaramos la variable pesos que recibirá el valor en COP que el usuario quiere pasar a USD (Lo escrito despues de un **#** hace refencia a un comentario, no lo leerá el programa al ser ejecutado):
```python
pesos = input("¿Cuantos pesos colombianos tienes?: ")
pesos = float(pesos) #De tipo flotante para que acepte decimales
valor dolar = 3668
dolares = pesos / valor_dolar
dolares = round(dolares, 2) #Función para redondear con 2 decimales
dolares = str(dolares) #Pasa a ser texto para imprimir respuesta
print("Tienes $" + dolares + " dólares")
```
Al ejecutarlo en nuestra terminal **Cmder** utilizando el comando **py** y luego el nombre del achivo nos arroja los siguientes resultados:

[![7](https://github.com/hackmilo/Notas---Curso-b-sico-de-Python/blob/main/img/7.png?raw=true "7")](http://https://github.com/hackmilo/Notas---Curso-b-sico-de-Python/blob/main/img/7.png?raw=true "7")

# Herramientas para programar

## Condicionales
La diferencia entre **if, elif y else**, y también el tema de hacer comentarios en el código.
- **if:** Con el ejemplo del código de esta clase: **if opcion == 1**. Aquí, si lo “traducimos”, sería “Si el usuario elige la opción 1, entonces…” y luego viene todo el código por debajo que conocemos como bloque de código.
- **else:** Si se desea ejecutar otro código en caso de que no se cumpla el if. Ósea, si por ejemplo, el usuario no elige la opción 1, entonces (else)…
- **elif:** Se utiliza cuando utilizamos múltiples condiciones, lo que en el código de esta clase son la opción 2 y 3. En esta clase, teníamos la opción 1, pero debemos también evaluar qué pasa si el usuario elige la opción 2 o 3, por lo que decimos “que estamos evaluando múltiples condiciones”.

Ejemplo 1: Un programa para saber si un número dado por el usuario es mayor, menor o igual a 5.

```python
numero = int(input("Escribe un numero: "))
if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")
```
Ejemplo 2: Programa para saber si al ingresar la edad del usuario será mayor o menor de edad:

```python
edad = int(input("Escribe tu edad: "))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```
**Comentarios en Python:**

Para realizar un comentario (de una sola línea), utilizamos el “#”. Un comentario es simplemente texto, el cual no es ejecutado y no afecta en absoluto en el código. Se utiliza para explicar las líneas de código. Para qué veas cómo se utiliza, mira este ejemplo:
`dolar = str(dolar) #Convierte el resultado (número) en un string.`

## Mejora de conversor con condicionales

Teniendo en cuenta el uso de condicionales podemos mejorar un poco nuestro conversor de moneda y tambien agregar un menú para que el usuario escoja la moneda que quiere cambiar a dolares:

```python
menu = """  
Bienvenido al conversor de monedas  👌💰📈

1 - Pesos colombianos 
2 - Pesos argetinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
	pesos = float(pesos)
	valor dolar = 3668
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuantos pesos argentinos tienes?: ")
	pesos = float(pesos)
	valor dolar = 91.64
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuantos pesos mexicanos tienes?: ")
	pesos = float(pesos)
	valor dolar = 20.59
	dolares = pesos / valor_dolar
	dolares = round(dolares, 2)
	dolares = str(dolares)
	print("Tienes $" + dolares + " dólares")
else:
    print("Ingresa una opción correcta por favor")
```
## No repetir código con funciones

Una **función** es un bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea, este bloque puede ser llamados cuando se necesite. Para crear una función se utiliza el comando **def** y el nombre de la función.

El uso de funciones es un componente muy importante del paradigma de la programación llamada estructurada, y tiene varias ventajas:

- **Modularización:** permite segmentar un programa complejo en una serie de partes o módulos más simples, facilitando así la programación y el depurado.
- **Reutilización:** permite reutilizar una misma función en distintos programas.

Ejemplo: La función de una resta con los argumentos a y b.

```python
>>> def resta(a, b):
			return a - b

>>> resta(30, 10)
20
```

## Modularizando nuestro conversor de monedas

Aplicando el concepto anterior de función se logra reemplazar algunas lineas de código en el programa de conversor al modularizarlo:

```python
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """  
Bienvenido al conversor de monedas  👌💰📈

1 - Pesos colombianos 
2 - Pesos argetinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombiano", 3875)
elif opcion == 2:
    conversor("argetinos", 91.64)
elif opcion == 3:
    conversor("mexiacanos", 20.59)
else:
    print("Ingresa una opción correcta por favor")
```

## Cadenas de carácteres y funciones Built-in

Algunas funciones que nos ayudan a trabajar con texto o cadenas de carácteres:

- **variable.upper():** Todos los caracteres en MAYÚSCULAS.
- **variable.capitalize():** Solo la primera en MAYÚSCULA.
- **variable.lower()** Todos los caracteres en minúscula.
- **variable.strip()** Eliminar espacios basura del string.
- **variable.replace(carácter a cambiar, carácter por poner)** Remplazar carácter.
- **variable[x]** Traer el carácter número x.
- **len()** Cantidad de caracteres de la variable.

### Funciones Built-in

El intérprete de Python tiene una serie de funciones y tipos incluidos en él que están siempre disponibles, solo requiere que las invoquemos. Están listados aquí en orden alfabético.



## Slices o rebanadas

Los slices, traducidos al español como “rebanadas", nos permiten dividir los caracteres de un string de múltiples formas.
El formato completo de la rebanada es: **[start : end : step]**, usualmente solo usamos start y end.

Ejemplo:


## Proyecto: palíndromo
