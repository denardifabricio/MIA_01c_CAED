def turing_sum_binarios(cinta_inicial: str):
    """
    Simula una máquina de Turing de una sola cinta
    que suma dos números binarios separados por '#'.
    Ejemplo: 1011#110 -> 10001
    """
    # Separar los números binarios
    if "#" not in cinta_inicial:
        raise ValueError("La cinta debe contener un separador '#'")

    a, b = cinta_inicial.strip().split("#")

    # Convertirlos en listas (de derecha a izquierda)
    a = list(a[::-1])
    b = list(b[::-1])

    # Variables
    carry = 0
    resultado = []

    # Sumar bit a bit (desde el menos significativo)
    for i in range(max(len(a), len(b))):
        bit1 = int(a[i]) if i < len(a) else 0
        bit2 = int(b[i]) if i < len(b) else 0
        s = bit1 + bit2 + carry
        resultado.append(str(s % 2))
        carry = s // 2

    if carry:
        resultado.append("1")

    # Invertir el resultado para devolverlo normal
    return "".join(resultado[::-1])


# Ejemplo de prueba
entrada = "1011#110"
salida = turing_sum_binarios(entrada)
print(f"Entrada: {entrada}")
print(f"Resultado: {salida}")


entrada = "1#1"
salida = turing_sum_binarios(entrada)
print(f"Entrada: {entrada}")
print(f"Resultado: {salida}")
