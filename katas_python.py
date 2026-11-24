"""Proyecto Lógica: Katas de Python — ThePowerMBA.

Soluciones a los ejercicios del enunciado. Las funciones se pueden importar
sin ejecutar preguntas interactivas. Para ver ejemplos: python katas_python.py
Para ejecutar los ejercicios que piden datos: python katas_python.py --interactivo
"""

from collections import Counter
from functools import reduce
from math import pi
from operator import mul, sub
import re
import sys


# EJERCICIO 1.
# Escribe una función que reciba una cadena y devuelva un diccionario con las
# frecuencias de cada letra. Los espacios no deben ser considerados.
def frecuencia_letras(texto):
    frecuencias = {}
    for caracter in texto:
        if caracter.isalpha():
            letra = caracter.lower()
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias


# EJERCICIO 2.
# Dada una lista de números, obtén otra con el doble de cada valor usando map().
def duplicar_numeros(numeros):
    return list(map(lambda numero: numero * 2, numeros))


# EJERCICIO 3.
# Recibe una lista de palabras y una palabra objetivo. Devuelve las palabras
# de la lista que contengan la palabra objetivo.
def palabras_que_contienen(palabras, objetivo):
    return [palabra for palabra in palabras if objetivo.lower() in palabra.lower()]


# EJERCICIO 4.
# Calcula la diferencia entre los valores de dos listas utilizando map().
def restar_listas(lista_a, lista_b):
    if len(lista_a) != len(lista_b):
        raise ValueError("Las listas deben tener el mismo número de elementos")
    return list(map(lambda a, b: a - b, lista_a, lista_b))


# EJERCICIO 5.
# Recibe una lista de notas y una nota_aprobado opcional (por defecto 5).
# Devuelve una tupla con la media y el estado ('aprobado' o 'suspenso').
def evaluar_notas(notas, nota_aprobado=5):
    if not notas:
        raise ValueError("No se puede calcular una media sin notas")
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# EJERCICIO 6.
# Calcula el factorial de un número de manera recursiva.
def factorial_recursivo(numero):
    if type(numero) is not int or numero < 0:
        raise ValueError("El factorial requiere un entero no negativo")
    if numero <= 1:
        return 1
    return numero * factorial_recursivo(numero - 1)


# EJERCICIO 7.
# Convierte una lista de tuplas en una lista de strings usando map().
def tuplas_a_texto(tuplas):
    return list(map(str, tuplas))


# EJERCICIO 8.
# Pide dos números al usuario e intenta dividirlos. Maneja valores no numéricos
# y divisiones entre cero, e informa de si la operación ha tenido éxito.
def programa_division():
    try:
        numero_a = float(input("Primer número: "))
        numero_b = float(input("Segundo número: "))
        resultado = numero_a / numero_b
    except ValueError:
        print("La división no se ha podido realizar: introduce números válidos.")
    except ZeroDivisionError:
        print("La división no se ha podido realizar: divisor igual a cero.")
    else:
        print(f"División realizada correctamente. Resultado: {resultado}")


# EJERCICIO 9.
# Filtra una lista de mascotas excluyendo: Mapache, Tigre, Serpiente Pitón,
# Cocodrilo y Oso. Utiliza filter().
def mascotas_permitidas(mascotas):
    prohibidas = {"mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"}
    return list(filter(lambda mascota: mascota.casefold() not in prohibidas, mascotas))


# EJERCICIO 10.
# Calcula el promedio de una lista y, si está vacía, lanza una excepción
# personalizada y maneja el error de forma adecuada.
class ListaVaciaError(Exception):
    """Error específico para una lista sin elementos."""


def promedio_con_excepcion(numeros):
    if not numeros:
        raise ListaVaciaError("No hay valores para calcular el promedio")
    return sum(numeros) / len(numeros)


def mostrar_promedio(numeros):
    try:
        print(f"Promedio: {promedio_con_excepcion(numeros):.2f}")
    except ListaVaciaError as error:
        print(f"No se pudo calcular el promedio: {error}")


# EJERCICIO 11.
# Pide una edad; maneja valores no numéricos y edades fuera del rango 0 a 120.
def programa_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if not 0 <= edad <= 120:
            raise ValueError("La edad debe estar entre 0 y 120")
    except ValueError as error:
        print(f"Edad no válida: {error}")
    else:
        print(f"Edad registrada: {edad} años")


# EJERCICIO 12.
# Dada una frase, devuelve la longitud de cada palabra usando map().
def longitudes_palabras(frase):
    return list(map(len, frase.split()))


# EJERCICIO 13.
# Para un conjunto de caracteres, devuelve tuplas con cada letra en mayúscula
# y minúscula, sin repetir letras. Usa map().
def letras_mayusculas_minusculas(caracteres):
    # Normalizo primero para que 'A' y 'a' no cuenten dos veces.
    letras = sorted({caracter.lower() for caracter in caracteres if caracter.isalpha()})
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras))


# EJERCICIO 14.
# Devuelve las palabras que comiencen por una letra especificada. Usa filter().
def palabras_que_empiezan(palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))


# EJERCICIO 15.
# Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres_a_lista = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# EJERCICIO 16.
# Recibe una cadena y un entero n; devuelve palabras con longitud mayor que n.
# Usa filter().
def palabras_mas_largas(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# EJERCICIO 17.
# Convierte una lista de dígitos en un número con reduce(). Ej.: [5, 7, 2] -> 572.
def digitos_a_numero(digitos):
    if any(type(digito) is not int or not 0 <= digito <= 9 for digito in digitos):
        raise ValueError("Cada elemento debe ser un dígito del 0 al 9")
    # En cada paso desplazamos el número acumulado una posición decimal.
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos, 0)


# EJERCICIO 18.
# Crea una lista de diccionarios de estudiantes (nombre, edad, calificación)
# y utiliza filter() para extraer los que tengan calificación >= 90.
ESTUDIANTES = [
    {"nombre": "Ana", "edad": 21, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 82},
    {"nombre": "Marta", "edad": 20, "calificacion": 91},
]


def estudiantes_destacados(estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


# EJERCICIO 19.
# Crea una función lambda que filtre los números impares de una lista.
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# EJERCICIO 20.
# Dada una lista de enteros y cadenas, conserva solo los valores int.
# Usa filter().
def solo_enteros(elementos):
    # type(...) is int evita incluir True/False (bool hereda de int en Python).
    return list(filter(lambda elemento: type(elemento) is int, elementos))


# EJERCICIO 21.
# Crea una función lambda que calcule el cubo de un número.
cubo = lambda numero: numero ** 3


# EJERCICIO 22.
# Obtén el producto de todos los números de una lista con reduce().
def producto_lista(numeros):
    return reduce(mul, numeros, 1)


# EJERCICIO 23.
# Concatena una lista de palabras con reduce().
def concatenar_palabras(palabras):
    return reduce(
        lambda acumulado, palabra: (acumulado + " " + palabra) if acumulado else palabra,
        palabras,
        "",
    )


# EJERCICIO 24.
# Calcula la diferencia total de una lista con reduce().
def diferencia_total(numeros):
    if not numeros:
        raise ValueError("La lista debe contener al menos un número")
    # Se resta en orden: el primer número menos los siguientes.
    return reduce(sub, numeros)


# EJERCICIO 25.
# Cuenta los caracteres de una cadena de texto dada.
def contar_caracteres(texto):
    return len(texto)


# EJERCICIO 26.
# Crea una lambda que calcule el resto de dividir dos números.
resto_division = lambda a, b: a % b


# EJERCICIO 27.
# Crea una función que calcule el promedio de una lista de números.
def promedio(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)


# EJERCICIO 28.
# Busca y devuelve el primer elemento duplicado de una lista.
def primer_duplicado(elementos):
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# EJERCICIO 29.
# Convierte una variable a texto y sustituye todos sus caracteres por '#',
# excepto los cuatro últimos.
def enmascarar(valor):
    texto = str(valor)
    return "#" * max(0, len(texto) - 4) + texto[-4:]


# EJERCICIO 30.
# Determina si dos palabras son anagramas: mismas letras en diferente orden.
def son_anagramas(palabra_a, palabra_b):
    a = palabra_a.replace(" ", "").lower()
    b = palabra_b.replace(" ", "").lower()
    return a != b and sorted(a) == sorted(b)


# EJERCICIO 31.
# Pide una lista de nombres y otro nombre para buscar. Si no está, lanza
# una excepción; si está, muestra un mensaje indicando que se encontró.
def buscar_nombre(nombres, objetivo):
    if objetivo.casefold() not in {nombre.casefold() for nombre in nombres}:
        raise LookupError(f"El nombre {objetivo} no aparece en la lista")
    return True


def programa_buscar_nombre():
    nombres = [nombre.strip() for nombre in input("Nombres separados por comas: ").split(",")]
    objetivo = input("Nombre a buscar: ").strip()
    try:
        buscar_nombre(nombres, objetivo)
    except LookupError as error:
        print(error)
    else:
        print(f"Se ha encontrado a {objetivo}")


# EJERCICIO 32.
# Recibe nombre completo y lista de empleados. Si figura en la lista,
# devuelve su puesto; si no, indica que no trabaja aquí.
def puesto_empleado(nombre_completo, empleados):
    # La lista de empleados se representa mediante diccionarios con nombre y puesto.
    for empleado in empleados:
        if empleado["nombre"].casefold() == nombre_completo.casefold():
            return empleado["puesto"]
    return "La persona no trabaja aquí"


# EJERCICIO 33.
# Crea una función lambda que sume los elementos correspondientes de dos listas.
sumar_listas = lambda lista_a, lista_b: list(map(lambda a, b: a + b, lista_a, lista_b))


# EJERCICIO 34.
# Crea la clase Arbol: inicia con tronco de longitud 1 y sin ramas.
# Métodos: crecer_tronco (+1), nueva_rama (longitud 1), crecer_ramas (+1
# en todas), quitar_rama (por posición) e info_arbol (longitud del tronco,
# cantidad de ramas y longitudes). Prueba el caso de uso del enunciado.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        # Interpretamos posición 2 como la segunda rama (numeración desde 1).
        if not 1 <= posicion <= len(self.ramas):
            raise IndexError("No existe una rama en esa posición")
        self.ramas.pop(posicion - 1)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy(),
        }


def ejemplo_arbol():
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    return arbol.info_arbol()


# EJERCICIO 35.
# No existe el enunciado número 35 en el PDF facilitado; pasa del 34 al 36.
# Se conserva este número a modo de referencia, sin inventar una kata.


# EJERCICIO 36.
# Crea la clase UsuarioBanco (nombre, saldo, cuenta corriente).
# Métodos: retirar_dinero (error cuando no se pueda), transferir_dinero
# desde otro usuario al actual y agregar_dinero.
# Caso de uso: Alicia (100) y Bob (50), ingresar 20 a Bob, transferir 80
# desde Bob a Alicia y retirar 50 a Alicia.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("El usuario no dispone de cuenta corriente")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # Transferimos desde 'otro_usuario' hacia el usuario actual.
        if not self.cuenta_corriente:
            raise ValueError("El destinatario no tiene cuenta corriente")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad


def ejemplo_banco():
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    try:
        # Bob tiene 70, así que la transferencia de 80 debe fallar.
        alicia.transferir_dinero(bob, 80)
    except ValueError as error:
        mensaje = f"Transferencia rechazada: {error}"
    else:
        mensaje = "Transferencia realizada"
    alicia.retirar_dinero(50)
    return {"mensaje": mensaje, "saldo_alicia": alicia.saldo, "saldo_bob": bob.saldo}


# EJERCICIO 37.
# Define contar_palabras (diccionario de frecuencias), reemplazar_palabras
# (palabra original por una nueva) y eliminar_palabra. Implementa
# procesar_texto(texto, opcion, *args) con opciones contar/reemplazar/eliminar.
def contar_palabras(texto):
    palabras = re.findall(r"\b\w+\b", texto.casefold())
    return dict(Counter(palabras))


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    patron = r"\b" + re.escape(palabra_original) + r"\b"
    return re.sub(patron, palabra_nueva, texto)


def eliminar_palabra(texto, palabra):
    patron = r"\b" + re.escape(palabra) + r"\b"
    resultado = re.sub(patron, "", texto)
    return re.sub(r"\s+", " ", resultado).strip()


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        if args:
            raise ValueError("'contar' no necesita argumentos adicionales")
        return contar_palabras(texto)
    if opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("'reemplazar' necesita palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    if opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("'eliminar' necesita la palabra que se quiere quitar")
        return eliminar_palabra(texto, args[0])
    raise ValueError("Opción no reconocida: contar, reemplazar o eliminar")


# EJERCICIO 38.
# Pide una hora y determina si es noche, día o tarde.
def momento_del_dia(hora):
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23")
    # Franjas elegidas para la kata; el PDF no concreta horas de corte.
    if 6 <= hora < 14:
        return "día"
    if 14 <= hora < 20:
        return "tarde"
    return "noche"


def programa_momento_dia():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        print(f"Es de {momento_del_dia(hora)}")
    except ValueError as error:
        print(f"Hora no válida: {error}")


# EJERCICIO 39.
# Convierte una nota numérica en texto: 0-69 insuficiente; 70-79 bien;
# 80-89 muy bien; 90-100 excelente.
def calificacion_texto(nota):
    if not 0 <= nota <= 100:
        raise ValueError("La calificación debe estar entre 0 y 100")
    if nota < 70:
        return "insuficiente"
    if nota < 80:
        return "bien"
    if nota < 90:
        return "muy bien"
    return "excelente"


def programa_calificacion():
    try:
        nota = float(input("Calificación (0-100): "))
        print(f"Resultado: {calificacion_texto(nota)}")
    except ValueError as error:
        print(f"Calificación no válida: {error}")


# EJERCICIO 40.
# Escribe una función que tome figura ('rectangulo', 'circulo', 'triangulo')
# y datos (tupla) y calcule el área correspondiente.
def calcular_area(figura, datos):
    if figura == "rectangulo" and len(datos) == 2:
        base, altura = datos
        area = base * altura
    elif figura == "circulo" and len(datos) == 1:
        (radio,) = datos
        area = pi * radio ** 2
    elif figura == "triangulo" and len(datos) == 2:
        base, altura = datos
        area = base * altura / 2
    else:
        raise ValueError("Figura desconocida o cantidad de medidas incorrecta")
    if any(medida <= 0 for medida in datos):
        raise ValueError("Las medidas deben ser positivas")
    return area


# EJERCICIO 41.
# Programa de compra en línea: pide precio original, pregunta si tiene cupón,
# solicita importe del cupón si responde que sí, aplica un descuento positivo
# y muestra el total final. Utiliza if/elif/else.
def precio_final(precio, cupon=0):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if cupon < 0:
        raise ValueError("El descuento no puede ser negativo")
    return max(0, precio - cupon)


def programa_compra():
    try:
        precio = float(input("Precio original (€): "))
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        respuesta = input("¿Tienes cupón? (sí/no): ").strip().casefold()
        if respuesta in ("sí", "si"):
            descuento = float(input("Importe del cupón (€): "))
            if descuento > 0:
                total = precio_final(precio, descuento)
            else:
                print("Cupón no válido; se mantiene el precio original.")
                total = precio
        elif respuesta == "no":
            total = precio
        else:
            raise ValueError("Responde sí o no")
        print(f"Precio final: {total:.2f} €")
    except ValueError as error:
        print(f"No se ha podido completar el cálculo: {error}")


def mostrar_ejemplos():
    """Pruebas sencillas de los casos de uso, sin pedir datos al usuario."""
    print("1. Frecuencias:", frecuencia_letras("Hola hola"))
    print("2. Duplicar:", duplicar_numeros([2, 4, 6]))
    print("5. Notas:", evaluar_notas([6, 7, 8]))
    print("6. Factorial:", factorial_recursivo(5))
    print("10. Promedio:", promedio_con_excepcion([3, 5, 7]))
    print("17. Dígitos:", digitos_a_numero([5, 7, 2]))
    print("18. Estudiantes:", estudiantes_destacados(ESTUDIANTES))
    print("28. Primer duplicado:", primer_duplicado([2, 4, 3, 4, 2]))
    print("34. Árbol:", ejemplo_arbol())
    print("36. Banco:", ejemplo_banco())
    print("37. Texto (contar):", procesar_texto("Datos y más datos", "contar"))
    print("37. Texto (reemplazar):", procesar_texto("datos útiles", "reemplazar", "datos", "cifras"))
    print("37. Texto (eliminar):", procesar_texto("datos útiles", "eliminar", "útiles"))
    print("40. Área de un círculo:", round(calcular_area("circulo", (3,)), 2))


def menu_interactivo():
    programas = {
        "8": programa_division,
        "11": programa_edad,
        "31": programa_buscar_nombre,
        "38": programa_momento_dia,
        "39": programa_calificacion,
        "41": programa_compra,
    }
    print("Ejercicios interactivos disponibles: " + ", ".join(programas))
    numero = input("Indica el ejercicio que quieres ejecutar: ").strip()
    if numero in programas:
        programas[numero]()
    else:
        print("Elige uno de los ejercicios disponibles.")


if __name__ == "__main__":
    if "--interactivo" in sys.argv:
        menu_interactivo()
    else:
        mostrar_ejemplos()
