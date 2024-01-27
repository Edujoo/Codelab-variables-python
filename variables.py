# Define variables de diferentes tipos primitivos
entero = 3
flotante = 1.04
cadena = "Hola, soy una cadena"

# Concatena las variables aplicando conversiones
resultado_concatenacion = cadena + str(entero) + str(flotante)

# Imprimir el resultado de la concatenación
print("Resultado de la concatenación:", resultado_concatenacion)

# Límites de los enteros y flotantes en Python (investigacion)
"""
En Python, los enteros no tienen límite práctico, ya que pueden crecer hasta el límite de la memoria disponible en la máquina.
Para los flotantes, Python utiliza el estándar de punto flotante de doble precisión (64 bits), lo que implica un límite en la magnitud y la precisión.

Límite de los enteros en Python 3:
- Depende de la arquitectura de la máquina y de la versión de Python.
- En sistemas de 64 bits, el límite es 2^63 - 1.

Límite de los flotantes en Python 3:
- Dependiendo de la implementación, el límite de precisión es de aproximadamente 15 dígitos decimales significativos.
- El límite de magnitud es aproximadamente 1.8 × 10^308.
"""

# Suma de los primeros n números pares = n * (n + 1)
# Solicita al usuario ingresar un número entero para n
n = int(input("Se solicita que ingrese un número entero: "))

# Aplica la fórmula de la suma de los primeros n números pares
suma_pares = n * (n + 1)

# Imprime el resultado de la suma de los primeros n números pares
print(f"Resultado de la suma de los primeros {n} números pares:", suma_pares)


