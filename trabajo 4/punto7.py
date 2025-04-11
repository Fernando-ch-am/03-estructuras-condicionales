#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num=int(input("ingrese un numero positivo: "))
num2=num+1
suma=0
if num>0:
    for cont in range (1,num2):
       suma=suma+cont
    print(suma)
else: 
    print("porfavor ingrese un numero positivo")



