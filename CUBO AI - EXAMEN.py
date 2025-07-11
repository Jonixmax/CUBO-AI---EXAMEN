# Función para aplicar un descuento
def aplicar_descuento(precio, porcentaje_descuento):
    return precio * (1 - porcentaje_descuento / 100)

# Función para aplicar IVA  (13%)
def aplicar_iva(precio):
    iva = 13
    return precio * (1 + iva / 100)

# Función para procesar la cesta de compra con descuento
def procesar_cesta_descuento(cesta, funcion_aplicar):
    total = 0
    print("\nDetalle de productos con descuento:")
    print("-" * 45)
    for producto, datos in cesta.items():
        precio = datos["precio"]
        descuento = datos["porcentaje"]
        precio_final = funcion_aplicar(precio, descuento)
        print(f"{producto:10} | Precio original: ${precio:.2f} → Con descuento: ${precio_final:.2f}")
        total += precio_final
    print("-" * 45)
    return total

# Función para procesar la cesta de compra con IVA 
def procesar_cesta_iva(cesta, funcion_aplicar):
    total = 0
    print("\nDetalle de productos con IVA (13%):")
    print("-" * 45)
    for producto, datos in cesta.items():
        precio = datos["precio"]
        precio_final = funcion_aplicar(precio)
        print(f"{producto:10} | Precio original: ${precio:.2f} → Con IVA: ${precio_final:.2f}")
        total += precio_final
    print("-" * 45)
    return total

# Cesta de productos
cesta_compra = {
    "PS4":       {"precio": 450, "porcentaje": 10},
    "Smart TV":  {"precio": 180, "porcentaje": 5},
    "Arduino":   {"precio":  20, "porcentaje": 17}
}

# Mostrar total con descuento 
print("\n TOTAL CON DESCUENTO:")
total_descuento = procesar_cesta_descuento(cesta_compra, aplicar_descuento)
print(f"Total a pagar con descuentos: ${total_descuento:.2f}")

# Mostrar total con IVA fijo del 13%
print("\n TOTAL CON IVA (13%):")
total_iva = procesar_cesta_iva(cesta_compra, aplicar_iva)
print(f"Total a pagar con IVA: ${total_iva:.2f}")
