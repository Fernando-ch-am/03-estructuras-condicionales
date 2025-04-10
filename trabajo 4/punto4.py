#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
total = 0  # Inicializa la variable para acumular la suma
numero=1
while numero>0:
     numero=int(input("Ingrese un número entero (0 para terminar): "))
     total=total+numero

if numero==0:
    print("El total acumulado es:", total)

