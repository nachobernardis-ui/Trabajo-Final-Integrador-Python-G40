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
