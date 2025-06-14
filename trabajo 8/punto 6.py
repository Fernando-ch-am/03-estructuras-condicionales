#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
alumnos = {}

nombre1 = input("Nombre del alumno 1: ")
notas1 = (float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: ")))
alumnos[nombre1] = notas1

nombre2 = input("Nombre del alumno 2: ")
notas2 = (float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: ")))
alumnos[nombre2] = notas2

nombre3 = input("Nombre del alumno 3: ")
notas3 = (float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: ")))
alumnos[nombre3] = notas3

print("\nPromedios:")
print(f"{nombre1}: {sum(notas1)/3:.2f}")
print(f"{nombre2}: {sum(notas2)/3:.2f}")
print(f"{nombre3}: {sum(notas3)/3:.2f}")