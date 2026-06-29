# --------------------------- DESCRIPCIÓN GENERAL ---------------------------
# En esta sección se realiza la configuración inicial del programa.
# Primero se importan los módulos necesarios para trabajar con fechas, horas
# y archivos del sistema. Luego se definen constantes que almacenan valores
# fijos, como el nombre del archivo de ventas, la cantidad mínima de productos
# requerida para aplicar un descuento y el porcentaje de dicho descuento.
# Finalmente, se carga la información de los restaurantes en una estructura
# de datos compuesta por una lista de diccionarios, donde cada restaurante
# contiene su nombre y un menú con productos, precios y toppings disponibles.
# Esta información será utilizada posteriormente por las distintas funciones
# del sistema para gestionar los pedidos y calcular los importes de cada venta.
# --------------------------------------------------------------------------

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


