# 1. imprimir_hola_mundo()

def imprimir_hola_mundo():
    print("Hola Mundo!")

if __name__ == "__main__":
    imprimir_hola_mundo()

# 2. saludar_usuario(nombre)

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre))

# 3. informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

if __name__ == "__main__":
    datos = [
        input("Nombre: "),
        input("Apellido: "),
        input("Edad: "),
        input("Residencia: ")
    ]
    informacion_personal(*datos)

# 4. Área y perímetro de un círculo

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    r = float(input("Radio del círculo (en unidades): "))
    print(f"Área: {calcular_area_circulo(r):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(r):.2f}")

# 5. segundos_a_horas(segundos)

def segundos_a_horas(segundos):
    return segundos / 3600

if __name__ == "__main__":
    seg = int(input("Cantidad de segundos: "))
    print(f"{seg} segundos → {segundos_a_horas(seg):.2f} horas")

# 6. tabla_multiplicar(numero)

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    num = int(input("Número para la tabla: "))
    tabla_multiplicar(num)

# 7. operaciones_basicas(a, b)

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b if b != 0 else None
    return suma, resta, mult, div

if __name__ == "__main__":
    x, y = map(float, input("Ingresa dos números separados por espacio: ").split())
    suma, resta, mult, div = operaciones_basicas(x, y)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {mult}")
    print(f"División: {div if div is not None else 'Error: división por cero'}")

# 8. calcular_imc(peso, altura)

def calcular_imc(peso, altura):
    return peso / altura**2

if __name__ == "__main__":
    p = float(input("Peso (kg): "))
    h = float(input("Altura (m): "))
    print(f"IMC: {calcular_imc(p, h):.2f}")

# 9. celsius_a_fahrenheit(celsius)

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

if __name__ == "__main__":
    c = float(input("Temperatura en °C: "))
    print(f"{c}°C → {celsius_a_fahrenheit(c):.2f}°F")

# 10. calcular_promedio(a, b, c)

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    valores = list(map(float, input("Ingresa tres números separados por espacio: ").split()))
    print(f"Promedio: {calcular_promedio(*valores):.2f}")


