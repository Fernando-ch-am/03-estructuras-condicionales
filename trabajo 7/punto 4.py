def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = input("Introduce un número entero positivo: ")

es_valido = True
for c in numero:
    if c not in "0123456789":
        es_valido = False
        break

if es_valido and numero != "":
    n = int(numero)
    if n >= 0:
        binario = decimal_a_binario(n)
        print(f"El número {n} en binario es: {binario}")
    else:
        print("El número debe ser positivo.")
else:
    print("Entrada no válida. Ingresa un número entero positivo.")