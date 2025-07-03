# Práctico 6: Estructuras de Datos Complejas – Programación 1 
# Ejercicio 1: Añadir frutas al diccionario 
precios_frutas = {
    'Manzana':   1200,
    'Pera':  1400,
    'Durazno':       1800,
    'Frutilla':      1600
}
precios_frutas["Mandarina"] = 1100
precios_frutas["Ciruela"]    = 2000
precios_frutas["Pomelo"]      = 2200
print("1) Tras añadir frutas:", precios_frutas)
# Salida esperada:
# {'Manzana': 1200, 'Pera': 1400, 'Durazno': 1800, 'Frutilla': 1600,
#  'Mandarina': 1100, 'Ciruela': 2000, 'Pomelo': 2200}

# Ejercicio 2: Actualizar precios (promociones del día)
precios_frutas["Manzana"] = 1300
precios_frutas["Durazno"]     = 1700
precios_frutas["Frutilla"]    = 1500
print("2) Tras actualizar precios:", precios_frutas)
# Salida esperada:
# {'Manzana': 1300, 'Pera': 1400, 'Durazno': 1700, 'Frutilla': 1500,
#  'Mandarina': 1100, 'Ciruela': 2000, 'Pomelo': 2200}

# Ejercicio 3: Obtener solo las frutas (claves)
frutas = list(precios_frutas.keys())
print("3) Lista de frutas:", frutas)
# Salida esperada:
# ['Manzana', 'Pera', 'Durazno', 'Frutilla', 'Mandarina', 'Ciruela', 'Pomelo']

# Ejercicio 4: Agenda de contactos telefónicos 
contactos = {}
for _ in range(5):
    nombre = input("Ingresá nombre del contacto: ")
    numero = input(f"Ingresá teléfono de {nombre} (ej: 11-3456-7890 o 15-1234-5678): ")
    contactos[nombre] = numero

consulta = input("¿Qué contacto querés consultar? ")
if consulta in contactos:
    print(f"El teléfono de {consulta} es {contactos[consulta]}")
else:
    print("Contacto no encontrado.")
# Ejemplo de uso:
# Ingresá nombre del contacto: Martín
# Ingresá teléfono de Martín: 15-2345-6789
# …
# ¿Qué contacto querés consultar? Martín
# El teléfono de Martín es 15-2345-6789

# Ejercicio 5: Frase → palabras únicas + recuento
frase = input("Ingresá una frase: ")
palabras = frase.split()
unicas   = set(palabras)
recuento = {}
for p in palabras:
    recuento[p] = recuento.get(p, 0) + 1

print("5) Palabras únicas:", unicas)
print("   Recuento:", recuento)
# Si ingresás: "Llevo a mi perro a pasear por el parque y se pone muy feliz"
# Esperado:
# Palabras únicas: {'Llevo', 'a', 'mi', 'perro', 'pasear', 'por', 'el', 'parque', 'y', 'se', 'pone', 'muy', 'feliz'}
# Recuento: {
#   'Llevo': 1,
#   'a':      2,
#   'mi':     1,
#   'perro':  1,
#   'pasear': 1,
#   'por':    1,
#   'el':     1,
#   'parque': 1,
#   'y':      1,
#   'se':     1,
#   'pone':   1,
#   'muy':    1,
#   'feliz':  1
# }
# Ejercicio 6: Promedio de notas de alumnos (nombres locales)
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas  = [float(input(f"  Nota {i+1} de {nombre}: ")) for i in range(3)]
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} → Promedio: {promedio:.2f}")
# Por ejemplo:
# Nombre del alumno: Lautaro
#   Nota 1 de Lautaro: 8
#   Nota 2 de Lautaro: 7.5
#   Nota 3 de Lautaro: 9
# Lautaro → Promedio: 8.17

# Ejercicio 7: Operaciones con sets de aprobados (DNI de ejemplo)
parcial1 = {20333444, 27455667, 30500112}
parcial2 = {27455667, 30500112, 40222333}
print("7) Aprobados en ambos parciales:", parcial1 & parcial2)
print("   Aprobados solo en uno:      ", parcial1 ^ parcial2)
print("   Aprobados al menos uno:    ", parcial1 | parcial2)
# Salida esperada:
# Aprobados en ambos parciales: {27455667, 30500112}
# Aprobados solo en uno:       {20333444, 40222333}
# Aprobados al menos uno:     {20333444, 27455667, 30500112, 40222333}

# Ejercicio 8: Gestión de stock de productos (ítems de almacén local)
productos = {"yerba": 20, "fideos": 15, "pan": 30}
prod = input("Ingresá producto: ").lower()
if prod in productos:
    add = int(input(f"¿Cuántas unidades de {prod} agregás? "))
    productos[prod] += add
    print(f"Nuevo stock de {prod}: {productos[prod]} unidades")
else:
    stock = int(input("Producto nuevo. Stock inicial: "))
    productos[prod] = stock
    print(f"{prod.capitalize()} agregado con {stock} unidades.")
# Ejemplo:
# Ingresá producto: yerba
# ¿Cuántas unidades de yerba agregás? 10
# Nuevo stock de yerba: 30 unidades

# Ejercicio 9: Agenda por (día, hora) con actividades típicas
agenda = {
    ("martes",   "18:00"): "Asado con amigos",
    ("jueves",   "20:00"): "Clase de folklore",
    ("sábado",   "16:00"): "Cine"
}
d = input("Día: ").lower()
h = input("Hora (HH:MM): ")
evento = agenda.get((d, h))
print("Actividad:", evento if evento else "No hay actividad programada.")
# Ejemplo:
# Día: sábado
# Hora (HH:MM): 16:00
# Actividad: Cine

# Ejercicio 10: Invertir diccionario países → capitales (vecinos de la región)
paises = {
    "Argentina": "Buenos Aires",
    "Uruguay":   "Montevideo",
    "Paraguay":  "Asunción"
}
invertido = {capital: pais for pais, capital in paises.items()}
print("10) Original:", paises)
print("    Invertido:", invertido)
# Salida esperada:
# Original:  {'Argentina': 'Buenos Aires', 'Uruguay': 'Montevideo', 'Paraguay': 'Asunción'}
# Invertido: {'Buenos Aires': 'Argentina', 'Montevideo': 'Uruguay', 'Asunción': 'Paraguay'}