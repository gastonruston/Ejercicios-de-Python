# Contraseña segura El sistema pide una contraseña. Mientras no sea "python123", debe volver a solicitarla. Consigna: Usar while para validar el ingreso.


while True:
    Contraseña = input("Ingrese la contraseña: ")
    if Contraseña == "python123":
        break
    print ("Contraseña inválida")
print ("Acceso concedido")

    
    