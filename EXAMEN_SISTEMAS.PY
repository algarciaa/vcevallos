# ingreso de cantidad
while True:
    try:
        cantidad = int(input("INGRESE CANTIDAD DE ALUMNOS: "))
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad debe ser un numero entero positivo")
    except ValueError:
        print("Error: La cantidad debe ser un numero entero positivo")

# REGISTRO DE CALIFICACIONES
calificaciones = []

for i in range(cantidad):
    while True:
        try:
            nota = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
            # Validación del rango
            if 0.0 <= nota <= 10.0:
                calificaciones.append(nota)
                break
            else:
                print("Error: la calificación debe estar entre 0.0 y 10.0.")
        except ValueError:
            print("Error: debe ingresar un número válido.")

# --- Análisis de resultados ---
suma_notas = sum(calificaciones)
promedio = suma_notas / cantidad

aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 7.0:
        aprobados += 1
    else:
        reprobados += 1