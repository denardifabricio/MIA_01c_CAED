#!/usr/bin/env python3
"""
Máquina de Turing de 1 Cinta para Suma Binaria
==============================================

Implementación basada en el algoritmo implicit-binary-add.
Suma dos números binarios en formato a+b mediante el algoritmo:
- Repetir: restar 1 del primer número y sumar 1 al segundo
- Hasta que el primer número sea cero
- El segundo número contendrá la suma

Ejemplo: '11+1' => '0+100' => resultado: '100'

El algoritmo:
1. Verificar si el primer número es cero
2. Si no es cero, restar 1 del primer número
3. Sumar 1 al segundo número
4. Repetir hasta que el primer número sea cero
5. Limpiar y presentar el resultado
"""

class MaquinaTuring1Cinta:
    def __init__(self, entrada):
        """
        Inicializa la máquina de Turing con la entrada proporcionada
        
        Args:
            entrada: string en formato 'a+b' donde a y b son números binarios
        """
        self.cinta = list(' ' + entrada + ' ' * 20)  # Agregar espacios al inicio y final
        self.cabezal = 1  # Empezar después del espacio inicial
        self.estado = 'VERIFICAR_SI_CERO'
        self.entrada_original = entrada
        self.pasos = 0
        self.max_pasos = 10000
        
        # Tabla de transiciones según el pseudocódigo
        self.transiciones = self._crear_tabla_transiciones()
    
    def _crear_tabla_transiciones(self):
        """
        Crea la tabla de transiciones basada en implicit-binary-add
        
        Estructura: {estado: {símbolo: (nuevo_estado, nuevo_símbolo, dirección)}}
        
        El algoritmo verifica si el primer número es cero. Si no lo es,
        resta 1 del primer número y suma 1 al segundo, repitiendo hasta
        que el primer número sea cero.
        
        La resta se implementa usando complemento a uno doble:
        1. Complemento a uno de todo el número
        2. Sumar 1 (encontrar el 0 más a la derecha y cambiar a 1, los 1s previos a 0s)
        3. Complemento a uno nuevamente
        """
        return {
            # VERIFICAR_SI_CERO: Verificar si el primer número es cero (todos sus dígitos son 0)
            'VERIFICAR_SI_CERO': {
                '0': ('VERIFICAR_SI_CERO', '0', 'R'),
                '1': ('BUSCAR_IZQ_RESTAR1', '1', 'L'),
                '+': ('BUSCAR_IZQ_CERO', '_', 'L'),
            },
            
            # BUSCAR_IZQ_RESTAR1: Ir al inicio (blank) antes del primer número
            'BUSCAR_IZQ_RESTAR1': {
                '0': ('BUSCAR_IZQ_RESTAR1', '0', 'L'),
                '1': ('BUSCAR_IZQ_RESTAR1', '1', 'L'),
                ' ': ('RESTAR1_COMPLEMENTO', ' ', 'R'),
            },
            
            # RESTAR1_COMPLEMENTO: Complemento a 1 desde la izquierda hasta encontrar +
            'RESTAR1_COMPLEMENTO': {
                '0': ('RESTAR1_COMPLEMENTO', '1', 'R'),
                '1': ('RESTAR1_COMPLEMENTO', '0', 'R'),
                '+': ('RESTAR1_SUMAR1_CEROS_HASTA_0', '+', 'L'),
            },
            
            # RESTAR1_SUMAR1_CEROS_HASTA_0: Sumar 1 (cambiar 1s a 0s hasta encontrar un 0)
            'RESTAR1_SUMAR1_CEROS_HASTA_0': {
                '1': ('RESTAR1_SUMAR1_CEROS_HASTA_0', '0', 'L'),
                '0': ('RESTAR1_SUMAR1_BUSCAR_FIN', '1', 'R'),
            },
            
            # RESTAR1_SUMAR1_BUSCAR_FIN: Ir hasta el + para hacer el segundo complemento
            'RESTAR1_SUMAR1_BUSCAR_FIN': {
                '0': ('RESTAR1_SUMAR1_BUSCAR_FIN', '0', 'R'),
                '1': ('RESTAR1_SUMAR1_BUSCAR_FIN', '1', 'R'),
                '+': ('RESTAR1_COMPLEMENTO_DER', '+', 'L'),
            },
            
            # RESTAR1_COMPLEMENTO_DER: Complemento a 1 desde la derecha hasta el inicio
            'RESTAR1_COMPLEMENTO_DER': {
                '0': ('RESTAR1_COMPLEMENTO_DER', '1', 'L'),
                '1': ('RESTAR1_COMPLEMENTO_DER', '0', 'L'),
                ' ': ('BUSCAR_DER_SUMAR1', ' ', 'R'),
            },
            
            # BUSCAR_DER_SUMAR1: Ir al segundo número (después del +)
            'BUSCAR_DER_SUMAR1': {
                '0': ('BUSCAR_DER_SUMAR1', '0', 'R'),
                '1': ('BUSCAR_DER_SUMAR1', '1', 'R'),
                '+': ('SUMAR1_BUSCAR_FIN', '+', 'R'),
            },
            
            # SUMAR1_BUSCAR_FIN: Ir al final del segundo número
            'SUMAR1_BUSCAR_FIN': {
                '0': ('SUMAR1_BUSCAR_FIN', '0', 'R'),
                '1': ('SUMAR1_BUSCAR_FIN', '1', 'R'),
                ' ': ('SUMAR1_CEROS_HASTA_0', ' ', 'L'),
            },
            
            # SUMAR1_CEROS_HASTA_0: Sumar 1 al segundo número (cambiar 1s a 0s hasta encontrar 0 o llegar a +)
            'SUMAR1_CEROS_HASTA_0': {
                '1': ('SUMAR1_CEROS_HASTA_0', '0', 'L'),
                '0': ('BUSCAR_IZQ_CONTINUAR', '1', 'L'),
                '+': ('SUMAR1_NECESITA_NUEVO_DIGITO', '+', 'R'),  # Llegamos al + con carry: necesitamos nuevo dígito
            },
            
            # SUMAR1_NECESITA_NUEVO_DIGITO: Insertar un '1' justo después del +
            'SUMAR1_NECESITA_NUEVO_DIGITO': {
                '0': ('SUMAR1_CARRY0_DESPLAZAR', 'X', 'R'),  # Marcar y recordar que llevamos un 0
                '1': ('SUMAR1_CARRY1_DESPLAZAR', 'X', 'R'),  # Marcar y recordar que llevamos un 1
                ' ': ('SUMAR1_SOLO_ESCRIBIR_UNO', '1', 'L'),   # Segundo número vacío, solo escribir 1
            },
            
            # SUMAR1_SOLO_ESCRIBIR_UNO: El segundo número estaba vacío, ya escribimos 1
            'SUMAR1_SOLO_ESCRIBIR_UNO': {
                '+': ('BUSCAR_IZQ_CONTINUAR', '+', 'L'),
            },
            
            # SUMAR1_CARRY0_DESPLAZAR: Llevamos un 0, leer siguiente y desplazar
            'SUMAR1_CARRY0_DESPLAZAR': {
                '0': ('SUMAR1_CARRY0_DESPLAZAR', '0', 'R'),
                '1': ('SUMAR1_CARRY1_DESPLAZAR', '1', 'R'),
                ' ': ('SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR', '0', 'L'),
            },
            
            # SUMAR1_CARRY1_DESPLAZAR: Llevamos un 1, leer siguiente y desplazar
            'SUMAR1_CARRY1_DESPLAZAR': {
                '0': ('SUMAR1_CARRY0_DESPLAZAR', '0', 'R'),
                '1': ('SUMAR1_CARRY1_DESPLAZAR', '1', 'R'),
                ' ': ('SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR', '1', 'L'),
            },
            
            # SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR: Escribir el último dígito y volver
            'SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR': {
                '0': ('SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR', '0', 'L'),
                '1': ('SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR', '1', 'L'),
                'X': ('SUMAR1_REEMPLAZAR_X_CON_1', '1', 'L'),  # Reemplazar la marca X con 1
            },
            
            # SUMAR1_REEMPLAZAR_X_CON_1: Ya reemplazamos X, continuar
            'SUMAR1_REEMPLAZAR_X_CON_1': {
                '+': ('BUSCAR_IZQ_CONTINUAR', '+', 'L'),
            },
            
            # BUSCAR_IZQ_CONTINUAR: Volver al inicio del primer número para repetir
            'BUSCAR_IZQ_CONTINUAR': {
                '0': ('BUSCAR_IZQ_CONTINUAR', '0', 'L'),
                '1': ('BUSCAR_IZQ_CONTINUAR', '1', 'L'),
                '+': ('BUSCAR_IZQ_CONTINUAR', '+', 'L'),
                ' ': ('VERIFICAR_SI_CERO', ' ', 'R'),
            },
            
            # BUSCAR_IZQ_CERO: Reemplazar ceros a la izquierda con _
            'BUSCAR_IZQ_CERO': {
                '0': ('BUSCAR_IZQ_CERO', '_', 'L'),
                ' ': ('BUSCAR_INICIO', ' ', 'R'),
            },
            
            # BUSCAR_INICIO: Encontrar el inicio del resultado (saltar _)
            'BUSCAR_INICIO': {
                '_': ('BUSCAR_INICIO', '_', 'R'),
                '0': ('MOVER_DER_UNA_VEZ', '0', 'L'),
                '1': ('MOVER_DER_UNA_VEZ', '1', 'L'),
            },
            
            # MOVER_DER_UNA_VEZ: Mover a la derecha y terminar
            'MOVER_DER_UNA_VEZ': {
                '_': ('FIN', ' ', 'R'),
            },
            
            # FIN: Estado final
            'FIN': {},
        }
    
    def ejecutar_paso(self):
        """Ejecuta un paso de la máquina de Turing"""
        if self.estado == 'FIN':
            return False
        
        simbolo_actual = self.cinta[self.cabezal]
        
        # Buscar transición
        if self.estado not in self.transiciones:
            print(f"Error: Estado '{self.estado}' no definido")
            return False
        
        if simbolo_actual not in self.transiciones[self.estado]:
            print(f"Error: No hay transición para estado '{self.estado}' y símbolo '{simbolo_actual}'")
            print(f"Transiciones disponibles: {list(self.transiciones[self.estado].keys())}")
            return False
        
        nuevo_estado, nuevo_simbolo, direccion = self.transiciones[self.estado][simbolo_actual]
        
        # Ejecutar transición
        self.cinta[self.cabezal] = nuevo_simbolo
        self.estado = nuevo_estado
        
        if direccion == 'R':
            self.cabezal += 1
        elif direccion == 'L':
            self.cabezal -= 1
        
        # Asegurar que no salimos de la cinta
        if self.cabezal < 0:
            self.cinta.insert(0, ' ')
            self.cabezal = 0
        elif self.cabezal >= len(self.cinta):
            self.cinta.append(' ')
        
        self.pasos += 1
        return True
    
    def ejecutar(self, verbose=True):
        """
        Ejecuta la máquina de Turing hasta terminar
        
        Args:
            verbose: si True, imprime información detallada
        """
        if verbose:
            print(f"Entrada: '{self.entrada_original}'")
            print(f"Estado inicial: {self.estado}")
            print(f"Cinta inicial: {''.join(self.cinta).strip()}")
            print("-" * 60)
        
        paso = 0
        while self.estado != 'FIN' and self.pasos < self.max_pasos:
            simbolo_actual = self.cinta[self.cabezal]
            estado_anterior = self.estado
            
            if not self.ejecutar_paso():
                break
            
            paso += 1
            
            # Imprimir cada 10 pasos o en estados importantes
            if verbose and (paso <= 20 or paso % 50 == 0 or estado_anterior != self.estado):
                cinta_str = ''.join(self.cinta).strip()
                # Marcar posición del cabezal
                if self.cabezal < len(self.cinta):
                    cinta_visual = list(cinta_str)
                    pos_visual = self.cabezal - 1  # Ajustar por el espacio inicial
                    if 0 <= pos_visual < len(cinta_visual):
                        if paso <= 20:
                            print(f"Paso {paso}: Estado={estado_anterior}->{self.estado}, "
                                  f"Pos={self.cabezal}, Símbolo='{simbolo_actual}', "
                                  f"Cinta: {cinta_str}")
        
        if verbose:
            print("-" * 60)
            print(f"Ejecución completada en {self.pasos} pasos")
            print(f"Estado final: {self.estado}")
        
        resultado = self.obtener_resultado()
        if verbose:
            print(f"Cinta final: {resultado}")
        
        return resultado
    
    def obtener_resultado(self):
        """Obtiene el resultado de la cinta"""
        cinta_str = ''.join(self.cinta).strip()
        return cinta_str
    
    def exportar_algoritmo(self, nombre_archivo="suma_binaria_1cinta.txt"):
        """
        Exporta el algoritmo en formato para turingmachinesimulator.com
        Formato:
        estado,simbolo_leido
        nuevo_estado,simbolo_escrito,direccion
        """
        import os
        
        # Obtener la ruta del directorio donde está este script
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(dir_actual, nombre_archivo)
        
        lineas = []
        
        # Encabezado con comentarios
        lineas.append("// Entrada: a+b donde a y b son números binarios")
        lineas.append("// Salida: resultado de a+b en binario")
        lineas.append("// Ejemplo: 11+1 => 100")
        lineas.append("//")
        lineas.append("// Algoritmo de Suma Binaria Implícita")
        lineas.append("// para Simulador de Máquina de Turing")
        lineas.append("// turingmachinesimulator.com")
        lineas.append("//")
        lineas.append("// Algoritmo: Restar repetidamente 1 del primer número")
        lineas.append("// y sumar 1 al segundo número hasta que el primer número sea cero")
        lineas.append("")
        lineas.append("name: Suma Binaria (Algoritmo Implícito)")
        lineas.append("init: VERIFICAR_SI_CERO")
        lineas.append("accept: FIN")
        lineas.append("")
        
        # Generar transiciones en formato correcto
        # Formato: estado,simbolo_leido
        #          nuevo_estado,simbolo_escrito,direccion
        
        # Ordenar estados para mejor legibilidad
        estados_orden = ['VERIFICAR_SI_CERO', 'BUSCAR_IZQ_RESTAR1', 'RESTAR1_COMPLEMENTO', 
                        'RESTAR1_SUMAR1_CEROS_HASTA_0', 'RESTAR1_SUMAR1_BUSCAR_FIN', 'RESTAR1_COMPLEMENTO_DER',
                        'BUSCAR_DER_SUMAR1', 'SUMAR1_BUSCAR_FIN', 'SUMAR1_CEROS_HASTA_0',
                        'SUMAR1_NECESITA_NUEVO_DIGITO', 'SUMAR1_SOLO_ESCRIBIR_UNO', 
                        'SUMAR1_CARRY0_DESPLAZAR', 'SUMAR1_CARRY1_DESPLAZAR',
                        'SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR', 'SUMAR1_REEMPLAZAR_X_CON_1',
                        'BUSCAR_IZQ_CONTINUAR', 'BUSCAR_IZQ_CERO', 'BUSCAR_INICIO', 
                        'MOVER_DER_UNA_VEZ', 'FIN']
        
        for estado in estados_orden:
            if estado not in self.transiciones:
                continue
            
            trans = self.transiciones[estado]
            if not trans:
                continue
            
            # Agregar comentario para el estado
            comentario = self._comentario_estado(estado)
            if comentario:
                lineas.append(f"// {comentario}")
            
            # Generar cada transición
            for simbolo, (nuevo_estado, nuevo_simbolo, direccion) in sorted(trans.items()):
                # Formatear dirección: L = <, R = >, - = quedarse
                dir_simbolo = '<' if direccion == 'L' else ('>' if direccion == 'R' else '-')
                
                # Formatear estado y símbolo
                estado_fmt = estado
                simbolo_fmt = '_' if simbolo == ' ' else simbolo
                nuevo_simbolo_fmt = '_' if nuevo_simbolo == ' ' else nuevo_simbolo
                
                lineas.append(f"{estado_fmt},{simbolo_fmt}")
                lineas.append(f"{nuevo_estado},{nuevo_simbolo_fmt},{dir_simbolo}")
                lineas.append("")
        
        # Escribir archivo
        try:
            with open(ruta_completa, 'w', encoding='utf-8') as archivo:
                archivo.write('\n'.join(lineas))
            
            print(f"\n✓ Archivo '{nombre_archivo}' generado exitosamente")
            print(f"  Ruta: {ruta_completa}")
            print(f"  Formato: Compatible con turingmachinesimulator.com")
            print(f"  Estados: {len(self.transiciones)}")
            print(f"  Transiciones: {sum(len(t) for t in self.transiciones.values())}")
            return True
        except Exception as e:
            print(f"\n✗ Error al generar el archivo: {e}")
            return False
    
    def _comentario_estado(self, estado):
        """Devuelve un comentario descriptivo para cada estado"""
        comentarios = {
            'VERIFICAR_SI_CERO': "Verificar si el primer número es cero",
            'BUSCAR_IZQ_RESTAR1': "Ir al inicio del primer número para restar 1",
            'RESTAR1_COMPLEMENTO': "Complemento a 1 hasta encontrar +",
            'RESTAR1_SUMAR1_CEROS_HASTA_0': "Sumar 1 después del complemento (encontrar 0 desde derecha)",
            'RESTAR1_SUMAR1_BUSCAR_FIN': "Encontrar el final del primer número",
            'RESTAR1_COMPLEMENTO_DER': "Complemento a 1 desde derecha (completar resta)",
            'BUSCAR_DER_SUMAR1': "Ir al segundo número para sumar 1",
            'SUMAR1_BUSCAR_FIN': "Encontrar el final del segundo número",
            'SUMAR1_CEROS_HASTA_0': "Sumar 1 al segundo número (propagar acarreo)",
            'SUMAR1_NECESITA_NUEVO_DIGITO': "Manejar desbordamiento de acarreo a nuevo dígito",
            'SUMAR1_SOLO_ESCRIBIR_UNO': "Escribir 1 cuando el segundo número estaba vacío",
            'SUMAR1_CARRY0_DESPLAZAR': "Desplazar llevando un 0",
            'SUMAR1_CARRY1_DESPLAZAR': "Desplazar llevando un 1",
            'SUMAR1_ESCRIBIR_ACARREO_Y_RETORNAR': "Escribir último dígito acarreado y retornar",
            'SUMAR1_REEMPLAZAR_X_CON_1': "Reemplazar marcador X con 1",
            'BUSCAR_IZQ_CONTINUAR': "Retornar al inicio para repetir el ciclo",
            'BUSCAR_IZQ_CERO': "Limpiar ceros a la izquierda del resultado",
            'BUSCAR_INICIO': "Encontrar el inicio del resultado",
            'MOVER_DER_UNA_VEZ': "Mover a la derecha una vez y terminar",
            'FIN': "Estado final - terminado",
        }
        return comentarios.get(estado, "")


def suma_binaria_tradicional(bin1, bin2):
    """Función auxiliar para verificar el resultado"""
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    suma = num1 + num2
    return bin(suma)[2:]


def main():
    """Función principal"""
    print("=" * 70)
    print("MÁQUINA DE TURING - SUMA BINARIA (1 CINTA)")
    print("Basado en el pseudocódigo proporcionado")
    print("=" * 70)
    
    # Casos de prueba
    casos_prueba = [
        "11+1",        # 3 + 1 = 4 => '100'
        "1011+11001",  # 11 + 25 = 36 => '100100'
        "101+110",     # 5 + 6 = 11 => '1011'
        "1+1",         # 1 + 1 = 2 => '10'
        "10+11",       # 2 + 3 = 5 => '101'
    ]
    
    for i, entrada in enumerate(casos_prueba, 1):
        print(f"\n{'='*70}")
        print(f"CASO DE PRUEBA {i}:")
        print(f"{'='*70}")
        
        # Separar los números
        nums = entrada.split('+')
        if len(nums) == 2:
            num1, num2 = nums
            dec1 = int(num1, 2)
            dec2 = int(num2, 2)
            print(f"Entrada: {entrada}")
            print(f"  {num1} (decimal: {dec1})")
            print(f"  {num2} (decimal: {dec2})")
        
        # Ejecutar máquina de Turing
        mt = MaquinaTuring1Cinta(entrada)
        resultado = mt.ejecutar(verbose=(i <= 2))  # Detalles solo para los primeros 2 casos
        
        # Verificar resultado
        if len(nums) == 2:
            # Limpiar el resultado: remover espacios, +, y _
            resultado_limpio = resultado.replace(' ', '').replace('+', '').replace('_', '')
            # El resultado debe estar después de limpiar
            resultado_suma = resultado_limpio.strip()
            
            resultado_esperado = suma_binaria_tradicional(num1, num2)
            dec_resultado = int(resultado_suma, 2) if resultado_suma and resultado_suma != '' and resultado_suma.replace('0','').replace('1','') == '' else 0
            
            print(f"\nResultado: {resultado_suma} (decimal: {dec_resultado})")
            print(f"Esperado:  {resultado_esperado} (decimal: {dec1 + dec2})")
            print(f"Estado: {'✓ CORRECTO' if resultado_suma == resultado_esperado else '✗ ERROR'}")
    
    # Exportar algoritmo
    print(f"\n{'='*70}")
    print("EXPORTANDO ALGORITMO")
    print(f"{'='*70}")
    mt = MaquinaTuring1Cinta("1+1")
    mt.exportar_algoritmo()
    
    # Modo interactivo
    print(f"\n{'='*70}")
    print("MODO INTERACTIVO")
    print(f"{'='*70}")
    print("Ingresa dos números binarios en formato a+b")
    print("(o presiona Enter para salir)")
    
    while True:
        try:
            entrada = input("\nEntrada (formato a+b): ").strip()
            if not entrada:
                break
            
            if '+' not in entrada:
                print("Error: Usa el formato a+b (ej: 101+110)")
                continue
            
            nums = entrada.split('+')
            if len(nums) != 2:
                print("Error: Usa el formato a+b con exactamente un símbolo +")
                continue
            
            if not all(c in '01' for c in nums[0]) or not all(c in '01' for c in nums[1]):
                print("Error: Solo se permiten dígitos 0 y 1")
                continue
            
            print(f"\nEjecutando máquina de Turing...")
            mt = MaquinaTuring1Cinta(entrada)
            resultado = mt.ejecutar(verbose=False)
            
            # Extraer resultado: limpiar espacios, +, y _
            resultado_suma = resultado.replace(' ', '').replace('+', '').replace('_', '').strip()
            
            dec1 = int(nums[0], 2)
            dec2 = int(nums[1], 2)
            dec_resultado = int(resultado_suma, 2) if resultado_suma and resultado_suma.replace('0','').replace('1','') == '' else 0
            
            print(f"\n{nums[0]} ({dec1}) + {nums[1]} ({dec2}) = {resultado_suma} ({dec_resultado})")
            print(f"Cinta final completa: {resultado}")
            
        except KeyboardInterrupt:
            print("\n¡Gracias por usar el simulador!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
