# Algorítmos Divide y Vencerás

## Problema: Conteo de Inversiones

Enunciado: Sea A un array de los números 1, 2, ..., n en cualquier orden. Una inversión es una pareja (i, j) de índices del array, de forma que i < j pero A[i] > A[j]. Encuentre un algortimo tipo divide y vencerás que cuente el número de inversiones en un array A. Determine su complejidad en tiempo y en memoria. Implemente dicho algoritmo en su lenguaje de programación favorito con 3 arrays de ejemplo de longitud 10.

---

## Solución

### Descripción del Algoritmo

El algoritmo utiliza una estrategia divide y vencerás basada en la modificación del algoritmo Merge Sort. La idea clave es que se puede contar las inversiones mientras ordenamos el array.

#### Estrategia:

1. Dividir: se parte el array en dos mitades.
2. Conquistar: se cuenta recursivamente las inversiones en cada mitad.
3. Combinar: se cuenta las inversiones entre las dos mitades mientras las mezclamos en orden.

#### Insight Clave:

Cuando se mezcla dos subarrays ordenados (izquierdo y derecho):
- Si se toma un elemento del array derecho antes que elementos del array izquierdo, esto significa que el elemento derecho es menor que todos los elementos restantes del array izquierdo.
- Cada uno de estos elementos restantes forma una inversión con el elemento del array derecho.
- Por lo tanto, si hay `k` elementos restantes en el array izquierdo, contamos `k` inversiones.

### ¿Por qué Merge Sort y no otro algoritmo?

Esta es una pregunta que fue planteada antes de elegir el algoritmo base para entender por qué este enfoque es óptimo. Análisis las alternativas:

#### Quick Sort - No funciona eficientemente

Problema principal: Quick Sort no garantiza que los subarrays estén ordenados cuando los combina.

- Quick Sort divide el array usando un pivote (no necesariamente a la mitad)
- Después de particionar, los elementos menores que el pivote están a la izquierda y los mayores a la derecha
- PERO estos subarrays NO están ordenados internamente
- Por lo tanto, no se puede contar inversiones entre subarrays en tiempo lineal
- Se tendría que comparar cada elemento de la izquierda con cada elemento de la derecha: O(n²) en el paso de combinación
- Complejidad resultante: O(n²) en el peor caso


#### Merge Sort - La elección perfecta

Ventajas específicas para este problema:

1. Divide correctamente: Siempre divide el array exactamente a la mitad
   - Garantiza profundidad de recursión O(log n)

2. Subarrays ordenados: Después de la recursión, ambos subarrays están ordenados
   - Esto es crucial para contar inversiones eficientemente

3. Fase de mezcla O(n): La operación de merge es lineal
   - Podemos aprovechar esta fase para contar inversiones

4. Propiedad clave: Si `izq[i] > der[j]` y ambos están ordenados:
   - Sabemos que `izq[i]`, `izq[i+1]`, ..., `izq[último]` TODOS son mayores que `der[j]`
   - Podemos contar `len(izq) - i` inversiones en O(1)
   - Sin ordenamiento, tendríamos que verificar cada par individualmente

5. Estructura recursiva natural:
   ```
   Inversiones Totales = Inversiones(izquierda) 
                       + Inversiones(derecha) 
                       + Inversiones(entre ambas)
   ```
   Esta descomposición solo funciona si los subarrays están ordenados

#### 📊 Comparación de Algoritmos para Conteo de Inversiones

| Algoritmo | ¿Divide y Vencerás? | ¿Subarrays Ordenados? | Complejidad Temporal | ¿Funciona para conteo? |
|-----------|---------------------|-------------------------|----------------------|------------------------|
| Fuerza Bruta | No | No | O(n²) | Sí (pero lento) |
| Quick Sort | Sí | No | O(n log n) promedio | No eficientemente |
| Merge Sort | Sí | Sí | O(n log n) | Perfectamente |

#### Conclusión

Merge Sort es la ÚNICA opción entre los algoritmos de ordenamiento estándar que:
1. Tiene complejidad O(n log n)
2. Produce subarrays ordenados en cada paso
3. Tiene una fase de combinación donde podemos contar inversiones entre subarrays en tiempo lineal

La clave está en la propiedad de que los subarrays están ordenados, lo cual permite:
- Contar múltiples inversiones (len(izq) - i) en tiempo constante O(1)
- En lugar de verificar cada par individualmente O(n²)


### Análisis de Complejidad

#### Complejidad Temporal: O(n log n)

Justificación mediante el Teorema Fundamental (Master Theorem):

La recurrencia del algoritmo es:
```
T(n) = 2T(n/2) + O(n)
```

Donde:
- Dividimos el problema en 2 subproblemas (mitad izquierda y derecha)
- Cada subproblema es de tamaño n/2
- El trabajo de combinar (merge y conteo) es O(n)

Aplicando el Teorema Fundamental:

Tenemos la forma: `T(n) = aT(n/b) + O(n^d)`

Identificamos los parámetros:
- a = 2 (número de subproblemas recursivos)
- b = 2 (factor de reducción del tamaño)
- d = 1 (exponente del trabajo adicional, ya que O(n) = O(n^1))

Calculamos: a = 2 y b^d = 2^1 = 2

Como a = b^d (2 = 2), estamos en el caso 2 del teorema:

T(n) = O(n^d log n) = O(n^1 log n) = O(n log n)

Desglose intuitivo:
- Hay log n niveles de recursión (cada vez dividimos el array a la mitad hasta llegar a tamaño 1)
- En cada nivel, procesamos n elementos en total durante la fase de mezcla
- Total: O(n log n)

#### Complejidad Memoria: O(n)

Justificación:
- Necesitamos espacio adicional para:
  1. Los arrays auxiliares durante la fase de mezcla: `O(n)`
  2. La pila de recursión: `O(log n)` en profundidad
- Total: `O(n) + O(log n) = O(n)`

### Comparación con Fuerza Bruta

| Aspecto | Fuerza Bruta | Divide y Vencerás |
|---------|--------------|-------------------|
| Tiempo | O(n²) | O(n log n) |
| Espacio | O(1) | O(n) |


### Implementación

El algoritmo está implementado en Python en el archivo `conteo_inversiones.py`.

Funciones principales:
- `contar_inversiones(arr)`: Función principal que implementa el algoritmo divide y vencerás.
- `mezclar_y_contar(izq, der)`: Mezcla dos arrays ordenados y cuenta las inversiones entre ellos.
- `verificar_inversiones_fuerza_bruta(arr)`: Verificación mediante fuerza bruta para validar resultados. Esto se hace porque es un ejercicio académico y se necesita asegurarse que funciona correctamente. En una implementación en producción carercería de sentido.

### Casos de Prueba

Se implementaron 3 arrays de longitud 10 con diferentes características:

1. array casi ordenado (pocas inversiones):
   ```
   [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
   ```
   - Solo tiene 1 inversión: (5, 6) donde 7 > 6

2. array con inversiones moderadas:
   ```
   [3, 1, 5, 2, 8, 4, 9, 6, 10, 7]
   ```
   - Mezcla de elementos ordenados y desordenados

3. array en orden inverso (máximas inversiones):
   ```
   [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
   ```
   - Tiene el máximo número de inversiones posible: n(n-1)/2 = 45



### Ejecución

Para ejecutar el programa:

```bash
python conteo_inversiones.py
```

El programa mostrará:
- El array original
- Ejemplos de inversiones encontradas
- El número total de inversiones (calculado con divide y vencerás)
- Verificación del resultado (usando fuerza bruta)
- El array ordenado resultante
- Estadísticas adicionales

### Correctitud del Algoritmo

El algoritmo es correcto porque:

1. Caso base: Un array de tamaño ≤ 1 tiene 0 inversiones (correcto).

2. Paso recursivo: Las inversiones totales en un array se pueden clasificar en tres categorías:
   - Inversiones dentro de la mitad izquierda
   - Inversiones dentro de la mitad derecha  
   - Inversiones entre las dos mitades (elemento de la izquierda mayor que elemento de la derecha)

3. Combinación: Al mezclar dos subarrays ordenados, contamos correctamente las inversiones entre ellos:
   - Si `izq[i] > der[j]`, entonces `izq[i]` forma una inversión con `der[j]`
   - Además, todos los elementos después de `izq[i]` en el array izquierdo también forman inversiones con `der[j]`
   - Por lo tanto, sumamos `len(izq) - i` inversiones

