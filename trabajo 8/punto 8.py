#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
stock = {
    "manzanas": 10,
    "bananas": 5,
    "peras": 8
}

producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Querés agregar unidades? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print(f"{producto} no está en el inventario.")
    agregar_nuevo = input("¿Querés agregarlo? (s/n): ").lower()
    if agregar_nuevo == "s":
        unidades = int(input(f"¿Cuántas unidades querés agregar de {producto}?: "))
        stock[producto] = unidades
        print(f"{producto} fue agregado con un stock de {stock[producto]}")