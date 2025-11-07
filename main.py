
#ingreso de cantidad 
while True:
    try:
        cantidad = int(input("INGRESE CANTIDAD DE ALUMNOS: "))
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad debe ser un numero entero positivo")
    except ValueError:
        print("Error: La cantidad debe ser un numero entero positivo")

