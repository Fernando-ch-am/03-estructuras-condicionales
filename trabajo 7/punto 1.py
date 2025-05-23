def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 1:
        print("Por favor, introduce un número entero mayor o igual a 1.")
    else:
        print(f"Factoriales del 1 al {numero}:")
        for i in range(1, numero + 1):
            print(f"{i}! = {factorial(i)}")
except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")