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
#### Hasta aca el Primer avance del proyecto

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
#### Hasta aca el Segundo avance del proyecto

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
#### Hasta aca el Tercer avance del proyecto
