# Variables para almacenar los datos de entrada

nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))


# Calculo de total a pagar por el producto

subtotal = precio_unitario * cantidad_unidades
descuento = subtotal * 0.05  # Aplicando un descuento del 5%
total = subtotal - descuento

# Condicional para mostrar el descuento solo si es igual o mayor a 2 unidades

if cantidad_unidades >= 2:
    print("Nombre del producto: ", nombre_producto)
    print("Precio unitario: ", precio_unitario)
    print("Cantidad comprada: ", cantidad_unidades)
    print("Subtotal: ", subtotal)
    print("Descuento aplicado (5%): ", descuento)
    print("Total a pagar: ", total)
else:
    print("Nombre del producto: ", nombre_producto)
    print("Precio unitario: ", precio_unitario)
    print("Cantidad comprada: ", cantidad_unidades)
    print("Total a pagar: ", subtotal)

# Metodo de pago

medio_pago = input("Ingrese el medio de pago (efectivo, tarjeta): ")
print("Medio de pago seleccionado: ", medio_pago)
print("procesando su pago...")
print("Gracias por su compra. ¡Vuelva pronto!")