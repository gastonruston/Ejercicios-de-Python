# Supermercado
Compra = int(input("Ingresar el monto de la compra: "))
Con_descuento = Compra * 0.9
if Compra >= 10000:
    print(f"El importe total es: S", Con_descuento)
else:
    print(f"El importe total es: S", Compra)
