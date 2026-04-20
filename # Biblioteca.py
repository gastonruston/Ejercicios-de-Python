# Biblioteca
Estado_usuario = input("¿Tiene entregas pendientes? Sí o No ")
if Estado_usuario == "Sí":
    print("No puede retirar libros")
elif Estado_usuario == "No":
    print("Puede retirar un libro")
else:
    print("Entrada inválida")
