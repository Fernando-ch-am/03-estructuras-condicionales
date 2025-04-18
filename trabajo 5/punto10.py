#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.
def calcular_promedio(a, b, c):
    return print(f"el promedio es: {(a + b + c) / 3}")

num1=int(input("ingrese num1: "))
num2=int(input("ingrese num2: "))
num3=int(input("ingrese num3: "))
calcular_promedio(num1, num2, num3)