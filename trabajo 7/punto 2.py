def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


entrada=input("Introduce una posición (número entero mayor o igual a 0): ")

es_entero = True
for caracter in entrada:
    if caracter not in "0123456789":
        es_entero = False
        break

if es_entero and entrada != "":
    posicion = int(entrada)
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")
else:
    print("Entrada no válida. Debes ingresar un número entero no negativo.")