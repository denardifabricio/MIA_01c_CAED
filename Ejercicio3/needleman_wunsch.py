

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """
    Implementa el algoritmo de Needleman-Wunsch para alineación global de secuencias.
    
    TEORÍA:
    El algoritmo de Needleman-Wunsch es un método de programacion dinámica que encuentra
    el alineamiento global óptimo entre dos secuencias. Utiliza una matriz de puntuación
    donde cada celda representa el mejor score posible para alinear los prefijos de ambas
    secuencias hasta ese punto. El algoritmo garantiza encontrar el alineamiento óptimo
    mediante la exploración sistematica de todas las posibles alineaciones.
    
    Parámetros:
    -----------
    seq1 : str
        Primera secuencia de nucleótidos
    seq2 : str
        Segunda secuencia de nucleótidos
    match : int
        Puntuación por coincidencia (default: +1)
    mismatch : int
        Puntuación por desajuste (default: -1)
    gap : int
        Penalización por hueco (default: -2)
    
    Retorna:
    --------
    tuple: (matrix, alignment1, alignment2, final_score)
    """
    
    # PASO 1: INICIALIZACION DE LA MATRIZ
    # =====================================
    # Dimenciones: (len(seq1)+1) x (len(seq2)+1)
    # La fila y columna extra (índice 0) representan la secuencia vacia
    n_rows = len(seq1)
    n_cols = len(seq2)
    
    # Crear matriz de programación dinámica
    # Cada celda [i][j] contendrá el score óptimo para alinear seq1[0:i] con seq2[0:j]
    matriz = [[0 for _ in range(n_cols + 1)] for _ in range(n_rows + 1)]
    
    # CONDICIONES DE FRONTERA:
    # La primera fila representa alinear la secuencia vacía con seq2 (solo gaps)
    # La primera columna representa alinear seq1 con la secuencia vacia (solo gaps)
    # Cada gap acumula la penalizacion correspondiente
    for i in range(n_rows + 1):
        matriz[i][0] = i * gap
    for j in range(n_cols + 1):
        matriz[0][j] = j * gap
    
    # PASO 2: LLENADO DE LA MATRIZ (PROGRAMACIÓN DINÁMICA)
    # ======================================================
    # ECUACIÓN DE RECURRENCIA:
    # Para cada celda [i][j], calculamos el score óptimo considerando tres posiblidades:
    #
    # 1. DIAGONAL: Alinear seq1[i-1] con seq2[j-1]
    #    - Si los caracteres coinciden: score[i-1][j-1] + match
    #    - Si no coinciden: score[i-1][j-1] + mismatch
    #
    # 2. ARRIBA: Insertar un gap en seq2 (o eliminar de seq1)
    #    - score[i-1][j] + gap
    #
    # 3. IZQUIERDA: Insertar un gap en seq1 (o eliminar de seq2)
    #    - score[i][j-1] + gap
    #
    # Tomamos el MAXIMO de estas tres opciones, garantizando optimalidad local
    # que se propaga a optimalidad global (principio de Bellman)
    
    for i in range(1, n_rows + 1):
        for j in range(1, n_cols + 1):
            # Calcular puntuación de coincidencia/desajuste (movimiento diagonal)
            if seq1[i-1] == seq2[j-1]:
                diagonal_score = matriz[i-1][j-1] + match
            else:
                diagonal_score = matriz[i-1][j-1] + mismatch
            
            # Calcular puntuaciones con gaps (movimientos vertical y horizontal)
            up_score = matriz[i-1][j] + gap      # Gap en seq2
            left_score = matriz[i][j-1] + gap    # Gap en seq1
            
            # DECISIÓN ÓPTIMA: Tomar el máximo de las tres opciones
            # Esto garantiza que cada celda contiene el mejor score posible
            matriz[i][j] = max(diagonal_score, up_score, left_score)
    
    # PASO 3: TRACEBACK (RECONSTRUCCIÓN DEL ALINEAMIENTO ÓPTIMO)
    # ============================================================
    # TEORÍA DEL TRACEBACK:
    # Una vez construida la matriz, el score óptimo está en matrix[rows][cols].
    # Para recuperar el alineamiento que produjo ese score, recorremos la matriz
    # en sentido inverso (de la esquina inferior derecha hacia el origen).
    #
    # En cada paso, determinamos qué movimiento (diagonal, arriba, izquierda)
    # fue usado para llegar a la celda actual, basandonos en las puntuaciones.
    # Este proceso garantiza recuperar UNO de los alineamientos óptimos
    # (puede haber múltiples alineamientos con el mismo score óptimo).
    #
    # INTERPRETACIÓN DE LOS MOVIMIENTOS:
    # - DIAGONAL: Ambos caracteres se alinean (match o mismatch)
    # - ARRIBA: Insertar gap en seq2 (alinear seq1[i] con '-')
    # - IZQUIERDA: Insertar gap en seq1 (alinear '-' con seq2[j])
    
    alignment1 = []
    alignment2 = []
    
    # Comenzar desde la esquina inferior derecha (alineamiento completo)
    i = n_rows
    j = n_cols
    
    # Continuar hasta llegar al origen [0][0]
    while i > 0 or j > 0:
        # CASOS BORDE: Si estamos en la primera fila o columna
        # Solo podemos movernos en una direccion (forzar gaps)
        
        if j == 0:
            # Primera columna: solo podemos ir hacia arriba (gaps en seq2)
            alignment1.append(seq1[i-1])
            alignment2.append('-')
            i -= 1
        elif i == 0:
            # Primera fila: solo podemos ir hacia la izquierda (gaps en seq1)
            alignment1.append('-')
            alignment2.append(seq2[j-1])
            j -= 1
        else:
            # CASO GENERAL: Recalcular las tres opciones para determinar
            # qué movimiento fue usado para llegar a esta celda
            
            # Calcular score diagonal
            if seq1[i-1] == seq2[j-1]:
                diagonal_score = matriz[i-1][j-1] + match
            else:
                diagonal_score = matriz[i-1][j-1] + mismatch
            
            # Calcular scores con gaps
            up_score = matriz[i-1][j] + gap
            left_score = matriz[i][j-1] + gap
            
            # DECISIÓN: Elegir el camino que produjo el valor actual
            # Priorizamos diagonal > arriba > izquierda en caso de empate
            if matriz[i][j] == diagonal_score:
                # Movimiento diagonal: alinear ambos caracteres
                alignment1.append(seq1[i-1])
                alignment2.append(seq2[j-1])
                i -= 1
                j -= 1
            elif matriz[i][j] == up_score:
                # Movimiento hacia arriba: gap en seq2
                alignment1.append(seq1[i-1])
                alignment2.append('-')
                i -= 1
            else:
                # Movimiento hacia la izquierda: gap en seq1
                alignment1.append('-')
                alignment2.append(seq2[j-1])
                j -= 1
    
    # Los alineamientos se construyeron en orden inverso (de fin a inicio)
    # Invertirlos para obtener el orden correcto
    alignment1 = ''.join(reversed(alignment1))
    alignment2 = ''.join(reversed(alignment2))
    
    # El puntaje final del alineamiento global optimo
    # está en la esquina inferior derecha de la matriz
    puntaje_final = matriz[n_rows][n_cols]
    
    return matriz, alignment1, alignment2, puntaje_final


def print_matrix(matrix, seq1, seq2):
    """
    Imprime la matriz de puntuación de forma legible.
    
    INTERPRETACIÓN DE LA MATRIZ:
    Cada celda [i][j] representa el score óptimo acumulado para alinear
    los primeros i caracteres de seq1 con los primeros j caracteres de seq2.
    La matriz completa muestra el "paisaje" de scores, donde el camino optimo
    desde [0][0] hasta [rows][cols] representa el mejor alineamiento global.
    
    Parámetros:
    -----------
    matrix : list[list[int]]
        Matriz de puntuación
    seq1 : str
        Primera secuencia
    seq2 : str
        Segunda secuencia
    """
    # Encabezado
    print("\nMatriz de Puntuación:")
    print("=" * 60)
    
    # Primera fila con la secuencia 2
    print(f"      -", end="")
    for char in seq2:
        print(f"   {char}", end="")
    print()
    
    # Filas de la matriz
    for i in range(len(matrix)):
        # Etiqueta de fila
        if i == 0:
            print(f"  -", end="")
        else:
            print(f"  {seq1[i-1]}", end="")
        
        # Valores de la fila
        for j in range(len(matrix[i])):
            print(f" {matrix[i][j]:3d}", end="")
        print()
    print("=" * 60)


def print_alignment(alignment1, alignment2, seq1_original, seq2_original):
    """
    Imprime el alineamiento de forma legible, mostrando coincidencias.
    
    VISUALIZACIÓN DEL ALINEAMIENTO:
    El alineamiento muestra cómo se emparejan los caracteres de ambas secuencias:
    - '|' indica coincidencia perfecta (match)
    - '*' indica desajuste (mismatch)
    - ' ' (espacio) indica presencia de un gap
    
    Los gaps representan inserciones o deleciones evolutivas, es decir,
    posiciones donde una secuencia tiene un nucleotido y la otra no.
    
    Parámetros:
    -----------
    alignment1 : str
        Primera secuencia alineada
    alignment2 : str
        Segunda secuencia alineada
    seq1_original : str
        Primera secuencia original
    seq2_original : str
        Segunda secuencia original
    """
    print("\nAlineamiento Óptimo:")
    print("-" * 60)
    
    # Crear línea de coincidencias
    linea_match = []
    for i in range(len(alignment1)):
        if alignment1[i] == alignment2[i]:
            linea_match.append('|')  # Coincidencia
        elif alignment1[i] == '-' or alignment2[i] == '-':
            linea_match.append(' ')  # Gap
        else:
            linea_match.append('*')  # Desajuste
    
    # Imprimir en bloques de 60 caracteres para mejor legibilidad
    tamanio_bloque = 60
    for i in range(0, len(alignment1), tamanio_bloque):
        print(f"Seq1: {alignment1[i:i+tamanio_bloque]}")
        print(f"      {''.join(linea_match[i:i+tamanio_bloque])}")
        print(f"Seq2: {alignment2[i:i+tamanio_bloque]}")
        print()
    
    print("-" * 60)


def analyze_alignment(alignment1, alignment2, match=1, mismatch=-1, gap=-2):
    """
    Analiza y muestra estadísticas del alineamiento.
    
    ANÁLISIS DE CALIDAD DEL ALINEAMIENTO:
    Las estadísticas permiten evaluar la similitud entre las secuencias:
    
    - MATCHES: Posiciones con nucleótidos identicos (evidencia de conservación)
    - MISMATCHES: Posiciones con nucleótidos diferentes (posibles mutaciones)
    - GAPS: Posiciones con inserciones/deleciones (indels)
    - IDENTIDAD: Porcentaje de posiciones idénticas (metrica de similitud)
    
    Un alto porcentaje de identidad sugiere relacion evolutiva cercana o
    función biológica conservada entre las secuencias.
    
    Parámetros:
    -----------
    alignment1 : str
        Primera secuencia alineada
    alignment2 : str
        Segunda secuencia alineada
    match : int
        Puntuación por coincidencia
    mismatch : int
        Puntuación por desajuste
    gap : int
        Penalización por hueco
    """
    num_matches = 0
    num_mismatches = 0
    num_gaps = 0
    
    # Contar cada tipo de evento en el alineamiento
    for i in range(len(alignment1)):
        if alignment1[i] == '-' or alignment2[i] == '-':
            num_gaps += 1              # Gap (insercion/deleción)
        elif alignment1[i] == alignment2[i]:
            num_matches += 1           # Coincidencia (conservacion)
        else:
            num_mismatches += 1        # Desajuste (sustitución)
    
    longitud_total = len(alignment1)
    # Identidad: porcentaje de posiciones con nucleótidos idénticos
    # Es una medida estándar de similitud en bioinformática
    porcentaje_identidad = (num_matches / longitud_total) * 100 if longitud_total > 0 else 0
    
    print("\nEstadísticas del Alineamiento:")
    print("-" * 60)
    print(f"Longitud del alineamiento: {longitud_total}")
    print(f"Coincidencias (matches):   {num_matches} ({num_matches * match:+d} puntos)")
    print(f"Desajustes (mismatches):   {num_mismatches} ({num_mismatches * mismatch:+d} puntos)")
    print(f"Huecos (gaps):             {num_gaps} ({num_gaps * gap:+d} puntos)")
    print(f"Identidad:                 {porcentaje_identidad:.2f}%")
    print("-" * 60)


def process_sequence_pair(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """
    Procesa una pareja de secuencias y muestra todos los resultados.
    
    FLUJO DEL ANÁLISIS:
    1. Ejecutar el algoritmo de Needleman-Wunsch
    2. Mostrar la matriz de programación dinámica construida
    3. Presentar el alineamiento óptimo recuperado
    4. Calcular y reportar estadísticas de calidad
    5. Mostrar el score final (medida de similitud global)
    
    Este proceso completo permite tanto validar la implementación como
    analizar la relación biológica entre las secuencias.
    
    Parámetros:
    -----------
    seq1 : str
        Primera secuencia de nucleótidos
    seq2 : str
        Segunda secuencia de nucleótidos
    match : int
        Puntuación por coincidencia
    mismatch : int
        Puntuación por desajuste
    gap : int
        Penalización por hueco
    """
    print("\n" + "=" * 70)
    print(f"ALINEAMIENTO DE SECUENCIAS")
    print("=" * 70)
    print(f"Secuencia 1: {seq1}")
    print(f"Secuencia 2: {seq2}")
    print(f"\nEsquema de puntuación:")
    print(f"  Match:    {match:+d}")
    print(f"  Mismatch: {mismatch:+d}")
    print(f"  Gap:      {gap:+d}")
    
    # Ejecutar el algoritmo
    matriz, alineamiento1, alineamiento2, puntaje_final = needleman_wunsch(
        seq1, seq2, match, mismatch, gap
    )
    
    # Mostrar resultados
    print_matrix(matriz, seq1, seq2)
    print_alignment(alineamiento1, alineamiento2, seq1, seq2)
    analyze_alignment(alineamiento1, alineamiento2, match, mismatch, gap)
    
    print(f"\n*** PUNTAJE FINAL DEL ALINEAMIENTO: {puntaje_final} ***\n")
    print("=" * 70)


def main():
    """
    Función principal que procesa varias parejas de secuencias.
    
    PROPÓSITO DEL PROGRAMA:
    Demostrar el funcionamiento del algoritmo de Needleman-Wunsch en multiples
    casos de uso, incluyendo secuencias de diferentes longitudes, niveles de
    similitud variados, y diferentes patrones de gaps y mismatches.
    
    ESQUEMA DE PUNTUACIÓN UTILIZADO:
    - Match: +1 (recompensa por nucleótidos idénticos)
    - Mismatch: -1 (penalización por nucleótidos diferentes)
    - Gap: -2 (penalización por inserción/deleción)
    
    Este esquema simple es adecuado para propósitos educativos. En aplicaciones
    reales de bioinformática se utilizan matrices de sustitución más sofisticadas
    (como BLOSUM o PAM para proteínas) que consideran la probabilidad evolutiva
    de cada tipo de mutación.
    """
    print("\n" + "=" * 70)
    print("ALGORITMO DE NEEDLEMAN-WUNSCH")
    print("Alineación Global de Secuncias de Nucleótidos")
    print("=" * 70)
    
    # ================================================================
    # CONJUNTO DE DATOS DE PRUEBA
    # ================================================================
    # Las parejas incluyen diversos escenarios:
    # - Secuencias de longitud similar vs. muy diferentes
    # - Alta similitud vs. baja similitud
    # - Necesidad de gaps vs. principalmente matches/mismatches
    # - Secuencias cortas (validación manual fácil) vs. más largas
    parejas_secuencias = [
        # Ejemplos originales del ejercicio
        ("GATTACA", "GCATGCU"),      # Caso clásico de referencia
        ("ACGT", "ACCT"),             # Secuencias cortas, 1 mismatch
        ("ATGCT", "AGCT"),            # Requiere 1 gap óptimo
        
        # Ejemplos adicionales con características específicas
        ("AGTACGCA", "TATGC"),        # Longitudes muy diferentes (8 vs 5)
        ("CCGTACG", "ACGTACG"),       # Alta similitud (85.7% identidad)
        ("TGCATGC", "TGCGC"),         # Múltiples gaps necesarios
        ("AGGTAB", "GXTXAYB"),        # Con caracteres no-estándar
        ("AATCG", "AACG"),            # Caso simple: 1 gap
        ("GCGTATGC", "GCTATGC"),      # Casi idénticas (87.5% identidad)
        ("TCCAGAGA", "TCGAGAGA")      # Secuencias más largas, 1 mismatch
    ]
    
    # ================================================================
    # PARÁMETROS DEL MODELO DE PUNTUACIÓN
    # ================================================================
    # Estos valores definen el "costo" relativo de diferentes eventos
    # evolutivos y determinan el comportamiento del alineamiento:
    #
    # MATCH (+1): Favorece conservacion de nucleótidos
    # MISMATCH (-1): Penaliza mutaciones puntuales (sustituciones)
    # GAP (-2): Penaliza mas fuertemente inserciones/deleciones
    #
    # La relación gap/mismatch (-2 vs -1) significa que el algoritmo
    # preferirá un mismatch sobre un gap cuando sea posible.
    MATCH = 1
    MISMATCH = -1
    GAP = -2
    
    # Procesar cada pareja
    for i, (seq1, seq2) in enumerate(parejas_secuencias, 1):
        print(f"\n\n{'#' * 70}")
        print(f"PAREJA {i} DE {len(parejas_secuencias)}")
        print(f"{'#' * 70}")
        process_sequence_pair(seq1, seq2, MATCH, MISMATCH, GAP)
    
    print("\n\n" + "=" * 70)
    print("PROCESO COMPLETADO")
    print("=" * 70)


if __name__ == "__main__":
    main()
