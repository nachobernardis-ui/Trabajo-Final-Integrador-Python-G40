# Importación de módulos necesarios
import datetime  # Permite guardar la fecha y hora de cada venta
import os        # Permite verificar si existe el archivo de ventas


# Constantes del sistema
ARCHIVO_VENTAS = "ventas.txt"
CANTIDAD_MINIMA_DESCUENTO = 3
PORCENTAJE_DESCUENTO = 0.20


# Lista de restaurantes disponibles
restaurantes = [
    "Burger House",
    "Pizza Point",
    "Sushi Go"
]


# Lista de productos de cada restaurante
productos = [
    ["Hamburguesa simple", "Papas fritas"],
    ["Pizza muzzarella", "Empanadas"],
    ["Combo sushi chico", "Arrolladitos primavera"]
]


# Lista de precios de cada producto
precios = [
    [3500, 2000],
    [6000, 800],
    [7000, 3000]
]


# Lista de toppings disponibles para cada producto
toppings_nombres = [
    [
        ["Queso extra", "Panceta"],
        ["Cheddar"]
    ],
    [
        ["Jamón", "Aceitunas"],
        ["Salsa picante"]
    ],
    [
        ["Salsa soja extra", "Wasabi"],
        ["Salsa agridulce"]
    ]
]


# Lista de precios de los toppings
toppings_precios = [
    [
        [500, 800],
        [700]
    ],
    [
        [1000, 500],
        [200]
    ],
    [
        [300, 300],
        [400]
    ]
]
#### Hasta aca el Primer avance del proyecto


# Estadísticas iniciales de ventas por restaurante
pedidos_restaurante = [0, 0, 0]
productos_restaurante = [0, 0, 0]
total_restaurante = [0, 0, 0]


# Crea el archivo de ventas si todavía no existe
def verificar_archivo():
    if not os.path.exists(ARCHIVO_VENTAS):
        archivo = open(ARCHIVO_VENTAS, "w", encoding="utf-8")
        archivo.write("REGISTRO DE VENTAS\n")
        archivo.close()


# Obtiene la fecha y hora actual del sistema
def fecha_actual():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# Lee una opción numérica y valida que esté dentro del rango permitido
def leer_opcion(mensaje, limite):
    while True:
        try:
            opcion = int(input(mensaje))

            if opcion >= 1 and opcion <= limite:
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


# Lee una respuesta válida de sí o no
def leer_respuesta(mensaje):
    while True:
        respuesta = input(mensaje).lower()

        if respuesta == "s" or respuesta == "n":
            return respuesta

        print("Respuesta inválida. Ingresá s o n.")
#### Hasta aca el Segundo avance del proyecto


# Muestra los restaurantes disponibles y permite elegir uno
def elegir_restaurante():
    print("\nRestaurantes disponibles:")

    for i in range(len(restaurantes)):
        print(f"{i + 1}) {restaurantes[i]}")

    indice = leer_opcion("Seleccione un restaurante: ", len(restaurantes))
    return indice


# Permite elegir si el pedido es para comer en el local o para llevar
def elegir_modalidad():
    print("\nModalidad del pedido")
    print("1) Comer en el local")
    print("2) Para llevar")

    opcion = leer_opcion("Seleccione una opción: ", 2)

    if opcion == 0:
        return "Comer en el local"
    else:
        return "Para llevar"


# Permite agregar toppings al producto elegido
def elegir_toppings(indice_restaurante, indice_producto):
    toppings_elegidos = []
    precios_elegidos = []

    respuesta = leer_respuesta("¿Desea agregar toppings? s/n: ")

    while respuesta == "s":
        print("\nToppings disponibles:")

        cantidad_toppings = len(toppings_nombres[indice_restaurante][indice_producto])

        for i in range(cantidad_toppings):
            nombre = toppings_nombres[indice_restaurante][indice_producto][i]
            precio = toppings_precios[indice_restaurante][indice_producto][i]
            print(f"{i + 1}) {nombre} - ${precio}")

        indice_topping = leer_opcion("Seleccione un topping: ", cantidad_toppings)

        nombre_topping = toppings_nombres[indice_restaurante][indice_producto][indice_topping]
        precio_topping = toppings_precios[indice_restaurante][indice_producto][indice_topping]

        toppings_elegidos.append(nombre_topping)
        precios_elegidos.append(precio_topping)

        respuesta = leer_respuesta("¿Desea agregar otro topping? s/n: ")

    return toppings_elegidos, precios_elegidos


# Permite seleccionar productos y armar el pedido completo
def seleccionar_productos(indice_restaurante):
    pedido = []
    seguir = "s"

    while seguir == "s":
        print(f"\nMenú de {restaurantes[indice_restaurante]}:")

        cantidad_productos = len(productos[indice_restaurante])

        for i in range(cantidad_productos):
            nombre = productos[indice_restaurante][i]
            precio = precios[indice_restaurante][i]
            print(f"{i + 1}) {nombre} - ${precio}")

        indice_producto = leer_opcion("Seleccione un producto: ", cantidad_productos)

        nombre_producto = productos[indice_restaurante][indice_producto]
        precio_producto = precios[indice_restaurante][indice_producto]
        cantidad = leer_cantidad()

        toppings_elegidos, precios_toppings = elegir_toppings(indice_restaurante, indice_producto)

        producto_pedido = [
            nombre_producto,
            precio_producto,
            cantidad,
            toppings_elegidos,
            precios_toppings
        ]

        pedido.append(producto_pedido)

        seguir = leer_respuesta("¿Desea agregar otro producto? s/n: ")

    return pedido
#### Hasta aca el Tercer avance del proyecto


# Calcula el total sumando precio base, toppings y cantidad
def calcular_total(pedido):
    total = 0

    for item in pedido:
        precio_producto = item[1]
        cantidad = item[2]
        precios_toppings = item[4]

        total_toppings = 0

        for precio in precios_toppings:
            total_toppings = total_toppings + precio

        subtotal = (precio_producto + total_toppings) * cantidad
        total = total + subtotal

    return total


# Cuenta la cantidad total de productos comprados
def contar_productos(pedido):
    cantidad_total = 0

    for item in pedido:
        cantidad_total = cantidad_total + item[2]

    return cantidad_total


# Aplica descuento si la compra supera los 3 productos
def aplicar_descuento(total, cantidad_productos):
    if cantidad_productos > CANTIDAD_MINIMA_DESCUENTO:
        descuento = total * PORCENTAJE_DESCUENTO
    else:
        descuento = 0

    total_final = total - descuento
    return descuento, total_final


# Actualiza las estadísticas del restaurante elegido
def registrar_venta(indice_restaurante, cantidad_productos, total_final):
    pedidos_restaurante[indice_restaurante] = pedidos_restaurante[indice_restaurante] + 1
    productos_restaurante[indice_restaurante] = productos_restaurante[indice_restaurante] + cantidad_productos
    total_restaurante[indice_restaurante] = total_restaurante[indice_restaurante] + total_final


# Guarda la venta realizada en ventas.txt
def guardar_venta(restaurante, modalidad, cantidad_productos, total_final, descuento):
    archivo = open(ARCHIVO_VENTAS, "a", encoding="utf-8")

    archivo.write(f"\nFecha: {fecha_actual()}\n")
    archivo.write(f"Restaurante: {restaurante}\n")
    archivo.write(f"Modalidad: {modalidad}\n")
    archivo.write(f"Productos vendidos: {cantidad_productos}\n")
    archivo.write(f"Descuento aplicado: ${descuento}\n")
    archivo.write(f"Total vendido: ${total_final}\n")
    archivo.write("-----------------------------\n")

    archivo.close()


# Muestra el resumen del pedido realizado
def mostrar_resumen(restaurante, modalidad, pedido, total, descuento, total_final):
    print("\nResumen del pedido")
    print(f"Restaurante: {restaurante}")
    print(f"Modalidad: {modalidad}")

    for item in pedido:
        print(f"\nProducto: {item[0]}")
        print(f"Cantidad: {item[2]}")

        if len(item[3]) > 0:
            print("Toppings:")

            for i in range(len(item[3])):
                print(f"- {item[3][i]}: ${item[4][i]}")
        else:
            print("Toppings: sin toppings")

    print(f"\nTotal sin descuento: ${total}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Total final: ${total_final}")


# Muestra las estadísticas acumuladas de todos los restaurantes
def mostrar_estadisticas():
    print("\nEstadísticas de ventas por restaurante")

    for i in range(len(restaurantes)):
        print(f"\nRestaurante: {restaurantes[i]}")
        print(f"Pedidos realizados: {pedidos_restaurante[i]}")
        print(f"Productos vendidos: {productos_restaurante[i]}")
        print(f"Total vendido: ${total_restaurante[i]}")
#### Hasta aca el Cuarto avance del proyecto

# Realiza todo el proceso de un pedido
def realizar_pedido():
    indice_restaurante = elegir_restaurante()
    modalidad = elegir_modalidad()
    pedido = seleccionar_productos(indice_restaurante)

    total = calcular_total(pedido)
    cantidad_productos = contar_productos(pedido)
    descuento, total_final = aplicar_descuento(total, cantidad_productos)

    registrar_venta(indice_restaurante, cantidad_productos, total_final)
    guardar_venta(restaurantes[indice_restaurante], modalidad, cantidad_productos, total_final, descuento)
    mostrar_resumen(restaurantes[indice_restaurante], modalidad, pedido, total, descuento, total_final)


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
#### Hasta aca el Quinto avance del proyecto