#Nombre: Año bisiesto
#Entradas: Ingrese año
#Salida: El año ingresado es bisiesto o no
#Proceso: Se ingresa el año y luego el sistema verifica que el año se a bisiesto o no

año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")