# Nombre: Nota
# Entradas: Se pide al usuario que ingrese la nota
# Salida: Indica si la persona aprobó o no
# Proceso: Verifica, de acuerdo al año, el mínimo aprobatorio para pasar una materia 

NOTA_MINIMA_APROBATORIA = 70
nota = float(input("Por favor, ingrese la nota del estudiante: ")) 
if nota >= NOTA_MINIMA_APROBATORIA:
    print("¡Felicidades! El estudiante ha APROBADO.")
else:
    print("Lo sentimos, el estudiante ha REPROBADO.")