<img src="https://github.com/hernancontigiani/ceia_memorias_especializacion/raw/master/Figures/logoFIUBA.jpg" width="500" align="center">

<p>&nbsp;</p>

# Computación, algoritmos y estructuras de datos - Trabajo Práctico Final

**Autor:**
- Esp. Ing. Fabricio Denardi  

**Docente:**
- Dr. Camilo Argoty

**Cohorte:**
- MIA 01-2025


<p>&nbsp;</p>

# Definición
El trabajo práctico final de la materia Computación, algoritmos y estructuras de datos de la Maestría en Inteligencia artificial (MIA) de la Universidad de Buenos Aires (UBA) consiste en la resolución de una serie de ejercicios relacionados con la temática vista.

# Ejercicios

## Ejercicio 1
Implementar una máquina de Turing que puede sumar dos números binarios. Se desarrolló una máquina con 3 cintas.

A su vez, se investigó y encontró información para realizar una versión con una única cinta, por lo que se implementó y comparó con la desarrollada por el alumno.
La resolución está en [Ejercicio 1](./Ejercicio1/Ejercicio1.md).

### Ejemplos
101+110 = 1011

1. **Versión de 1 cinta**: 
[suma_binaria_1_cinta_101+110.mov](https://drive.google.com/file/d/16Cg6Snkdgqv9JBCpi4O_rP3FWkof1WLe/view?usp=drive_link)
2. **Versión de 1 cinta**: 
[suma_binaria_3_cintas_101+110.mov](https://drive.google.com/file/d/1Tw2BcpaJVxhiYiwpn9wOpOkoh4mIuGJl/view?usp=drive_link)

## Ejercicio 2
Conteo de inversiones: Sea A un array de los números 1, 2, ..., n en cualquier orden. Una inversión es una pareja (i, j) de índices del array, de forma que i < j pero A[i] > A[j]. Encuentre un algortimo tipo divide y vencerás que cuente el número de inversiones en un array A. Determine su complejidad en tiempo y en memoria. Implemente dicho algoritmo en su lenguaje de programación favorito con 3 arrays de ejemplo de longitud 10.


La resolución está en [Ejercicio 2](./Ejercicio2/Ejercicio2.md).

## Ejercicio 3
En este ejercicio se aplicarán conceptos fundamentales de algoritmos y estructuras de datos en el contexto de la bioinformática, específicamente en la alineación global de secuencias de nucleótidos. El objetivo es comprender cómo los algoritmos permiten comparar secuencias biológicas para identificar similitudes, mutaciones y relaciones evolutivas.


La resolución está en [Ejercicio 3](./Ejercicio3/Ejercicio3.md).


### A modo de resumen: resolución
- Un informe en PDF con la parte teórica y una explicación breve del código implementado.

Si bien se solicitó 1 o 2 páginas, dado que lo hice con LaTex (suelen ser más páginas comparadas con un word) y quise hacerlo más completo, el infrome poseé más páginas.

El informe teórico puede verse [aquí](./Ejercicio3/Informe.pdf).

- El código fuente debidamente comentado.
El código fuente puede verse en [needleman_winsch.py](./Ejercicio3/needleman_wunsch.py)

- Una captura o impresión de los alineamientos generados por el programa.
Se deja un video con la ejecución del algoritmo [aquí](https://drive.google.com/file/d/1kL5Bx45YSIY701X8oVuYyxWKSQZOOvHc/view?usp=sharing).