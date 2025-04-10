#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

cont_valores=2
valores=0
for cont in range(1,cont_valores+1):
    num=int(input(f"ingrese el n{cont}: "))
    cont=cont+1
    valores=valores+num
print(valores)


    