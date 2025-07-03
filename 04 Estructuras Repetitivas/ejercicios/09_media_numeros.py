# 09_media_numeros.py
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

def main():
    cantidad = 100  # Cambiar este valor para probar con menos elementos
    total = 0

    for i in range(cantidad):
        x = int(input(f"Número {i+1}/{cantidad}: "))
        total += x

    promedio = total / cantidad if cantidad > 0 else 0
    print(f"El promedio de los {cantidad} números es: {promedio:.2f}")

if __name__ == "__main__":
    main()