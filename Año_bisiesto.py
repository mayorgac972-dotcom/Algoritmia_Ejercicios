# Nombre: Año bisiesto
# Entradas: Año a verificar
# Salida: Indica si el año es bisiesto o no
# Proceso: Pide el año, lo toma y verifica si es divisible entre cuatro para saber si es bisiesto o no

año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")