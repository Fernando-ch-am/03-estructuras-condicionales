#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return 3.141592 * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * 3.141592 * radio

radio=float(input("ingrese el radio:"))

print(f"el area es:{calcular_area_circulo(radio)}")
print(f"el perimetro: {calcular_perimetro_circulo(radio)}")