#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(seg):
    return print(f"{seg / 3600} hs")

segundos_a_horas(seg=float(input("ingrese una cantidad de segundos: ")))