#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido,edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=input("ingrese su edad: ")
residencia=input("ingrese su residencia: ")
informacion_personal(nombre, apellido,edad, residencia)