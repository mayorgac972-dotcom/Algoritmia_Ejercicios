#Nombre: Congelacion
#Entradas: Ingrese la temperatura
#Salida: Latemperatura es acta o no para la congelacion
#Proceso: Ingrese la temperatura y luego le indica si las temperaturas es acta o no para la congelacion

temperatura = float(input("Ingresa la temperatura en °C: "))
if temperatura <= 0:
    print("La temperatura es adecuada para congelación.")
else:
    print("La temperatura no es adecuada para congelación.")