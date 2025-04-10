#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
from random import randint

cont=0
num=randint(0,9)
numero_del_usuario=0

while numero_del_usuario!=num:
    numero_del_usuario=int(input("ingrese un numero del 0 al 9: "))
    cont+=1
    if -1>=numero_del_usuario>9:
        print("este numero esta fuera del rango")
else:
    print(f"correcto!, el numero era {num} y tus intentos fueron {cont}")
