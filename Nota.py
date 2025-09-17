#Nombre: Nota
#Entradas: Ingrese la nota del estudiante
#Salida: El estudianteaprobo o reprobo
#Proceso: Ingrese la nota del estudiante y el sistema verifica si aprobo o reprobo

nota = float(input("Ingresa la nota del estudiante: "))
if nota >= 60:
    print("El estudiante aprobó.")
else:
    print("El estudiante reprobó.")