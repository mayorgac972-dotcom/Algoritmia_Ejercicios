# Nombre: Congelación
# Entrada: Ingrese en qué temperatura se encuentra
# Salida: Indica si la temperatura es óptima o no para la congelación
# Proceso: Pide los grados y luego realiza una operación para saber si se puede congelar o no

temperatura = float(input("Ingresa la temperatura en °C: "))
if temperatura <= 0:
    print("La temperatura es adecuada para congelación.")
else:
    print("La temperatura no es adecuada para congelación.")