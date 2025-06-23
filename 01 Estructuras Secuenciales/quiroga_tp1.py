# TP 1 – Estructuras Secuenciales – Camilo Quiroga
# UTN - Tecnicatura Universitaria en Programación a Distancia

import math

# 1. Hola Mundo
print("Hola Mundo!")

# 2. Saludo personalizado
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

# 3. Presentación completa
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Área y perímetro de un círculo
radio = float(input("Ingresá el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# 5. Segundos a horas
segundos = int(input("Ingresá la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6. Tabla de multiplicar
numero = int(input("Ingresá un número para ver su tabla: "))
print(f"Tabla del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones con dos números enteros distintos de cero
num1 = int(input("Ingresá el primer número (≠ 0): "))
num2 = int(input("Ingresá el segundo número (≠ 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2:.2f}")

# 8. Índice de Masa Corporal
peso = float(input("Ingresá tu peso en kg (ej: 70.5): "))
altura = float(input("Ingresá tu altura en metros (ej: 1.70): "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

# 9. Conversión de temperatura Celsius a Fahrenheit
celsius = float(input("Ingresá la temperatura en °C: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10. Promedio de 3 números
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio:.2f}")