#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
     return print(f"tu imc es igual a: {peso / (altura ** 2)}")

peso=float(input("ingrese su peso: "))
altura=float(input("ingrese su altura: "))
calcular_imc(peso, altura)