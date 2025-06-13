#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print("\n🟢 Palabras únicas:")
print(palabras_unicas)

contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("\n🔢 Cantidad de veces que aparece cada palabra:")
print(contador_palabras)