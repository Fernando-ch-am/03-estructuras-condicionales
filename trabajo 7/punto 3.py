def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base_input = input("Introduce la base (número entero): ")
exponente_input = input("Introduce el exponente (entero no negativo): ")

es_valido = True
for c in base_input + exponente_input:
    if c not in "-0123456789":
        es_valido = False
        break

if es_valido and exponente_input.lstrip("-").isdigit():
    base = int(base_input)
    exponente = int(exponente_input)
    if exponente < 0:
        print("El exponente debe ser un entero no negativo.")
    else:
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
else:
    print("Entrada no válida. Asegúrate de ingresar números enteros.")