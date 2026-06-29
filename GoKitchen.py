# Importación de módulos necesarios
import datetime  # Permite guardar la fecha y hora de cada venta
import os        # Permite verificar si existe el archivo de ventas


# Constantes del sistema
ARCHIVO_VENTAS = "ventas.txt"
CANTIDAD_MINIMA_DESCUENTO = 3
PORCENTAJE_DESCUENTO = 0.20


# Lista de restaurantes con sus productos y toppings
restaurantes = [
    {
        "nombre": "Burger House",
        "menu": [
            ("Hamburguesa simple", 3500, [("Queso extra", 500), ("Panceta", 800)]),
            ("Papas fritas", 2000, [("Cheddar", 700)])
        ]
    },
    {
        "nombre": "Pizza Point",
        "menu": [
            ("Pizza muzzarella", 6000, [("Jamón", 1000), ("Aceitunas", 500)]),
            ("Empanadas", 800, [("Salsa picante", 200)])
        ]
    },
    {
        "nombre": "Sushi Go",
        "menu": [
            ("Combo sushi chico", 7000, [("Salsa soja extra", 300), ("Wasabi", 300)]),
            ("Arrolladitos primavera", 3000, [("Salsa agridulce", 400)])
        ]
    }
]


# Estadísticas iniciales de ventas por restaurante
estadisticas = [
    {"restaurante": restaurante["nombre"], "pedidos": 0, "productos": 0, "total": 0}
    for restaurante in restaurantes
]


# Crea el archivo de ventas si todavía no existe
def verificar_archivo():
    if not os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
            archivo.write("REGISTRO DE VENTAS\n")


# Obtiene la fecha y hora actual del sistema
def fecha_actual():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# Lee una opción numérica y valida que esté dentro del rango permitido
def leer_opcion(mensaje, limite):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= limite:
                return opcion - 1  # Se resta 1 porque las listas empiezan en 0
            print("Opción inválida.")
        except ValueError:
            print("Ingresá un número válido.")


# Lee una cantidad válida de productos
def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad > 0:
                return cantidad
            print("La cantidad debe ser mayor a 0.")
        except ValueError:
            print("Ingresá un número válido.")


# Muestra los restaurantes disponibles y permite elegir uno
def elegir_restaurante():
    print("\nRestaurantes disponibles:")

    for i, restaurante in enumerate(restaurantes, start=1):
        print(f"{i}) {restaurante['nombre']}")

    indice = leer_opcion("Seleccione un restaurante: ", len(restaurantes))
    return indice, restaurantes[indice]


# Permite elegir si el pedido es para comer en el local o para llevar
def elegir_modalidad():
    print("\nModalidad del pedido")
    print("1) Comer en el local")
    print("2) Para llevar")

    opcion = leer_opcion("Seleccione una opción: ", 2)

    if opcion == 0:
        return "Comer en el local"

    return "Para llevar"


# Permite agregar toppings al producto elegido
def elegir_toppings(toppings):
    elegidos = []
    respuesta = input("¿Desea agregar toppings? s/n: ").lower()

    while respuesta == "s":
        print("\nToppings disponibles:")

        for i, (nombre, precio) in enumerate(toppings, start=1):
            print(f"{i}) {nombre} - ${precio}")

        indice = leer_opcion("Seleccione un topping: ", len(toppings))
        elegidos.append(toppings[indice])  # Guarda el topping elegido

        respuesta = input("¿Desea agregar otro topping? s/n: ").lower()

    return elegidos


# Permite seleccionar productos y armar el pedido completo
def seleccionar_productos(restaurante):
    pedido = []
    seguir = "s"

    while seguir == "s":
        print(f"\nMenú de {restaurante['nombre']}:")

        for i, (nombre, precio, toppings) in enumerate(restaurante["menu"], start=1):
            print(f"{i}) {nombre} - ${precio}")

        indice = leer_opcion("Seleccione un producto: ", len(restaurante["menu"]))

        # Se desarma la tupla del producto elegido
        nombre, precio, toppings = restaurante["menu"][indice]

        pedido.append({
            "producto": nombre,
            "precio": precio,
            "cantidad": leer_cantidad(),
            "toppings": elegir_toppings(toppings)
        })

        seguir = input("¿Desea agregar otro producto? s/n: ").lower()

    return pedido


# Calcula el total sumando precio base, toppings y cantidad
def calcular_total(pedido):
    total = 0

    for item in pedido:
        total_toppings = sum(precio for nombre, precio in item["toppings"])
        total += (item["precio"] + total_toppings) * item["cantidad"]

    return total


# Cuenta la cantidad total de productos comprados
def contar_productos(pedido):
    return sum(item["cantidad"] for item in pedido)


# Aplica descuento si la compra supera los 3 productos
def aplicar_descuento(total, cantidad_productos):
    if cantidad_productos > CANTIDAD_MINIMA_DESCUENTO:
        descuento = total * PORCENTAJE_DESCUENTO
    else:
        descuento = 0

    return descuento, total - descuento


# Actualiza las estadísticas del restaurante elegido
def registrar_venta(indice_restaurante, cantidad_productos, total_final):
    estadisticas[indice_restaurante]["pedidos"] += 1
    estadisticas[indice_restaurante]["productos"] += cantidad_productos
    estadisticas[indice_restaurante]["total"] += total_final


# Guarda la venta realizada en ventas.txt
def guardar_venta(restaurante, modalidad, cantidad_productos, total_final):
    with open(ARCHIVO_VENTAS, "a", encoding="utf-8") as archivo:
        archivo.write(f"\nFecha: {fecha_actual()}\n")
        archivo.write(f"Restaurante: {restaurante}\n")
        archivo.write(f"Modalidad: {modalidad}\n")
        archivo.write(f"Productos vendidos: {cantidad_productos}\n")
        archivo.write(f"Total vendido: ${total_final}\n")
        archivo.write("-----------------------------\n")


# Muestra el resumen del pedido realizado
def mostrar_resumen(restaurante, modalidad, pedido, total, descuento, total_final):
    print("\nResumen del pedido")
    print(f"Restaurante: {restaurante}")
    print(f"Modalidad: {modalidad}")

    for item in pedido:
        print(f"\nProducto: {item['producto']}")
        print(f"Cantidad: {item['cantidad']}")

        if item["toppings"]:
            print("Toppings:")
            for nombre, precio in item["toppings"]:
                print(f"- {nombre}: ${precio}")
        else:
            print("Toppings: sin toppings")

    print(f"\nTotal sin descuento: ${total}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Total final: ${total_final}")


# Muestra las estadísticas acumuladas de todos los restaurantes
def mostrar_estadisticas():
    print("\nEstadísticas de ventas por restaurante")

    for datos in estadisticas:
        print(f"\nRestaurante: {datos['restaurante']}")
        print(f"Pedidos realizados: {datos['pedidos']}")
        print(f"Productos vendidos: {datos['productos']}")
        print(f"Total vendido: ${datos['total']}")


# Realiza todo el proceso de un pedido
def realizar_pedido():
    indice, restaurante = elegir_restaurante()
    modalidad = elegir_modalidad()
    pedido = seleccionar_productos(restaurante)

    total = calcular_total(pedido)
    cantidad_productos = contar_productos(pedido)
    descuento, total_final = aplicar_descuento(total, cantidad_productos)

    registrar_venta(indice, cantidad_productos, total_final)
    guardar_venta(restaurante["nombre"], modalidad, cantidad_productos, total_final)
    mostrar_resumen(restaurante["nombre"], modalidad, pedido, total, descuento, total_final)


# Menú principal del programa
def menu():
    verificar_archivo()

    while True:
        print("""
--- SISTEMA DE PEDIDOS DE COMIDA ---
1. Realizar pedido
2. Ver estadísticas de ventas
3. Salir
""")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            realizar_pedido()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


# Ejecución del programa
menu()