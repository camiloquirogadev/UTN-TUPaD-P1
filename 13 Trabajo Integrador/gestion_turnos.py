from datetime import datetime               # Para convertir y comparar horarios
from time import time                       # Para medir tiempo de ejecución
from memory_profiler import memory_usage    # Para medir uso de memoria
import matplotlib.pyplot as plt             # Para graficar los resultados
import random                               # Para generar turnos aleatorios

# Función auxiliar: convierte "HH:MM" a datetime para poder comparar horas
def hora_a_datetime(hora_str):
    return datetime.strptime(hora_str, "%H:%M")

# Algoritmo Insertion Sort adaptado a horarios de turnos
def insertion_sort_por_hora(turnos):
    for i in range(1, len(turnos)):
        actual = turnos[i]                 # Turno actual a ubicar en su lugar correcto
        j = i - 1                          # Índice anterior
        # Mientras no llegamos al inicio y el turno anterior es posterior al actual
        while j >= 0 and hora_a_datetime(turnos[j]["hora"]) > hora_a_datetime(actual["hora"]):
            turnos[j + 1] = turnos[j]      # Desplazamos el turno hacia la derecha
            j -= 1
        turnos[j + 1] = actual             # Insertamos el turno actual en la posición correcta
    return turnos

# Búsqueda lineal por número de documento (DNI)
def buscar_por_dni(turnos, dni):
    for turno in turnos:
        if turno["dni"] == dni:
            return turno                   # Devuelve el turno si lo encuentra
    return None                            # Si no está, devuelve None

# Lista de turnos fija, simulando una base de datos chica
turnos = [
    {"dni": 34567123, "nombre": "Lucía López", "hora": "10:30"},
    {"dni": 29876123, "nombre": "Carlos Pérez", "hora": "09:00"},
    {"dni": 41678901, "nombre": "Ana Toro", "hora": "11:15"},
    {"dni": 37890123, "nombre": "Julián Quiroga", "hora": "08:45"},
    {"dni": 30987654, "nombre": "Laura González", "hora": "09:45"}
]

# Medimos el tiempo y el uso de memoria de la ordenación
start_time = time()
mem_before = memory_usage()[0]

turnos_ordenados = insertion_sort_por_hora(turnos)

mem_after = memory_usage()[0]
end_time = time()

# Mostramos los turnos ya ordenados por hora
print("Turnos ordenados por hora:")
for turno in turnos_ordenados:
    print(f'{turno["hora"]} - {turno["nombre"]} ({turno["dni"]})')

# Imprimimos el tiempo de ejecución y el uso de memoria
print(f"\n⏱ Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f" Memoria utilizada: {mem_after - mem_before:.4f} MiB")

# Búsqueda por DNI
dni_a_buscar = 30987654
resultado = buscar_por_dni(turnos_ordenados, dni_a_buscar)

print("\n Resultado de la búsqueda:")
if resultado:
    print(f'Turno encontrado: {resultado["hora"]} - {resultado["nombre"]}')
else:
    print("Paciente no encontrado.")

# -------- PRUEBA DE RENDIMIENTO CON LISTAS DE DISTINTO TAMAÑO -------- #

# Genera turnos aleatorios para simular bases de datos más grandes
def generar_turnos(n):
    turnos = []
    for i in range(n):
        hora = f"{random.randint(8, 18)}:{random.choice(['00', '15', '30', '45'])}"
        turnos.append({
            "dni": random.randint(20000000, 45000000),
            "nombre": f"Paciente {i+1}",
            "hora": hora
        })
    return turnos

# Lista de tamaños a probar y lista para guardar los tiempos medidos
tamaños = [10, 100, 500, 1000, 2000]
tiempos = []

# Medimos el tiempo que tarda Insertion Sort en cada caso
for n in tamaños:
    datos = generar_turnos(n)
    inicio = time()
    insertion_sort_por_hora(datos)
    fin = time()
    tiempos.append(fin - inicio)

# Graficamos los resultados para visualizar la eficiencia
plt.plot(tamaños, tiempos, marker='o')
plt.title("Rendimiento de Insertion Sort")                  # Título del gráfico
plt.xlabel("Cantidad de turnos")                            # Eje X
plt.ylabel("Tiempo de ejecución (segundos)")                # Eje Y
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_rendimiento.png")
print("📊 Gráfico guardado como 'grafico_rendimiento.png'")        