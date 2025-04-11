#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
cant_numeros=10
suma=0
for i in range(cant_numeros):
    num=int(input(f"ingrese el n{i+1}/{cant_numeros}: "))
    suma=suma+num
print(f"el promedio es: {suma/cant_numeros}")