# Crear una matriz de calificaciones para 6 materias y 100 alumnos
calificaciones = [[0] * 100 for _ in range(6)]

# Llenar la matriz con calificaciones aleatorias (solo para propósitos de ejemplo)
import random
for i in range(6):
    for j in range(100):
        calificaciones[i][j] = random.randint(60, 100)  # Calificaciones aleatorias entre 60 y 100

# Mostrar la matriz de calificaciones (solo para propósitos de visualización)
print("Matriz de Calificaciones:")
for i in range(6):
    print(f"Materia {i + 1}: {calificaciones[i]}")

# Buscar la calificación del alumno 95 en la materia 5
alumno_buscar = 95
materia_buscar = 5

if 1 <= alumno_buscar <= 100 and 1 <= materia_buscar <= 6:
    calificacion = calificaciones[materia_buscar - 1][alumno_buscar - 1]
    print(f"La calificación del alumno {alumno_buscar} en la materia {materia_buscar} es: {calificacion}")
else:
    print("Número de alumno o materia fuera de rango. Deben estar entre 1 y 100 para alumnos y 1 y 6 para materias.")
