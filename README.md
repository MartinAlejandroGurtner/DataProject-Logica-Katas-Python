# Proyecto Lógica: Katas de Python

## Objetivo

Este proyecto reúne las katas del módulo de Python del Máster en Data Analytics de ThePowerMBA. El objetivo es practicar los fundamentos del lenguaje y resolver problemas con funciones, colecciones, condicionales, bucles, excepciones y clases.

El trabajo sigue el orden del enunciado y mantiene cada ejercicio identificado en el código. He priorizado soluciones legibles y comentarios en las partes donde la lógica es menos inmediata.

## Herramientas

- Python 3 (solo biblioteca estándar).
- Editor de código compatible con archivos `.py`.
- Terminal para ejecutar el archivo y sus ejemplos.

No hace falta instalar dependencias externas.

## Archivos

- `katas_python.py`: soluciones de las katas, con comentarios de los enunciados y ejemplos de funcionamiento.

## Cómo ejecutarlo

Desde una terminal, situándose en la carpeta del proyecto:

```bash
python katas_python.py
```

Este comando muestra ejemplos de varias funciones, entre ellas la recursividad, las clases `Arbol` y `UsuarioBanco`, y el procesado de texto.

Para probar los programas que necesitan entradas por teclado (ejercicios 8, 11, 31, 38, 39 y 41):

```bash
python katas_python.py --interactivo
```

Se abre un menú en el que se indica el número de ejercicio que se quiere ejecutar. En algunos equipos Windows el comando puede ser `py` en lugar de `python`.

También se pueden importar las funciones en otro script o desde la consola de Python para probar valores distintos.

## Enfoque seguido

Los primeros ejercicios trabajan operaciones básicas y estructuras de datos. Después se introducen funciones de orden superior (`map`, `filter`, `reduce`), funciones lambda y comprobaciones de entrada. Los ejercicios más avanzados incluyen clases y métodos, como la estructura de un árbol y la gestión básica del saldo entre dos cuentas.

He separado la lógica de cálculo de la entrada de datos siempre que ha sido posible. Así es más sencillo comprobar una función con distintos ejemplos sin tener que introducir datos cada vez que se ejecuta el archivo. En los ejercicios que piden expresamente usar `map`, `filter` o `reduce`, he mantenido esas herramientas.

## Observaciones del enunciado

**Ejercicio 35.** El documento facilitado salta del 34 al 36. Por eso se mantiene una nota en el código, pero no se inventa una solución para un enunciado que no aparece.

**Ejercicio 34.** Para eliminar la rama de la posición 2 se interpreta que las posiciones empiezan en 1, de modo que se elimina la segunda rama de la lista.

**Ejercicio 36.** El caso de uso tiene una inconsistencia: Bob comienza con 50 y recibe 20, por lo que cuenta con 70. La transferencia de 80 a Alicia no puede completarse sin saldo suficiente. La clase lanza la excepción correspondiente y el ejemplo muestra cómo se gestiona, sin modificar los importes del enunciado.

**Ejercicio 38.** El PDF no define las horas a partir de las cuales empieza el día o la tarde. Para resolverlo se han establecido los siguientes intervalos: día de 06:00 a 13:59, tarde de 14:00 a 19:59 y noche de 20:00 a 05:59.

## Comprobación

Las funciones pueden verificarse con distintos valores de entrada. En especial, conviene probar casos límite: listas vacías, divisiones entre cero, duplicados, saldos insuficientes, horas fuera de rango y descuentos mayores que el precio de compra.

La comprobación definitiva de la entrega debe hacerse ejecutando el archivo en el equipo desde el que se presenta el proyecto.
