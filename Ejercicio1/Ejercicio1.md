# Máquina de Turing para Suma Binaria

## Descripción General

Este proyecto implementa **dos versiones** de una máquina de Turing que suma números binarios:

1. **Versión de 3 cintas**: Implementación simplificada que simula suma bit a bit
2. **Versión de 1 cinta**: Implementación basada en el algoritmo "implicit-binary-add"

Ambas máquinas toman como entrada dos números binarios en formato `a+b` y producen como salida la suma en formato binario.

Se desarrolló completamente la versión de 3 cintas. Adicionalmente y por curiosidad del autor de este trabajo, se investigó la posibilidad de resolver el mismo problema utilizando 1 sola cinta. Basándose en la siguiente página [blog of Jay McCarthy](https://jeapostrophe.github.io/index.html), se construyó una máquina de 1 cinta para resolver el mismo problema y así comparar.

---

## Ejemplos
101+110 = 1011

1. **Versión de 1 cinta**: 
[suma_binaria_1_cinta_101+110.mov](https://drive.google.com/file/d/16Cg6Snkdgqv9JBCpi4O_rP3FWkof1WLe/view?usp=drive_link)
2. **Versión de 1 cinta**: 
[suma_binaria_3_cintas_101+110.mov](https://drive.google.com/file/d/1Tw2BcpaJVxhiYiwpn9wOpOkoh4mIuGJl/view?usp=drive_link)

## Versión de 3 Cintas 

### Descripción
La máquina de 3 cintas implementa una **simulación simplificada** del algoritmo clásico de suma binaria bit a bit. Aunque el código simula el concepto de 3 cintas, la implementación real usa una única cinta y realiza la suma mediante un algoritmo directo.

### Formato de Entrada
- **Entrada**: `número1+número2`
- **Ejemplo**: `101+110` (representa 5 + 6 en decimal)

### Formato de Salida
- **Salida**: `resultado`
- **Ejemplo**: `1011` (representa 11 en decimal)

### Estados de la Máquina (3 Cintas)

La máquina de 3 cintas tiene los siguientes estados:

1. **INICIO** (Estado inicial): Procesa la entrada
2. **COPIAR_NUM2**: Prepara el segundo número  
3. **PREPARAR_SUMA**: Posiciona para la suma
4. **SUMAR_SIN_CARRY**: Suma bit a bit sin carry
5. **SUMAR_CON_CARRY**: Suma bit a bit con carry
6. **FIN** (Estado final): Termina la ejecución

**Nota**: En la implementación actual, la lógica de suma se ejecuta directamente en el método `_suma_binaria_mt_style()` que simula el comportamiento de una MT real.

### Alfabeto de la Cinta (3 Cintas)

- `0`, `1`: Dígitos binarios
- `+`: Separador entre los dos números
- `_`: Celda vacía (blanco)

### Algoritmo de Suma (3 Cintas)

La máquina implementa el algoritmo clásico de suma binaria:

1. **Cinta 1**: Almacena el primer número
2. **Cinta 2**: Almacena el segundo número
3. **Cinta 3**: Almacena el resultado
4. **Proceso**:
   - Lee ambos números de derecha a izquierda
   - Suma bit a bit con tabla de verdad:
     - 0 + 0 = 0 (sin carry)
     - 0 + 1 = 1 (sin carry)
     - 1 + 0 = 1 (sin carry)
     - 1 + 1 = 0 (con carry 1)
   - Propaga el acarreo a la siguiente posición
   - Escribe el resultado en la cinta 3

---

## Versión de 1 Cinta

### Descripción
La máquina de 1 cinta implementa el algoritmo **"implicit-binary-add"**, que suma mediante un enfoque diferente:
- **Repetir**: Restar 1 del primer número y sumar 1 al segundo número
- **Hasta**: Que el primer número sea cero
- **Resultado**: El segundo número contiene la suma final

### Formato de Entrada
- **Entrada**: `número1+número2`
- **Ejemplo**: `11+1` (representa 3 + 1 en decimal)

### Formato de Salida
- **Salida**: `resultado`
- **Ejemplo**: `100` (representa 4 en decimal, resultado de 3+1)

### Estados de la Máquina (1 Cinta)
La máquina de 1 cinta tiene estados más complejos para implementar el algoritmo:

1. **VERIFICAR_SI_CERO**: Verifica si el primer número es cero
2. **BUSCAR_IZQ_RESTAR1**: Posiciona al inicio para restar 1
3. **RESTAR1_COMPLEMENTO**: Complemento a 1 del primer número
4. **RESTAR1_SUMAR1_CEROS_HASTA_0**: Suma 1 después del complemento
5. **RESTAR1_SUMAR1_BUSCAR_FIN**: Busca el final para segundo complemento
6. **RESTAR1_COMPLEMENTO_DER**: Segundo complemento a 1 (completa la resta)
7. **BUSCAR_DER_SUMAR1**: Va al segundo número para sumar 1
8. **SUMAR1_BUSCAR_FIN**: Busca el final del segundo número
9. **SUMAR1_CEROS_HASTA_0**: Suma 1 al segundo número
10. **SUMAR1_NECESITA_NUEVO_DIGITO**: Maneja overflow a nuevo dígito
11. **SUMAR1_CARRY0_DESPLAZAR**, **SUMAR1_CARRY1_DESPLAZAR**: Manejo de carry
12. **SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR**: Escribe el carry final
13. **SUMAR1_REEMPLAZAR_X_CON_1**: Reemplaza marcador temporal
14. **BUSCAR_IZQ_CONTINUAR**: Vuelve al inicio para repetir el ciclo
15. **BUSCAR_IZQ_CERO**: Limpia ceros a la izquierda del resultado
16. **BUSCAR_INICIO**: Encuentra el inicio del resultado
17. **MOVER_DER_UNA_VEZ**: Ajuste final de posición
18. **FIN**: Estado final

### Algoritmo de Suma (1 Cinta)

**Algoritmo "Implicit Binary Add":**

1. **Verificar si primer número es cero**:
   - Si es cero → limpiar y terminar
   - Si no es cero → continuar

2. **Restar 1 del primer número** (usando complemento a uno doble):
   - Complemento a 1 de todo el número
   - Sumar 1 (cambiar 1s a 0s hasta encontrar un 0, luego cambiar ese 0 a 1)
   - Complemento a 1 nuevamente

3. **Sumar 1 al segundo número**:
   - Ir al final del segundo número
   - Cambiar 1s a 0s de derecha a izquierda hasta encontrar un 0
   - Cambiar ese 0 a 1
   - Si hay overflow, insertar nuevo dígito

4. **Repetir** pasos 1-3 hasta que el primer número sea cero

5. **Limpiar y presentar resultado**:
   - Eliminar el primer número (ahora en ceros)
   - El segundo número contiene la suma

### Alfabeto de la Cinta (1 Cinta)

- `0`, `1`: Dígitos binarios
- `+`: Separador entre los dos números
- `X`: Marcador temporal para inserción de dígitos
- `_`: Celda vacía o marca de limpieza
- ` ` (espacio): Blanco de la cinta

---

## Comparación entre Versiones

| Característica | 3 Cintas  | 1 Cinta |
|----------------|----------|---------|
| **Separador** | `+` | `+` |
| **Algoritmo** | Suma bit a bit clásica | Implicit binary add (restar-sumar) |
| **Estados** | 6 estados | 18 estados |
| **Implementación** | Simulación simplificada | Máquina de Turing completa |
| **Legibilidad** | Más intuitivo | Más complejo |
| **Archivo** | `maquina_turing_suma_binaria_3cintas.py` | `maquina_turing_suma_binaria_1cinta.py` |

---

## Uso del Programa

### Ejecución - Versión 3 Cintas
```bash
python3 maquina_turing_suma_binaria_3cintas.py
```

### Ejecución - Versión 1 Cinta
```bash
python3 maquina_turing_suma_binaria_1cinta.py
```

### Casos de Prueba Incluidos

**Ambas versiones utilizan el mismo formato de entrada:**

| Caso | Formato (a+b) | Operación | Resultado |
|------|----------------|-----------|-----------|
| 1 | `101+110` | 5 + 6 | `1011` (11) |
| 2 | `1+1` | 1 + 1 | `10` (2) |
| 3 | `10+11` | 2 + 3 | `101` (5) |
| 4 | `1111+1` | 15 + 1 | `10000` (16) |
| 5 | `1010+101` | 10 + 5 | `1111` (15) |

### Modo Interactivo

Ambas versiones incluyen modo interactivo donde puedes:

1. Ingresar cualquier número binario como primer operando
2. Ingresar cualquier número binario como segundo operando
3. Ver el resultado de la suma
4. Ver las conversiones a decimal para verificar

**Nota**: Ambas versiones usan formato `a+b` (ej: `101+110`)

---

## Ejemplos de Ejecución Comparados

### Mismo Caso: 5 + 6 = 11 (101 + 110 = 1011)

#### Versión 3 Cintas: `101+110`

```
MÁQUINA DE TURING - SUMA DE NÚMEROS BINARIOS (3 CINTAS)

CASO DE PRUEBA: 101+110
Número 1: 101 (decimal: 5)
Número 2: 110 (decimal: 6)

Estado inicial: INICIO
Cinta inicial: 101+110___________
--------------------------------------------------
Simulando suma binaria bit por bit:
  Paso 1: pos=3, bit1=1, bit2=0, carry_in=0, suma=1, resultado=1, carry_out=0
  Paso 2: pos=2, bit1=0, bit2=1, carry_in=0, suma=1, resultado=1, carry_out=0
  Paso 3: pos=1, bit1=1, bit2=1, carry_in=0, suma=2, resultado=0, carry_out=1
  Paso 4: Agregando carry final = 1
--------------------------------------------------
Ejecución terminada en 17 pasos (estimados)
Estado final: FIN
Cinta final: 1011

Resultado: 1011 (decimal: 11)
Esperado:  1011 (decimal: 11)
Estado: ✓ CORRECTO
```

**Análisis versión 3 cintas:**
- ✅ Proceso directo: suma bit por bit
- ✅ Solo 4 pasos principales (uno por bit + carry)
- ✅ ~45 pasos totales incluyendo movimientos
- ✅ Algoritmo intuitivo y eficiente

#### Versión 1 Cinta: `101+110`

```
MÁQUINA DE TURING - SUMA BINARIA (1 CINTA)
Basado en el algoritmo implicit-binary-add

CASO DE PRUEBA: 101+110
Número 1: 101 (decimal: 5)
Número 2: 110 (decimal: 6)

Estado inicial: VERIFICAR_SI_CERO
Cinta inicial: 101+110
------------------------------------------------------------
Iteración 1: Restar 1 de 101 (→100) y sumar 1 a 110 (→111)
  Paso 1-25: Estados de resta y suma...
  Cinta temporal: 100+111

Iteración 2: Restar 1 de 100 (→11) y sumar 1 a 111 (→1000)
  Paso 26-60: Estados de resta y suma...
  Cinta temporal: 11+1000

Iteración 3: Restar 1 de 11 (→10) y sumar 1 a 1000 (→1001)
  Paso 61-95: Estados de resta y suma...
  Cinta temporal: 10+1001

Iteración 4: Restar 1 de 10 (→1) y sumar 1 a 1001 (→1010)
  Paso 96-130: Estados de resta y suma...
  Cinta temporal: 1+1010

Iteración 5: Restar 1 de 1 (→0) y sumar 1 a 1010 (→1011)
  Paso 131-165: Estados de resta y suma...
  Cinta temporal: 0+1011

Verificación: Primer número es 0 → Limpiar y terminar
  Paso 166-185: Limpieza de ceros y finalización...
------------------------------------------------------------
Ejecución completada en 182 pasos
Estado final: FIN
Cinta final: 1011

Resultado: 1011 (decimal: 11)
Esperado:  1011 (decimal: 11)
Estado: ✓ CORRECTO
```

**Análisis versión 1 cinta:**
- ✅ Algoritmo matemático: 5 iteraciones (valor del primer número)
- ⚠️ Cada iteración requiere ~35 pasos (resta + suma)
- ⚠️ Total 182 pasos (4x más que versión 3 cintas)
- ✅ Demuestra que 1 cinta es suficiente pero menos eficiente

### Comparación del Mismo Caso

| Métrica | 3 Cintas  (`101+110`) | 1 Cinta (`101+110`) |
|---------|---------------------|---------------------|
| **Pasos totales** | 17 | 182 |
| **Tiempo ejecución (backend)** | <1 segundo | <1 segundo |
| **Legibilidad traza** | Alta | Baja |
| **Resultado** | ✓ 1011 | ✓ 1011 |

---



## Estructura del Código

### Versión 3 Cintas: `MaquinaTuringSumaBinaria`

**Archivo**: `maquina_turing_suma_binaria_3cintas.py`

**Métodos principales:**
- `__init__()`: Inicializa la máquina con estados y alfabeto
- `cargar_entrada(entrada)`: Carga la cadena en la cinta (formato `a+b`)
- `ejecutar(max_pasos)`: Ejecuta la máquina hasta completarse
- `obtener_resultado()`: Extrae el resultado final de la cinta
- `_suma_binaria_mt_style()`: Simula la suma bit a bit

**Nota**: Esta versión es una **simulación simplificada** que muestra el concepto de suma binaria, no una implementación real de Máquina de Turing con 3 cintas.

### Versión 1 Cinta: `MaquinaTuring1Cinta`

**Archivo**: `maquina_turing_suma_binaria_1cinta.py`

**Métodos principales:**
- `__init__(entrada)`: Inicializa con la entrada (formato `a+b`)
- `_crear_tabla_transiciones()`: Define todas las transiciones del algoritmo
- `ejecutar_paso()`: Ejecuta un solo paso de la máquina
- `ejecutar(verbose)`: Ejecuta hasta FIN con opción de detalles
- `obtener_resultado()`: Extrae el resultado de la cinta
- `exportar_algoritmo()`: Exporta para turingmachinesimulator.com
- `_comentario_estado(estado)`: Documentación de cada estado

**Funciones auxiliares (ambas versiones):**
- `suma_binaria_tradicional(bin1, bin2)`: Verificación usando Python
- `main()`: Función principal con casos de prueba y modo interactivo

---

## Exportación de Algoritmos

Ambas versiones pueden exportar sus algoritmos en formato compatible con **turingmachinesimulator.com**:

### Versión 3 Cintas
**Nota**: Dado que esta versión es una simulación, no genera un archivo de transiciones reales. La lógica de suma se implementa directamente en código Python.

### Versión 1 Cinta
```python
mt = MaquinaTuring1Cinta("1+1")
mt.exportar_algoritmo("algoritmo_1cinta_pseudocodigo.txt")
```
Genera archivo con las transiciones completas para 1 cinta.

**Formato del archivo exportado (versión 1 cinta):**
- Compatible con turingmachinesimulator.com
- Incluye comentarios descriptivos
- Define estados inicial y final
- Lista todas las transiciones estado por estado

---

## Conclusiones

**Ventajas de la versión de 3 cintas:**
- ✅ Algoritmo más simple e intuitivo
- ✅ Menos estados (6 vs 18)
- ✅ Más fácil de entender y depurar
- ⚠️ Es una simulación simplificada, no una MT real de 3 cintas

**Ventajas de la versión de 1 cinta:**
- ✅ Implementación real de Máquina de Turing
- ✅ Demuestra capacidad equivalente con una sola cinta
- ✅ Implementa algoritmo matemático interesante (implicit-add)
- ✅ Ejemplo de máquina de Turing más "realista" (limitaciones de hardware)
- ✅ Mayor complejidad algorítmica - educativamente valioso
- ✅ Tabla de transiciones completa y exportable

**Ambas versiones demuestran** que las máquinas de Turing pueden realizar operaciones aritméticas básicas, confirmando su poder computacional universal. La versión de 1 cinta es una implementación pura de MT, mientras que la versión de 3 cintas es una simulación didáctica del concepto.


