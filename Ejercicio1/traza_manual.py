#!/usr/bin/env python3
"""
Trazado manual del algoritmo para 1+1
"""

# Entrada: " 1+1 "
# Estado: check-if-zero, Pos=1 (apuntando a '1')

# Paso 1: check-if-zero
# Lee '1' -> va a seek-left&sub1, deja '1', L
# Cinta: " 1+1 ", Pos=0 (apuntando a ' ')

# Paso 2: seek-left&sub1
# Lee ' ' -> va a sub1:ones-complement, deja ' ', R
# Cinta: " 1+1 ", Pos=1 (apuntando a '1')

# Paso 3: sub1:ones-complement
# Lee '1' -> va a sub1:ones-complement, escribe '0', R
# Cinta: " 0+1 ", Pos=2 (apuntando a '+')

# Paso 4: sub1:ones-complement
# Lee '+' -> va a sub1:add1:zero-until-0, deja '+', L
# Cinta: " 0+1 ", Pos=1 (apuntando a '0')

# Paso 5: sub1:add1:zero-until-0
# Lee '0' -> va a sub1:add1:find-end, escribe '1', R
# Cinta: " 1+1 ", Pos=2 (apuntando a '+')

# Paso 6: sub1:add1:find-end
# Lee '+' -> va a sub1:ones-complementR, deja '+', L
# Cinta: " 1+1 ", Pos=1 (apuntando a '1')

# Paso 7: sub1:ones-complementR
# Lee '1' -> va a sub1:ones-complementR, escribe '0', L
# Cinta: " 0+1 ", Pos=0 (apuntando a ' ')

# Paso 8: sub1:ones-complementR
# Lee ' ' -> va a seek-right&add1, deja ' ', R
# Cinta: " 0+1 ", Pos=1 (apuntando a '0')

# Ahora el primer número es '0' (hemos restado 1 a '1', obteniendo '0')

# Paso 9: seek-right&add1
# Lee '0' -> va a seek-right&add1, deja '0', R
# Cinta: " 0+1 ", Pos=2 (apuntando a '+')

# Paso 10: seek-right&add1
# Lee '+' -> va a add1:find-end, deja '+', R
# Cinta: " 0+1 ", Pos=3 (apuntando a '1')

# Paso 11: add1:find-end
# Lee '1' -> va a add1:find-end, deja '1', R
# Cinta: " 0+1 ", Pos=4 (apuntando a ' ')

# Paso 12: add1:find-end
# Lee ' ' -> va a add1:zero-until-0, deja ' ', L
# Cinta: " 0+1 ", Pos=3 (apuntando a '1')

# Paso 13: add1:zero-until-0
# Lee '1' -> va a add1:zero-until-0, escribe '0', L
# Cinta: " 0+0 ", Pos=2 (apuntando a '+')

# Paso 14: add1:zero-until-0
# Lee '+' -> va a seek-left&continue, escribe '1', L
# Cinta: " 0+10 ", Pos=1 (apuntando a '0')

# ERROR: Ahora el segundo número es '10' pero debería estar a la derecha del '+'
# El problema es que estamos escribiendo el '1' sobre el '+'!

print("¡Encontré el error!")
print("El estado add1:zero-until-0 no debería escribir sobre el '+'")
print("Cuando llega al '+', significa que necesitamos agregar un dígito nuevo a la izquierda")
print("Pero esto es difícil en una máquina de Turing...")
print()
print("El problema es que en el algoritmo de Racket, cuando sumamos 1 y llegamos al '+',")
print("significa que hay un carry que se propaga más allá del número.")
print("En Racket, esto se maneja expandiendo el número hacia la izquierda.")
print()
print("Para una máquina de Turing de 1 cinta, necesitamos:")
print("1. Detectar cuando hay carry al inicio del segundo número")
print("2. Mover todo el segundo número a la derecha")
print("3. Insertar un '1' al inicio")
