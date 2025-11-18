"""
Algoritmo Divide y Vencerás para Conteo de Inversiones
========================================================

Una inversión en un array A es una pareja (i, j) donde i < j pero A[i] > A[j].

Este algoritmo utiliza una estrategia divide y vencerás similar a Merge Sort
para contar eficientemente el número de inversiones.

*** RELACIÓN CON MERGE SORT ***
================================================================================
Este algoritmo ES ESENCIALMENTE MERGE SORT con una modificación:

MERGE SORT ESTÁNDAR:
1. Divide: Partir el array en dos mitades
2. Conquista: Ordenar recursivamente cada mitad
3. Combina: Mezclar (merge) las dos mitades ordenadas

ALGORITMO DEL EJERCICIO (Merge Sort + Conteo):
1. Divide: Partir el array en dos mitades [IGUAL]
2. Conquista: Ordenar Y contar inversiones en cada mitad [MODIFICADO PARA RESOLVER EL PROBLEMA PLANTEADO]
3. Combina: Mezclar Y contar inversiones entre mitades [MODIFICADO PARA RESOLVER EL PROBLEMA PLANTEADO]

La diferencia clave está en la función merge():
- Merge Sort: solo mezcla
- EL algoritmo: mezcla Y cuenta cuando un elemento derecho < elemento izquierdo
  (lo cual indica una inversión)

Por eso tienen la MISMA complejidad temporal: O(n log n)
================================================================================

Complejidad:
- Tiempo: O(n log n)  [igual que Merge Sort]
- Espacio: O(n)       [igual que Merge Sort]

Autor: Implementación para CAED
Fecha: Noviembre 2025
"""


def contar_inversiones(arr):
    """
    Cuenta el número de inversiones en un array usando divide y vencerás.
    
    *** ESTA ES LA ESTRUCTURA BÁSICA DE MERGE SORT ***
    Este algoritmo sigue EXACTAMENTE la misma estructura que Merge Sort,
    pero además de ordenar, cuenta las inversiones.
    
    Args:
        arr: Lista de números a analizar
        
    Returns:
        tupla (arr_ordenado, num_inversiones)
    """
    # ========================================================================
    # PASO 1: CASO BASE (igual que Merge Sort)
    # ========================================================================
    '''Caso base: array de tamaño 0 o 1 no tiene inversiones
    En Merge Sort: un array de 1 elemento ya está ordenado
    En mi algoritmo: además, no tiene inversiones (0)'''
    if len(arr) <= 1:
        return arr.copy(), 0

    # ========================================================================
    # PASO 2: DIVIDIR (igual que Merge Sort)
    # ========================================================================
    '''Partir el array en dos mitades aproximadamente iguales
    Esto es EXACTAMENTE lo que hace Merge Sort'''
    medio = len(arr) // 2
    izquierda = arr[:medio]      # Primera mitad
    derecha = arr[medio:]        # Segunda mitad
    
    # ========================================================================
    # PASO 3: CONQUISTAR - Llamadas Recursivas (igual que Merge Sort)
    # ========================================================================
    ''' Resolver recursivamente para cada mitad
    En Merge Sort: ordenamos recursivamente cada mitad
    En mi algoritmo: ordenamos Y contamos inversiones en cada mitad'''
    izq_ordenada, inv_izq = contar_inversiones(izquierda)  # Resuelve mitad izquierda
    der_ordenada, inv_der = contar_inversiones(derecha)    # Resuelve mitad derecha
    
    # ========================================================================
    # PASO 4: COMBINAR - Mezcla (igual que Merge Sort + conteo de inversiones)
    # ========================================================================
    ''' Mezclar las dos mitades ordenadas en un solo array ordenado
    En Merge Sort: solo mezclamos (función merge)
    En nuestmiro algoritmo: mezclamos Y contamos inversiones entre mitades'''
    arr_ordenado, inv_mezcla = mezclar_y_contar(izq_ordenada, der_ordenada)
    
    # ========================================================================
    # PASO 5: ACUMULACIÓN DE RESULTADOS
    # ========================================================================
    '''Total de inversiones = inversiones izquierda + inversiones derecha + inversiones entre mitades
    Esta es la ÚNICA diferencia conceptual con Merge Sort:
    - Merge Sort solo retorna el array ordenado
    - Mi algoritmo retorna el array ordenado Y el conteo de inversiones'''
    total_inversiones = inv_izq + inv_der + inv_mezcla
    
    return arr_ordenado, total_inversiones


def mezclar_y_contar(izq, der):
    """
    Mezcla dos arrays ordenados y cuenta las inversiones entre ellos.
    
    *** ESTA ES LA FUNCIÓN MERGE DE MERGE SORT (CON MODIFICACIÓN) ***
    
    En Merge Sort estándar, esta función se llama "merge" y solo mezcla
    dos arrays ordenados en uno solo ordenado.

    Aquí se hace lo mismo, PERO también se cuentan las inversiones que ocurren
    cuando un elemento del array derecho es menor que elementos del array izquierdo.
    
    Cuando un elemento de la mitad derecha es menor que un elemento de la mitad izquierda,
    se cuentan todas las inversiones que esto genera (todos los elementos restantes de la izquierda).
    
    Args:
        izq: array izquierdo ordenado
        der: array derecho ordenado
        
    Returns:
        tupla (array_mezclado, num_inversiones)
    """
    resultado = []      # array que contendrá la mezcla ordenada (igual que en Merge Sort)
    inversiones = 0     # Contador de inversiones (ESTO es lo que agregamos a Merge Sort)
    i = j = 0           # Índices para recorrer izq y der respectivamente
    
    # ========================================================================
    # FASE 1: MEZCLA PRINCIPAL (idéntica a Merge Sort, con conteo agregado)
    # ========================================================================
    #
    ''' Mezclar mientras ambos arrays tengan elementos
    Este es el bucle principal de la función merge() de Merge Sort'''
    while i < len(izq) and j < len(der):
        # ====================================================================
        # CASO A: Elemento izquierdo es menor o igual (NO hay inversión)
        # ====================================================================
        if izq[i] <= der[j]:
            # En Merge Sort: tomamos el elemento menor (izquierdo)
            resultado.append(izq[i])
            i += 1
            # En mi algoritmo: NO incrementamos inversiones (orden correcto)
            
        # ====================================================================
        # CASO B: Elemento derecho es menor (¡HAY inversión!)
        # ====================================================================
        else:
            # En Merge Sort: tomamos el elemento menor (derecho)
            resultado.append(der[j])
            
            # *** AQUÍ ESTÁ LA MODIFICACIÓN CLAVE ***
            # Si der[j] < izq[i], entonces der[j] también es menor que
            # TODOS los elementos restantes en izq (desde i hasta el final)
            # porque izq ya está ordenado.
            # 
            # Por lo tanto, cada uno de esos elementos forma una inversión con der[j]
            # Número de inversiones = cantidad de elementos restantes en izq
            inversiones += len(izq) - i  # Contamos todas las inversiones
            
            j += 1
    
    # ========================================================================
    # FASE 2: COPIAR ELEMENTOS RESTANTES (igual que Merge Sort)
    # ========================================================================
    ''' Agregar elementos restantes de izq (si los hay)
    En Merge Sort: copiamos lo que queda del array izquierdo
    En nuestro algoritmo: igual, y NO hay inversiones adicionales
    (porque cualquier elemento que quede en izq es mayor que todos en der)'''
    resultado.extend(izq[i:])
    
    # Agregar elementos restantes de der (si los hay)
    # En Merge Sort: copiamos lo que queda del array derecho
    # En nuestro algoritmo: igual, y NO hay inversiones adicionales
    # (porque ya procesamos todos los elementos de izq)
    resultado.extend(der[j:])
    
    # ========================================================================
    #ETAPA FINAL: RETORNAR RESULTADOS
    # ========================================================================
    # Merge Sort retorna: resultado
    # Nuestro algoritmo retorna: (resultado, inversiones)
    return resultado, inversiones


def verificar_inversiones_fuerza_bruta(arr):
    """
    Verifica el conteo de inversiones usando fuerza bruta (O(n²)).
    Nos permite validar el algoritmo divide y vencerás en EL ejercicio.
    
    Args:
        arr: Lista de números a analizar
        
    Returns:
        número de inversiones
    """
    inversiones = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversiones += 1
    return inversiones


def mostrar_ejemplos_inversiones(arr, nombre, max_ejemplos=5):
    """
    Mosdtrar ejemplos de inversiones en un array.
    
    Args:
        arr: array a analizar
        nombre: Nombre descriptivo del caso de prueba
    """
    print(f"\n{'='*70}")
    print(f"Caso de prueba: {nombre}")
    print(f"{'='*70}")
    print(f"array original: {arr}")
    
    # Encontrar algunas inversiones de ejemplo (máximo 5 por efecto para que sea legible)
    inversiones_ejemplo = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversiones_ejemplo.append((i, j, arr[i], arr[j]))
                if len(inversiones_ejemplo) >= max_ejemplos:
                    break
        if len(inversiones_ejemplo) >= 5:
            break
    
    if inversiones_ejemplo:
        print(f"\nEjemplos de inversiones (i, j) donde i < j pero A[i] > A[j]:")
        for i, j, val_i, val_j in inversiones_ejemplo:
            print(f"  - Índices ({i}, {j}): A[{i}] = {val_i} > A[{j}] = {val_j}")
        if len(inversiones_ejemplo) == 5:
            print("  - ...")
    
    # Contar inversiones con divide y vencerás
    arr_copia = arr.copy()
    arr_ordenado, inversiones = contar_inversiones(arr_copia)
    
    # Verificar con fuerza bruta
    inversiones_fb = verificar_inversiones_fuerza_bruta(arr)
    
    print(f"\nResultados:")
    print(f"  - Número total de inversiones (Divide y Vencerás): {inversiones}")
    print(f"  - Verificación (Fuerza Bruta): {inversiones_fb}")
    print(f"  - CORRECTO" if inversiones == inversiones_fb else "  - ERROR: No coinciden")
    print(f"  - array ordenado: {arr_ordenado}")
    print(f"  - Número máximo posible de inversiones: {n * (n - 1) // 2}")
    print(f"  - Porcentaje de inversiones: {100 * inversiones / (n * (n - 1) // 2):.1f}%")


CASOS_DE_PRUEBA = [
    {
        "nombre": "array casi ordenado (pocas inversiones)",
        "array": [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
    },
    {
        "nombre": "array con inversiones moderadas",
        "array": [3, 1, 5, 2, 8, 4, 9, 6, 10, 7]
    },
    {
        "nombre": "array en orden inverso (máximas inversiones)",
        "array": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    },
    {
        "nombre": "Bonus Track !!! array ordenado (0 inversiones)",
        "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
]


def ejecutar_casos_de_prueba(casos=None):
    """
    Ejecuta una lista de casos de prueba parametrizados.
    
    Args:
        casos: Lista de diccionarios con formato:
               [{"nombre": str, "array": list}, ...]
               Si es None, usa CASOS_DE_PRUEBA por defecto
    
    Ejemplo de uso con casos personalizados:
        mis_casos = [
            {"nombre": "Mi caso 1", "array": [5, 4, 3, 2, 1]},
            {"nombre": "Mi caso 2", "array": [1, 3, 2, 4]}
        ]
        ejecutar_casos_de_prueba(mis_casos)
    """
    if casos is None:
        casos = CASOS_DE_PRUEBA
    
    print("\n" + "="*70)
    print("ALGORITMO DIVIDE Y VENCERÁS: CONTEO DE INVERSIONES")
    print("="*70)
    print("\nComplejidad Temporal: O(n log n)")
    print("Complejidad Espacial: O(n)")
    print("\nUna inversión es una pareja (i, j) donde i < j pero A[i] > A[j]")
    
    for caso in casos:
        mostrar_ejemplos_inversiones(caso["array"], caso["nombre"])
    
    print(f"\n{'='*70}")
    print("ANÁLISIS COMPLETO")
    print(f"{'='*70}\n")


def main():
    """
    Función principal que ejecuta los casos de prueba por defecto.
    
    Para ejecutar con casos personalizados, usa ejecutar_casos_de_prueba() directamente.
    """
    ejecutar_casos_de_prueba()


if __name__ == "__main__":
    main()
