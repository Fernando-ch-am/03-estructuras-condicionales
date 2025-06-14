#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
agenda = {
    ("lunes", "10:00"): "Reunión con el equipo",
    ("martes", "14:00"): "Clase de programación",
    ("miércoles", "09:00"): "Gimnasio",
    ("viernes", "18:00"): "Cine con amigos"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Evento: {agenda[clave]}")
else:
    print("No hay eventos programados en ese día y hora.")