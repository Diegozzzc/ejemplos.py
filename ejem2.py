calificaciones = [[0] * 6 for _ in range(100)]

import random
for i in range(100):
    for j in range(6):
        calificaciones[i][j] = random.randint(60, 100)  

for i in range(100):
    print(f"Alumno {i + 1}: {calificaciones[i]}")

alumno_buscar = 95
materia_buscar = 5

if 1 <= alumno_buscar <= 100 and 1 <= materia_buscar <= 6:
    calificacion = calificaciones[alumno_buscar - 1][materia_buscar - 1]
    print(f"La calificación del alumno {alumno_buscar} en la materia {materia_buscar} es: {calificacion}")
else:
    print("Número de alumno o materia fuera de rango. Deben estar entre 1 y 100 para alumnos y 1 y 6 para materias.")
