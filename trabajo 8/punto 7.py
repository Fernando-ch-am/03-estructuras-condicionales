#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Estudiantes que aprobaron ambos parciales:", ambos)
print("Estudiantes que aprobaron solo uno de los dos:", solo_uno)
print("Estudiantes que aprobaron al menos un parcial:", al_menos_uno)