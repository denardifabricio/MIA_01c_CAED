# Ejercicio 3: Alineación de Secuencias de Nucleótidos

## Parte 1: Conceptos Teóricos

El estudiante deberá investigar y redactar un documento (1–2 páginas) explicando:

1. Qué es una secuencia de nucleótidos y por qué su comparación es importante en biología molecular.

2. Qué es una alineación de secuencias, diferenciando entre:
   - Alineación global y alineación local.
   - Coincidencias (matches), desajustes (mismatches) y huecos (gaps).

3. El modelo de puntuación usado para alinear secuencias:
   - Reglas de puntuación para coincidencias y desajustes.
   - Penalización por apertura y extensión de huecos.

4. Una descripción conceptual del algoritmo de Needleman–Wunsch, incluyendo:
   - Construcción de la matriz de programación dinámica.
   - Ecuación de recurrencia.
   - Proceso de traceback para recuperar el alineamiento óptimo.

El documento debe incluir al menos una referencia bibliográfica confiable.

## Parte 2: Implementación del Algoritmo

El estudiante deberá implementar en el lenguaje de programación de su preferencia (se recomienda Python) un programa que:

1. Reciba varias parejas de secuencias de nucleótidos, por ejemplo:
   - ("GATTACA", "GCATGCU")
   - ("ACGT", "ACCT")
   - ("ATGCT", "AGCT")

2. Implemente desde cero el algoritmo de Needleman–Wunsch utilizando el siguiente esquema de puntuación:
   - Match = +1
   - Mismatch = –1
   - Gap = –2

3. Genere como salida, para cada pareja de secuencias:
   - La matriz de puntuación completa.
   - El alineamiento global óptimo entre ambas secuencias.
   - El puntaje final del alineamiento.


# Resolución
- Un informe en PDF con la parte teórica y una explicación breve del código implementado.
El informe teórico puede verse [aquí](Informe.pdf).

- El código fuente debidamente comentado.
El código fuente puede verse en [needleman_winsch.py](needleman_wunsch.py)

- Una captura o impresión de los alineamientos generados por el programa.
Se deja un video con la ejecución del algoritmo [aquí](https://drive.google.com/file/d/1kL5Bx45YSIY701X8oVuYyxWKSQZOOvHc/view?usp=sharing).