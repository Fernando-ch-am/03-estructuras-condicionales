#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    return print(f"suma: {a + b} resta: {a - b} multiplicacion: {a * b} divicion: {a / b}")

num1=int(input("ingrese numero 1: "))
num2=int(input("ingrese numero 2: "))
operaciones_basicas(num1, num2)