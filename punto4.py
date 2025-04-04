#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad=input("ingrese su edad: ")
edad=int(edad)
if(edad<12):
    print("niño/a")
elif(18>edad>=12):
    print("adolecente")
elif(30>edad<=18):
    print("adulto/a joven")
elif(edad>=30):
    print("adulto/a")